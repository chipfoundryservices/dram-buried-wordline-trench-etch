# Chapter 3 — Plasma Etch Fundamentals for Trenches

## 3.1 Ions, neutrals and the sheath

A low-pressure plasma supplies two populations to the wafer. **Neutrals** — radicals such as Cl, Br, F, O and CF_x — are many, slow and arrive from all directions with a roughly cosine distribution. **Ions** — Cl₂⁺, Br⁺, Ar⁺ and the like — are few, but are accelerated across the **sheath** to energies of tens to hundreds of electron-volts and arrive nearly perpendicular to the wafer.

The angular spread of the ions is set by the ratio of their transverse temperature to the sheath voltage. For a collisionless sheath, the characteristic angle is roughly θ ≈ √(kT_i / eV_s); with T_i ≈ 0.05–0.1 eV and V_s ≈ 100 V this gives two to three degrees. Collisions in the sheath at higher pressure broaden it. Chapter 5 uses σ = 2°, 4° and 8° to span the range.

## 3.2 Ion-neutral synergy

Neither population etches silicon or oxide efficiently on its own. Neutrals adsorb and form a halogenated surface layer; ions supply the energy to break bonds and eject products. The classic Coburn–Winters experiment showed that together they etch an order of magnitude faster than either alone.

A useful model treats the surface as a fraction θ covered by reactant. Neutrals fill it at a rate proportional to their flux Γ_n and the empty fraction; ions empty it at a rate proportional to their flux Γ_i and a yield. At steady state the etch rate becomes

R = 1 / (1/(aΓ_n) + 1/(bΓ_i)),

a series combination of a neutral-supply term and an ion-supply term. When aΓ_n ≪ bΓ_i the etch is **neutral-limited**; when bΓ_i ≪ aΓ_n it is **ion-limited**. Chapter 7 builds directly on this form.

## 3.3 Silicon and oxide behave differently

Silicon in Cl₂/HBr chemistries is etched by halogen radicals with modest ion help; the reaction is substantially neutral-limited at the energies used for trenches. Oxide needs much more ion energy to break Si–O bonds; in halogen chemistry it is strongly ion-limited, and in fluorocarbon chemistry it depends on a polymer film that ions must thin.

This difference is the central fact of word-line trench etch. One plasma meets two surfaces that want different things, and the trench's geometry filters the plasma differently for each.

## 3.4 Selectivity and loading

**Selectivity** is the ratio of etch rates of two materials. Three are relevant here: silicon to hard mask, silicon to oxide (or its inverse), and either to the nitride liner. **Loading** is the dependence of rate on the amount of exposed material; **microloading** is the dependence on local pattern density; **aspect-ratio-dependent etching (ARDE)** is the dependence on the feature's depth-to-width ratio. In a dense word-line array, ARDE dominates and is the subject of the next four chapters.

## 3.5 Passivation

Sidewalls are protected by a thin film of etch products and added gases — SiO_xBr_y from HBr/O₂, or CF_x polymer from fluorocarbons. The film is removed from the floor by ion bombardment but survives on the walls where ion flux is grazing. The balance between deposition and removal sets the taper angle (Chapter 8).
