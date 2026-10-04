# Chapter 5 — Ion Delivery and Charging

## 5.1 Ions as nearly straight lines

Ions arrive with a narrow angular distribution and, at these energies, do not re-emit usefully after striking a wall: they deposit their energy into the sidewall film, sputter a little of it, and are neutralised. To first order, an ion reaches the floor only if its straight-line path does not hit a wall on the way down.

The simulation launches ions uniformly across the opening with an in-plane angle drawn from a Gaussian of standard deviation σ and counts those that land on the floor. Only the in-plane angle matters for an infinitely long trench; motion along the trench is free.

## 5.2 Results

{{TABLE:ion}}

{{FIG:ion}}

At AR = 8 a σ = 4° beam still delivers 57 % of its flux to the floor, while the neutrals at s = 0.05 deliver 18 %. The ion-to-neutral ratio at the floor has grown by a factor of more than three relative to the top. At AR = 15 the factor is about 4.6.

This is the most important single number in the book. As a trench deepens, its floor becomes progressively **ion-rich and neutral-starved**. Any material whose etch is neutral-limited slows down faster than any material whose etch is ion-limited.

## 5.3 Angular spread as a knob

A tighter angular distribution (σ = 2°) keeps 78 % of ions at AR = 8; a broad one (σ = 8°) only 34 %. Raising bias voltage or lowering pressure narrows the distribution. Because the trench is two-dimensional, ions lost on the way down strike the *sidewalls*, mostly in the top third of the trench. Those wall impacts drive bowing (Chapter 8) and damage the future gate-oxide surface (Chapter 12).

## 5.4 Charging

Electrons arrive nearly isotropically and are stopped by the sidewalls near the top of the trench; ions reach the floor. On insulating surfaces this separates charge: the upper sidewalls charge negative, the floor positive. In a word-line trench the silicon floor is conducting and drains charge to the substrate, but the STI oxide floor does not. Positive charge on oxide floors deflects late-arriving ions toward the adjacent silicon wall, which is one mechanism for **notching** at the foot of the saddle fin.

Charging is reduced by pulsed bias (which lets electrons reach deeper during the off phase), by lower aspect ratio at the moment of landing, and by keeping the ion energy distribution narrow. The present model does not include it; its numbers are best read as the uncharged limit.

## 5.5 Summary

- Ion delivery falls off slowly with depth; neutral delivery falls off quickly.
- The floor of a deep trench is therefore relatively ion-rich.
- Lost ions end up on the sidewalls, where they shape the profile.
