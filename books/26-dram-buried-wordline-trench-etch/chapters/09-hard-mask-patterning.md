# Chapter 9 — Hard Mask and Patterning

## 9.1 Why a hard mask

Photoresist thin enough to resolve a 20 nm line cannot survive a 150 nm silicon etch. The pattern is therefore transferred first into a **hard mask** — typically amorphous carbon (a-C) under a silicon oxynitride or oxide cap, sometimes over a thin oxide or nitride pad — and the trench is etched through the hard mask.

## 9.2 Multiple patterning

At word-line pitches below about 40 nm, single-exposure 193 nm immersion lithography cannot print the lines. **Self-aligned double patterning (SADP)** forms spacers on a mandrel and uses the spacers as the mask, halving the pitch; **self-aligned quadruple patterning (SAQP)** repeats the process. EUV lithography can print some of these layers directly. Each approach leaves its signature: SADP and SAQP produce **pitch walking**, in which alternate spaces differ slightly in width.

Pitch walking matters doubly here. A wider space is a wider trench, which etches faster at a given depth (lower AR) and, by the argument of Chapter 7, leaves a slightly shorter fin. Alternate word lines then differ systematically in threshold voltage.

## 9.3 Mask open

The cap is opened in fluorocarbon chemistry, the carbon in O₂/N₂ or O₂/COS, and the pad in fluorocarbon again. The carbon open sets the profile that the silicon etch inherits: a tapered or faceted carbon line throws ions onto the trench walls (Chapter 8).

## 9.4 Mask selectivity budget

With a carbon mask, HBr-based silicon etch has a selectivity of perhaps 10–30. A 150 nm etch then consumes 5–15 nm of carbon in open area, more on the facet. Because silicon slows down with depth (Chapter 7) while mask erosion does not, the *effective* selectivity over the whole etch is lower than the open-area value — by a factor of more than two in the model of Chapter 7, where silicon averages 0.43 R₀ over a 15 t₀ etch.

## 9.5 CD control

The final trench CD is set by the mask CD plus any bias introduced by the etch. Bias comes from mask erosion (positive), passivation build-up (negative) and taper. A typical target is zero bias at the top and a controlled taper below.

## 9.6 Array edge

At the edge of the array the pattern density changes abruptly. Neutral and by-product loading change, and the first few word lines are often dummies. Their trenches etch differently, and the transition is a common place for fin-height and depth excursions.
