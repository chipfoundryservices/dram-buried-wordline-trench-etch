# Chapter 13 — Metrology

## 13.1 What must be measured

The etch defines five numbers per trench: top CD, bottom CD (or taper), silicon depth, oxide depth and fin height. None is directly visible from above, and two (silicon depth and fin height) are buried under each other.

## 13.2 Optical critical-dimension metrology

**OCD** (scatterometry) measures spectra from a periodic target and fits them with a parametric model of the trench. It is fast, non-destructive and runs inline. Its weakness is the model: silicon and oxide segments along the same trench make the structure three-dimensional, and correlated parameters (taper and depth, for instance) are hard to separate. Dedicated targets with silicon-only and oxide-only trench segments help.

## 13.3 CD-SEM

Top-down **CD-SEM** measures top CD and roughness directly and can see partially down the trench. It cannot measure depth or fin height.

## 13.4 X-ray methods

**CD-SAXS** (critical-dimension small-angle X-ray scattering) passes X-rays through the wafer and measures the full profile of periodic structures with sub-nanometre precision, including taper and depth. Throughput has improved enough for sampling in production.

## 13.5 Cross-section and TEM

Transmission electron microscopy on lamellae cut across and along the trench is the reference. It shows fin shape, divots and floor rounding unambiguously, but is slow and destructive. It calibrates the inline methods.

## 13.6 Electrical metrology

Ultimately, the trench is judged by the transistor: threshold voltage, drive current, GIDL and word-line resistance. Electrical test arrives weeks later, so it is used to set targets and to detect drift rather than for run-to-run control.

## 13.7 A measurement plan

| Parameter | Inline method | Reference |
|---|---|---|
| Top CD, LER | CD-SEM | TEM |
| Depth (Si, ox) | OCD, CD-SAXS | TEM |
| Taper, floor shape | OCD, CD-SAXS | TEM |
| Fin height | OCD (dedicated target) | TEM along trench |
| Divot | AFM after strip, defect inspection | TEM |
