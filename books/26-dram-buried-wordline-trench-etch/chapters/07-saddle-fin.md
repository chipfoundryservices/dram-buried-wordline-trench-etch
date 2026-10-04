# Chapter 7 — The Silicon-Oxide Race and the Saddle Fin

## 7.1 The question

The word-line trench crosses silicon and oxide. At the end of etch, the oxide floor should sit 10–30 nm below the silicon floor so that the silicon forms a fin. How does a single plasma produce that offset, and how sensitive is it?

## 7.2 A rate model

Combine the synergy expression of Chapter 3 with the floor fluxes of Chapters 4 and 5. Normalise each flux to its value at the top of the trench, so Γ_n(AR) and Γ_i(AR) are the computed floor fractions. Write the rate of each material as

R(AR) = R₀ · (ρ + 1) / (ρ/Γ_n + 1/Γ_i),

where R₀ is the open-area rate and ρ measures how neutral-limited the material is (ρ ≫ 1: neutral-limited; ρ ≪ 1: ion-limited). At the top both fluxes are 1 and R = R₀.

The model in `sim/trench_mc.py` uses illustrative parameters:

| Material | R₀ (relative) | ρ | sticking s |
|---|---|---|---|
| Silicon | 1.00 | 3.0 | 0.05 |
| STI oxide | 0.80 | 0.3 | 0.01 |
| Ions | — | — | σ = 4° |

Width is 20 nm. Time is measured in t₀ = w / R₀(Si), the time to etch one trench width of silicon in open area. Depth is integrated step by step, with the local aspect ratio updated as the trench deepens.

## 7.3 Results

{{TABLE:etch}}

{{FIG:depth}}

The open-area rates favour silicon by 25 %, and for the first few nanometres silicon leads. But as the trench deepens, the silicon rate collapses with neutral delivery while the oxide rate, which depends mostly on ions, falls slowly. The oxide catches the silicon at t ≈ 3.95 t₀, at a depth of about 53 nm (AR ≈ 2.7), and pulls ahead thereafter. By t = 15 t₀ silicon has reached 130 nm and oxide 152 nm: a saddle fin of about 22 nm, formed purely by the geometry of transport.

## 7.4 Consequences

- **Fin height grows with depth.** Between t = 10 t₀ and 16 t₀ the fin grows by about 2 nm per t₀, while the silicon floor deepens by only 5–6 nm per t₀. A 5 % error in etch time therefore near t = 15 t₀ changes the fin by about 1.5 nm and the silicon depth by about 4 nm.
- **Fin height depends on width.** A narrower trench reaches a given aspect ratio sooner, so at fixed depth it has a taller fin. CD variation across the wafer becomes fin-height variation.
- **The silicon rate at end of etch is a quarter of open-area.** By t = 16 t₀ silicon etches at 0.26 R₀. Throughput is spent at the bottom.
- **Endpoint is invisible.** No interface is crossed; the etch is timed. Chapter 13 discusses how depth is measured instead.

## 7.5 Limits of the model

The model ignores charging, profile taper (which changes the effective width with depth), wall-film thickness, and the 3-D structure where silicon and oxide meet along the trench. Real fins are rounded where those effects act. The model's value is in showing the *mechanism* and the *sensitivities*, not in predicting a production depth.
