# Chapter 12 — Gate Stack, Metal Recess and Cap

## 12.1 Cleaning the trench

After etch, the trench walls carry SiO_xBr_y passivation, implanted halogen and a damaged silicon layer a few nanometres thick. A sequence of dilute HF and SC1-type cleans, sometimes preceded by a sacrificial oxidation, removes them. Each clean also widens the trench and deepens the oxide floor slightly; that consumption must be included in the etch targets.

## 12.2 Gate oxidation

The gate dielectric is grown on the trench walls, typically by **radical (in-situ steam) oxidation**, which oxidises (100) and (110) surfaces and the rounded floor at similar rates. Its thickness is around 4–6 nm. Any roughness, residual halogen or crystal damage from the etch shows up as thinning, interface traps or early breakdown.

## 12.3 Conductor

A thin TiN liner (barrier and work-function setter) and tungsten fill are deposited by CVD or ALD. Tungsten has the lowest resistivity achievable in a 20 nm trench, but it fills by growth from the walls and can leave a seam. Newer stacks use a **dual work-function** design: a high-work-function metal low in the trench near the channel, and a low-work-function layer (for example doped polysilicon) higher up, adjacent to the drain junctions, to reduce gate-induced drain leakage (**GIDL**).

## 12.4 Metal recess

The conductor is etched back to 40–60 nm below the silicon surface. This **recess etch** must be uniform across the wafer and along the line: too shallow and the gate overlaps the storage-node junction, raising GIDL; too deep and the channel is not fully gated at the top, raising resistance. Recess etch is plasma (SF₆/Cl₂-based for W, Cl₂-based for TiN) or wet, and is a subject in its own right.

## 12.5 Cap

A silicon nitride cap fills the trench above the recessed metal and is planarised. It insulates the word line from the bit-line and storage-node contacts that will land on the silicon surface beside it.

## 12.6 What the etch passes forward

| Etch feature | Downstream effect |
|---|---|
| Trench CD | metal volume → word-line resistance |
| Taper | fill seams and voids |
| Silicon depth | effective channel length, V_t |
| Fin height | drive current, passing-gate coupling |
| Floor roundness | gate-oxide integrity |
| Divot | parasitic gate, leakage |
| Sidewall roughness and damage | mobility, interface traps |
