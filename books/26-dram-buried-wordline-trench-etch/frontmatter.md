# DRAM Buried Word-Line Trench Etch

### Transport, Selectivity and Integration of the Trench That Holds the Access Transistor

*Book 26 · dram-buried-wordline-trench-etch series*

---

## Preface

Every modern DRAM cell is switched by a transistor that has been pushed underground. The gate of that transistor, the **buried word line**, sits in a narrow trench cut across silicon and isolation oxide alike, and the shape of that trench decides the cell's on-current, its leakage, and therefore its retention time. Few etches in the fab are so short and so consequential.

This book is organised in four parts and sixteen chapters, with seven appendices, a glossary and an index.

**Part I — Foundations** (Chapters 1–4): the cell, the process flow, plasma basics, and a computed treatment of neutral transport in a trench.

**Part II — Trench Etch Physics** (Chapters 5–8): ion delivery and charging, chemistry, the silicon-versus-oxide race that forms the saddle fin, and profile control.

**Part III — Process Integration** (Chapters 9–12): hard mask and patterning, reactor knobs, the bottom and the fin, and the gate stack and recess that follow.

**Part IV — Measurement, Control and Outlook** (Chapters 13–16): metrology, modelling, yield and reliability, and the road ahead.

### How the numbers were made

Transport numbers in Chapters 4–5 and Appendix B, and the depth histories in Chapter 7, come from a Monte Carlo simulation and rate model (`sim/trench_mc.py`). The neutral transport code is checked against the exact line-of-sight result for a fully absorbing trench. Everything else quantitative (process windows, dimensions, chemistries) is *illustrative*, chosen to show orders of magnitude and relationships; none of it describes a specific manufacturer's process. References are listed in Appendix G; readers should check citation details against the originals.
