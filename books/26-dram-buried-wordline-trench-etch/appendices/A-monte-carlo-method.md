# Appendix A — The Monte Carlo and Rate Model

## A.1 Neutral transport

Coordinates are in units of trench width; the walls are x = 0 and x = 1, the opening z = 0 and the floor z = AR. Only the in-plane components (x, z) of a direction matter, because motion along the trench does not change which surface is hit next.

A cosine-law direction about a surface normal is sampled as cos θ = √u, sin θ = √(1−u), with an azimuth φ uniform in [0, 2π); the in-plane tangential component is sin θ cos φ. Entering molecules use the downward normal; wall re-emission uses the inward normal of that wall.

For each molecule the distance to the next wall and to the next end (top or floor) is computed; the nearer one is hit. A floor hit is counted, a top hit is lost, and a wall hit is lost with probability s or re-emitted otherwise. All molecules are processed in vectorised batches.

## A.2 Ions

Ions start uniformly across the opening with an in-plane angle θ drawn from N(0, σ²). An ion reaches the floor if x + AR·tan θ lies within [0, 1]; otherwise it strikes a wall and is removed.

## A.3 Validation

For s = 1 the neutral floor fraction equals the line-of-sight view factor of the floor from the opening, √(1+AR²) − AR (crossed strings). Table 4.1 compares them. For the ion model the exact result is an error-function integral, which the code reproduces trivially.

## A.4 Rate model

R(AR)/R₀ = (ρ + 1)/(ρ/Γ_n + 1/Γ_i), with Γ_n and Γ_i linearly interpolated from the transport table. Depth is integrated by forward Euler with Δt = 0.05 t₀; halving the step changes depths by under 0.1 nm.

## A.5 Reproducing the results

```
cd sim
python3 trench_mc.py      # ~10 s, writes transport_results.csv and etch_results.csv
cd ..
python3 build/build.py    # regenerates tables, figures, HTML and EPUB
```

The random seed is fixed (26), so results are identical between runs.
