# Chapter 6 — Chemistry of the Word-Line Trench

## 6.1 The two jobs of the gas mix

The gas mixture must etch silicon and oxide at controlled relative rates, and it must passivate the sidewalls just enough to keep them straight. No single gas does both well, so mixtures are the rule.

## 6.2 Halogen chemistries for silicon

**HBr** is the backbone of silicon trench etch. Bromine is heavy, its silicon bromides are less volatile than chlorides, and the resulting SiBr_x deposits help passivate the walls. HBr etch is highly selective to oxide and photoresist.

**Cl₂** etches silicon faster and more isotropically. It is added to raise the rate and to adjust the profile.

**O₂** in small fractions oxidises redeposited SiBr_x into a more robust SiO_xBr_y wall film. A few percent O₂ can turn a bowed profile into a tapered one.

**NF₃ or SF₆** in small amounts add fluorine, which etches silicon spontaneously and isotropically; it is used to clean the walls of excess film and to round the trench floor.

## 6.3 Etching the oxide at the same time

Pure HBr/O₂ etches STI oxide slowly, because breaking Si–O bonds requires energetic ions. That is a feature, not a bug: it is this ion-limited oxide etch that lets the oxide catch up with silicon deep in the trench (Chapter 7). When a larger oxide-to-silicon depth difference is wanted, a fluorocarbon step (CF₄, CHF₃ or C₄F₈ with Ar) is added, either before the silicon step to pre-recess the STI, or after it to deepen the oxide only.

## 6.4 Multi-step recipes

A representative sequence is:

| Step | Purpose | Illustrative chemistry |
|---|---|---|
| Breakthrough | remove native oxide and residue | CF₄ / Ar, short |
| Main etch | silicon and oxide to near-final depth | HBr / Cl₂ / O₂ |
| Over-etch / fin | define fin height, round floor | HBr / O₂, lower bias; or CF_x / Ar for oxide |
| Soft landing | reduce damage | low-bias HBr / He |

The numbers in Chapter 7 refer to the main etch only.

## 6.5 By-products and the sticking coefficient

The sticking coefficient s used in Chapter 4 is the probability that a radical is lost at a wall. For Br on a SiO_xBr_y-covered wall s is small (perhaps 0.01–0.1); for O on the same wall it may be larger; for F on bare silicon it is high. Because neutral delivery to the floor depends so strongly on s, changing the wall chemistry changes the floor chemistry. A thick passivation film that consumes radicals also starves the floor.

## 6.6 Chamber condition

Halogen chemistry deposits on chamber walls, and the wall state changes the plasma's radical densities by tens of percent. Seasoning, wall temperature control and in-situ cleans are as much a part of the recipe as the gas flows; Chapter 15 returns to this as a source of lot-to-lot drift.
