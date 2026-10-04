# Chapter 1 — Why Bury the Word Line

## 1.1 The one-transistor, one-capacitor cell

A DRAM bit is a capacitor that holds charge and a transistor that connects it to a **bit line** when the **word line** — the transistor's gate — is raised. The capacitor leaks, so every cell must be read and rewritten many times a second; the time a cell can hold its state without refresh is its **retention time**. Almost every design decision in the array trades on-current (how quickly the capacitor charges and discharges) against off-state leakage (how long it keeps its charge).

For decades the access transistor was a planar MOSFET with a polysilicon gate on top of the silicon. As the cell shrank toward a 6F² footprint (F being the half-pitch of the tightest line), the planar gate length shrank with it, and short-channel leakage became intolerable.

## 1.2 Recessed channels, then buried gates

The first answer was to *recess* the channel: etch a short trench into the silicon under the gate so that the current path goes down, around and up. The **recess-channel array transistor (RCAT)** lengthened the effective channel without growing the cell. A refinement, the **saddle fin** (or S-RCAT), let the gate wrap the sides of the silicon under the trench as well as its floor, restoring drive current that the longer channel had cost.

The decisive step was to put the *entire* gate, including its conductor, inside the trench and cap it with dielectric. This is the **buried-channel array transistor (BCAT)**, or simply the **buried word line (BWL)**. The word line runs below the silicon surface, the bit-line contact and storage-node contact land on the surface above it, and the parasitic capacitance between word line and bit line drops sharply. Since roughly the 4x nm generation every major DRAM maker has used some form of buried word line.

## 1.3 What the trench etch has to deliver

The word-line trench is a line-and-space pattern running across the active area. Along its length it crosses silicon active regions and **shallow-trench-isolation (STI)** oxide alternately. A single etch step must therefore cut two materials at once and leave them at *different* depths on purpose:

- in the **active** silicon, the floor sets the channel's lower boundary; its depth and roundness set the effective gate length and threshold voltage;
- in the **STI** oxide, the floor is deliberately deeper, so that the silicon between neighbouring trenches stands up as a fin that the gate metal wraps — the saddle fin;
- the sidewalls must be near vertical and smooth, because the gate oxide grown or deposited on them *is* the transistor's gate dielectric.

Too little fin and the cell is weak; too much and the word line couples to the neighbouring cell's channel (**passing-gate** or row-hammer effects, Chapter 15). A difference of a few nanometres matters.

## 1.4 Why this etch is hard

Three themes run through the book:

1. **Two materials, one plasma.** Silicon and oxide respond to different parts of the plasma. Chapter 7 shows with a computed model how this makes the oxide *overtake* the silicon as the trench deepens, which is precisely how the saddle fin forms.
2. **Aspect ratio at small width.** Trenches 15–25 nm wide and 120–200 nm deep give aspect ratios of 6–12, enough for transport limits (Chapters 4–5) to set the rate.
3. **Everything that follows depends on it.** Gate oxidation, TiN/W fill, metal recess and capping all inherit the trench's shape (Chapter 12).

> **A note on numbers.** Process values quoted in this book are *representative and illustrative*. The transport and depth-history numbers in Chapters 4, 5 and 7 and Appendix B are computed by `sim/trench_mc.py` and can be reproduced exactly.
