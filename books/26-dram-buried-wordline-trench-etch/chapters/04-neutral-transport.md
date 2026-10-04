# Chapter 4 — Neutral Transport in a Trench

## 4.1 Free-molecular conditions

At the pressures used for trench etch (a few to tens of millitorr), the mean free path of a neutral is millimetres to centimetres, while the trench is 20 nm wide. The **Knudsen number** is enormous, so molecules inside the trench never collide with each other — only with the walls. This is **free-molecular** (Knudsen) flow, and transport becomes a geometry problem.

## 4.2 The model

The simulation in `sim/trench_mc.py` treats the trench as infinitely long (the word line is many microns long against a 20 nm width), with walls at x = 0 and x = 1 in units of the width and the floor at depth AR. Each molecule:

1. enters the top with a uniform position and a cosine angular distribution;
2. flies straight to the next surface;
3. at a wall, is lost with probability s (the **sticking coefficient**, standing for any reaction or recombination that removes it) or re-emitted diffusely with a cosine distribution;
4. is counted if it reaches the floor, and lost if it flies back out of the top.

Three hundred thousand molecules are traced for each aspect ratio and sticking coefficient.

## 4.3 Validation

When s = 1 every wall hit is fatal, so only molecules with a direct line of sight to the floor arrive. For a two-dimensional slot this fraction is known exactly from Hottel's crossed-strings rule: W = √(1 + AR²) − AR. The simulation reproduces it to within the Monte Carlo noise (about ±0.001) at every aspect ratio:

{{TABLE:valid}}

## 4.4 Results

The floor fraction for five sticking coefficients is:

{{TABLE:neutral}}

{{FIG:neutral}}

Three features stand out.

- **Even a perfectly unreactive gas is throttled.** With s = 0 only 27 % of the entering flux reaches the floor at AR = 8; the rest diffuses back out.
- **Reactivity makes it much worse.** At s = 0.05, a modest value for Br or Cl on a passivated wall, the fraction at AR = 8 falls to 18 % and at AR = 10 to 13 %.
- **The 2-D trench is kinder than a hole.** Because molecules can travel freely along the trench, a trench passes more flux than a round hole of the same width and depth, and the advantage grows with aspect ratio (Book 24 of this series computes the slot-versus-hole comparison). Word-line trenches benefit from this; the storage-node contact holes that come later do not.

## 4.5 What this means for silicon

Silicon etch in halogen chemistry is neutral-limited. Its rate therefore follows these curves closely, and ARDE in silicon is dominated by neutral starvation. Chapter 7 turns these numbers into etch-rate histories.
