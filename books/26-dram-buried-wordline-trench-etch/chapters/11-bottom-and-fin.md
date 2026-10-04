# Chapter 11 — The Floor, the Fin and the Liner

## 11.1 Depth targeting without endpoint

The silicon floor does not stop on anything. Depth is set by time, and is controlled run to run from metrology (Chapter 13). Because silicon slows to a quarter of its open-area rate by the end of etch (Chapter 7), time error translates only weakly into depth error — a useful self-limiting effect.

## 11.2 The nitride liner and divots

STI trenches are often lined with a thin silicon nitride between the thermal oxide liner and the oxide fill. In the word-line trench the liner appears as a thin vertical sheet between silicon and oxide. If the chemistry etches nitride more slowly than both, a **nitride fence** remains; if faster, a **divot** opens. Divots fill with gate metal and create a parasitic, strongly coupled gate at the edge of the active area. They are among the most damaging defects in this module.

## 11.3 Fin height targeting

Fin height is the difference of two drifting quantities. The sensitivities from Chapter 7 — fin height grows by roughly 2 nm per t₀ late in the etch, and depends on trench width — mean that fin-height control needs both a stable etch time and a stable CD. Two practical schemes:

- **One-step**: rely on the transport mechanism of Chapter 7, tuning bias and O₂ to set the offset.
- **Two-step**: etch silicon and oxide together to target silicon depth, then deepen the oxide with a selective fluorocarbon step. This decouples the two depths at the cost of an extra step and more charging risk.

## 11.4 Floor rounding

A rounded silicon floor reduces field crowding and helps the gate oxide grow uniformly. Rounding steps (low-bias, fluorine-containing) also remove the most damaged surface layer. They must not be so isotropic that they widen the trench or undercut the fin.

## 11.5 Microloading along the trench

The silicon segments of a word-line trench are short (one active area) and alternate with oxide. By-products from silicon etch, mostly SiBr_x, travel along the trench and redeposit on adjacent oxide segments, and vice versa. The result is that floor depths near silicon–oxide transitions differ from those in the middle of each segment, giving the fin its characteristic sloped shoulders.

## 11.6 Passing word lines

The word line that passes over the STI between two active areas sits beside the end of an active bar. Its oxide floor is deep; the silicon wall it faces is the side of the neighbouring cell's storage-node junction. Too deep an oxide etch brings the passing word line too close to that junction, raising leakage and row-hammer sensitivity (Chapter 15).
