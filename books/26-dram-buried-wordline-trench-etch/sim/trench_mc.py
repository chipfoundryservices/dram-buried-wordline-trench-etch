#!/usr/bin/env python3
"""Monte Carlo of ion and neutral delivery to the floor of a 2-D trench,
plus an ion-neutral synergy rate model that turns those fluxes into
etch-depth histories for silicon and STI oxide (saddle-fin formation).

Geometry (lengths in units of trench width w):
  trench: infinite along y, walls at x=0 and x=1, depth AR (z=0 top).
Neutrals: enter with a cosine distribution, re-emit diffusely at walls,
  lost at each wall hit with probability s (sticking coefficient).
Ions: enter with a Gaussian in-plane angle of standard deviation sigma,
  lost on the first wall hit (they feed sidewall etch / passivation).

Validation: with s = 1 the neutral result must equal the exact
line-of-sight (crossed-strings) value  W = sqrt(1 + AR^2) - AR.
Outputs: transport_results.csv and etch_results.csv.
"""
import csv, sys
import numpy as np

rng = np.random.default_rng(26)
ARS = [0.5, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15]
SS = [0.0, 0.01, 0.05, 0.2, 1.0]
SIGMAS = [2.0, 4.0, 8.0]          # ion angular spread, degrees
N = 300_000


def cosine_dir(n):
    u = rng.random(n)
    phi = 2 * np.pi * rng.random(n)
    return np.sqrt(u), np.sqrt(1 - u) * np.cos(phi)


def neutral(ar, s, n):
    x = rng.random(n)
    dz, dx = cosine_dir(n)
    z = np.zeros(n)
    thru = 0
    while x.size:
        with np.errstate(divide="ignore", invalid="ignore"):
            tw = np.where(dx > 0, (1 - x) / dx, np.where(dx < 0, -x / dx, np.inf))
            tz = np.where(dz > 0, (ar - z) / dz, np.where(dz < 0, -z / dz, np.inf))
        end = tz < tw
        t = np.minimum(tw, tz)
        x, z = x + dx * t, z + dz * t
        thru += int((end & (dz > 0)).sum())
        keep = ~end & (rng.random(x.size) >= s)
        x, z = np.where(x[keep] < .5, 0.0, 1.0), z[keep]
        nrm, tan = cosine_dir(x.size)
        dx, dz = np.where(x == 0.0, nrm, -nrm), tan
    return thru / n


def ion(ar, sigma_deg, n):
    x = rng.random(n)
    th = np.radians(sigma_deg) * rng.standard_normal(n)
    # lateral travel to the floor; reaches it if it stays inside 0..1
    xb = x + ar * np.tan(th)
    return float(np.mean((xb >= 0) & (xb <= 1)))


def rate(gi, gn, ratio):
    """Normalised synergy rate: R = 1 / (ratio/gn + 1/gi), R(top)=1.
    ratio = ion-to-neutral supply demand; large -> neutral-limited."""
    return (ratio + 1) / (ratio / max(gn, 1e-12) + 1 / max(gi, 1e-12))


def main():
    trows = []
    for ar in ARS:
        r = dict(AR=ar)
        for s in SS:
            r[f"n_s{s}"] = neutral(ar, s, N)
        for sg in SIGMAS:
            r[f"i_sig{sg}"] = ion(ar, sg, N)
        r["los_exact"] = (1 + ar * ar) ** .5 - ar
        trows.append(r)
        print(r, file=sys.stderr, flush=True)
    with open("transport_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=trows[0].keys())
        w.writeheader(); w.writerows(trows)

    # depth histories: Si (Cl2/HBr-type, neutral-limited, ratio 3, s=0.05)
    # and STI oxide (ion-limited, ratio 0.3, s=0.01); sigma = 4 deg.
    ar_g = np.array(ARS, float)
    gi = np.array([r["i_sig4.0"] for r in trows])
    gn = {s: np.array([r[f"n_s{s}"] for r in trows]) for s in (0.01, 0.05)}
    width = 20.0                                  # nm, trench CD
    mats = {"Si": (1.00, 3.0, 0.05), "SiO2": (0.80, 0.3, 0.01)}  # R0 rel, ratio, s
    erows = []
    dt = 0.05                                      # in units of t0 = w / R0_Si
    depth = {m: 0.0 for m in mats}
    t = 0.0
    while t <= 16.0 + 1e-9:
        row = dict(t=round(t, 3))
        for m, (r0, ratio, s) in mats.items():
            arr = depth[m] / width
            g_i = np.interp(arr, ar_g, gi, left=1.0)
            g_n = np.interp(arr, ar_g, gn[s], left=1.0)
            row[f"d_{m}"] = depth[m]
            row[f"R_{m}"] = r0 * rate(g_i, g_n, ratio)
        erows.append(row)
        for m in mats:
            depth[m] += row[f"R_{m}"] * width * dt
        t += dt
    with open("etch_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=erows[0].keys())
        w.writeheader(); w.writerows(erows)


if __name__ == "__main__":
    main()
