# Appendix E — Derivations

## E.1 Line-of-sight fraction of a 2-D slot

For two-dimensional diffuse radiation between surfaces, the view factor from surface 1 to surface 2 by the crossed-strings rule is (sum of crossed strings − sum of uncrossed strings) / (2 × length of surface 1). For an opening and floor of width 1 separated by AR, the crossed strings each have length √(1+AR²) and the uncrossed ones length AR, so F = √(1+AR²) − AR. At large AR, F ≈ 1/(2AR).

## E.2 Synergy rate law

Let θ be the fractional coverage of reactant. Adsorption: dθ/dt = s₀Γ_n(1−θ); removal: Y Γ_iθ. At steady state θ = s₀Γ_n/(s₀Γ_n + YΓ_i), and R ∝ YΓ_iθ = 1/(1/(s₀Γ_n) + 1/(YΓ_i)). Normalising to the open-area fluxes and defining ρ = YΓ_i⁰/(s₀Γ_n⁰) gives R/R₀ = (ρ+1)/(ρ/Γ_n + 1/Γ_i).

## E.3 Limits

- ρ → ∞: R/R₀ → Γ_n, purely neutral-limited.
- ρ → 0: R/R₀ → Γ_i, purely ion-limited.

## E.4 Crossover condition

Silicon (R₀ = 1, ρ_Si) and oxide (R₀ = r < 1, ρ_ox) etch at equal rates when (ρ_Si+1)/(ρ_Si/Γ_n,Si + 1/Γ_i) = r(ρ_ox+1)/(ρ_ox/Γ_n,ox + 1/Γ_i). With the Chapter 7 parameters the rates cross at about AR = 1.3 (a depth of 26 nm); the *depths* cross later, at AR ≈ 2.7, because oxide must first make up the lead silicon built early.

## E.5 Ion floor fraction

For a Gaussian angular spread, the floor fraction is the average over x ∈ [0,1] of P(−x ≤ AR tan θ ≤ 1−x). For small σ this is approximately 1 − AR·σ·√(2/π) when ARσ ≪ 1.
