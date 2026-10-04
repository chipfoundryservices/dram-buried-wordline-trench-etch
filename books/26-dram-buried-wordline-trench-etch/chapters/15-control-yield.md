# Chapter 15 — Process Control, Yield and Reliability

## 15.1 Run-to-run control

Etch time is adjusted lot to lot from post-etch depth metrology and incoming CD. Because fin height grows faster than silicon depth late in the etch (Chapter 7), a controller that holds silicon depth will let fin height drift with CD; a controller that holds fin height will let depth drift. Most fabs control on a combination, weighted by electrical sensitivity.

## 15.2 Within-wafer uniformity

Centre-to-edge variation in plasma density, wafer temperature and incoming CD produce radial patterns in depth and fin height. Multi-zone gas injection and electrostatic-chuck temperature zones are the main correction tools. Edge rings erode over their life and shift the edge profile, so ring wear is tracked as a control variable.

## 15.3 Chamber drift

Wall deposits accumulate over a maintenance cycle, changing radical densities and therefore the neutral-limited silicon rate more than the ion-limited oxide rate. The fin height drifts upward as the chamber ages. Seasoning wafers after each clean and periodic in-situ cleans limit the drift.

## 15.4 Yield mechanisms

| Defect | Electrical signature |
|---|---|
| Fin too short | low on-current, write failures |
| Fin too tall | passing-gate coupling, retention loss |
| Silicon too deep | high V_t, slow cells |
| Divot | leakage, V_t tails |
| Residue on floor | open or high-resistance word line |
| Bowing | voids in fill, word-line resistance |

## 15.5 Retention and GIDL

Retention failures are dominated by the leakiest cells. Gate-induced drain leakage at the junction where the word-line metal overlaps the storage-node diffusion is set by the metal recess depth (Chapter 12), but its tail is set by trench-wall damage and roughness from the etch.

## 15.6 Row hammer

Repeatedly activating one word line disturbs cells on adjacent rows. The passing word line beside an active area couples to the storage-node junction of the neighbour; a deeper oxide floor (taller fin) increases that coupling. Row-hammer sensitivity therefore puts an upper limit on fin height that is independent of the drive-current argument for a taller fin.
