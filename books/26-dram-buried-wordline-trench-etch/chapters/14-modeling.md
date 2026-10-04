# Chapter 14 — Modelling the Trench Etch

## 14.1 Levels of model

- **Reactor models** compute plasma density, radical composition and ion energy–angle distributions from tool settings.
- **Feature-scale models** take those fluxes and compute how a feature's profile evolves.
- **Compact models** reduce either to a few fitted parameters for process control.

The model of Chapters 4–7 is a feature-scale model of the simplest useful kind: Monte Carlo transport plus a two-term surface rate law, with the profile reduced to a single depth.

## 14.2 Monte Carlo transport

Monte Carlo is the natural method for free-molecular transport: trace many molecules, apply the surface rules, count. It handles arbitrary geometries and surface rules without approximation; its cost is noise, which falls as one over the square root of the number of particles. With 300,000 particles the floor fractions in Appendix B carry a standard error below 0.001. Appendix A details the algorithm.

## 14.3 Profile evolution

Full feature-scale simulators represent the surface by strings, cells or level sets and move each surface element according to its local fluxes. They predict taper, bowing and fin shoulders, which the one-dimensional depth model cannot. They need surface rate laws for each material and each species, fitted from beam experiments or blanket-wafer data.

## 14.4 Calibration

Calibration is the hard part. The two parameters per material in Chapter 7 — R₀ and ρ — can be extracted from two experiments: an open-area rate, and the rate at one known aspect ratio. Sticking coefficients come from literature or from fits to depth versus width data across a test pattern with several trench widths. Fitting more parameters than the data can constrain is the commonest failure.

## 14.5 Uses

- Explaining a sensitivity (why fin height moves with CD).
- Ranking knobs before running experiments.
- Building virtual metrology: predicting depth from chamber sensors and incoming CD.
- Transferring a recipe between chamber types with different ion angular distributions.

## 14.6 Machine-learning surrogates

Neural-network and Gaussian-process surrogates trained on simulated and measured data are increasingly used for virtual metrology and recipe search. They are most reliable when constrained by physical structure — for example, by predicting ρ and R₀ rather than depth directly.
