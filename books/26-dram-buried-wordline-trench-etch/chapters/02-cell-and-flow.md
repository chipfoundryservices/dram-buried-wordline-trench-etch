# Chapter 2 — The Cell and the Process Flow

## 2.1 Layout of a 6F² array

In a 6F² layout the active regions are short silicon bars, tilted relative to the word lines, each carrying two transistors that share one bit-line contact in the middle and have a storage-node contact at each end. Two word lines cross each active bar; a third, the **passing word line**, crosses the STI between bars. Bit lines run perpendicular to the word lines on top.

The word-line trench therefore sees, along its length, an alternating sequence: silicon (an active bar), oxide (the STI between bars), silicon, oxide. The pitch is twice F; at F = 15 nm the trenches are around 15–20 nm wide on a 30–40 nm pitch.

## 2.2 Where the etch sits in the flow

A representative buried-word-line module runs:

1. **STI formation** — isolation trenches etched, lined and filled with oxide, planarised.
2. **Hard-mask stack** — oxide or nitride pad, amorphous carbon, and a silicon oxynitride or spin-on cap.
3. **Patterning** — lithography (often with self-aligned double or quadruple patterning) and mask open.
4. **Word-line trench etch** — the subject of this book; one or more steps that cut silicon and STI oxide.
5. **Clean and gate oxidation** — removal of residue and damage; growth (often radical oxidation) of the gate dielectric.
6. **Gate conductor** — a TiN liner and tungsten fill, or increasingly a dual work-function stack with a doped-polysilicon or low-work-function upper layer.
7. **Metal recess** — etch-back of TiN and W to a controlled depth below the silicon surface.
8. **Cap** — silicon nitride fill and planarisation.

Bit-line contacts, bit lines, storage-node contacts and capacitors follow on top.

## 2.3 Dimensions that matter

The important numbers are relative, so we normalise everything by the trench width w:

| Quantity | Illustrative value | Normalised |
|---|---|---|
| Trench width w | 20 nm | 1 |
| Silicon floor depth | 130–150 nm | 6.5–7.5 |
| STI floor depth | 150–175 nm | 7.5–8.8 |
| Saddle-fin height | 10–30 nm | 0.5–1.5 |
| Word-line metal top below Si surface | 40–60 nm | 2–3 |

The aspect ratio of the trench, depth over width, is therefore around 7–9 at the end of etch. Chapter 4 shows why that range is already firmly in the transport-limited regime.

## 2.4 Materials the plasma sees

- **Crystalline silicon** in active areas, usually doped; doping affects etch rate modestly in halogen plasmas.
- **STI oxide**, often a flowable or high-density-plasma oxide, sometimes with a thermal liner and a nitride liner at the silicon interface. The nitride liner is a notorious source of **divots** (Chapter 11).
- **Hard mask** (amorphous carbon, oxide or nitride) at the top.
- **Redeposited by-products** (SiBr_x, SiCl_x, SiO_xBr_y) on the sidewalls, which are both a nuisance and the main profile control lever.
