# Chapter 10 — Reactor Knobs: Bias, Pulsing and Temperature

## 10.1 Tool type

Word-line trench etch runs in inductively coupled (ICP) or similar high-density reactors, where source power sets the plasma density and radical production and a separate bias supply on the wafer sets ion energy. That separation is what makes the Chapter 7 balance tunable.

## 10.2 Source power

Higher source power raises both ion and radical fluxes, and increases dissociation, shifting the radical mix. Its main effect on the saddle fin is indirect, through the neutral-to-ion ratio at the top.

## 10.3 Bias power and voltage

Bias raises ion energy, which helps the ion-limited oxide etch more than the neutral-limited silicon etch, and narrows the ion angular distribution. Both push the oxide ahead: more bias, taller fin. Bias also raises sputtering of the mask and sidewall damage, so it is limited.

## 10.4 Pressure

Lower pressure narrows the ion angular distribution and lowers radical density. In the model, narrowing σ from 4° to 2° keeps more ions on the floor, accelerating the oxide; lower radical density slows silicon. Lower pressure therefore tends to taller fins, at the cost of rate.

## 10.5 Pulsing

**Pulsed** source or bias power separates the plasma into on and off phases. During the off phase electrons cool, the sheath collapses, and negative ions and electrons can reach deeper into the trench, partly neutralising charge. Synchronised pulsing of source and bias adds a further degree of freedom: radicals can be produced in one phase and ions delivered in another, which lets the neutral-to-ion ratio at the floor be set nearly independently of geometry.

## 10.6 Wafer temperature

Sidewall passivation and by-product volatility depend on wafer temperature. Lower temperature favours deposition and taper; higher temperature favours cleaner, more vertical walls and higher sticking for some radicals. Electrostatic-chuck zones let the temperature be adjusted radially to cancel centre-to-edge variation in depth and fin height.

## 10.7 A knob map

| Knob up | Si rate (deep) | Oxide rate (deep) | Fin height | Risk |
|---|---|---|---|---|
| Source power | ↑ | ↑ | ~ | dissociation shift |
| Bias | ~ | ↑↑ | ↑ | damage, mask loss |
| Pressure | ↑ (radicals) | ↓ (σ wider) | ↓ | bowing |
| O₂ fraction | ↓ | ~ | ↑ | taper |
| Wafer temperature | ↑ | ~ | ↓ | rough walls |

The arrows are qualitative and refer to the regime of Chapter 7.
