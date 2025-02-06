# Plugins used

* https://github.com/bennymeg/JLC-Plugin-for-KiCad

  JLC PCB Plug-in for KiCad

  Fill Symbol Field `JLC Part`

* https://github.com/MitjaNemec/ReplicateLayout

## Protype Baord

### Precondition

On schematics:
 * BP101: Gnd

On pcb:
 * Set GND point: Array 26x20
 * `Selection Filter`: Only check `Pads`
 * Select all pads which are NOT GND
 * `Properties -> Basic Properties -> Net: <empty>`

## Hierarchical sheet

* https://forum.kicad.info/t/variables-in-hierarchical-sheet-labels/41978

In pcb, place all relais footprints (silkscreen) correctly.

Select first pcb, `Tools -> External Plugins -> Replicate Layout`

## Production

### In schematics

Menu `Inspect -> Electrical Rule Chacker`, button `Run ERC`, No violatons

### Increment version number

Update in all sheets

### In pcb - final check and final commit

Menu `Tools -> Update PCB from Schematic`, only one error `Error: Multiple footprings found for 'PB101'`

Menu `Tools -> Cleanup Tracks & Vias`, select all,  `Build Changes`, No violatons

Menu `Inspect -> Design Rules Chacker`, check `Refill all zones`, button `Run DRC . No errors, no warnings.

Delete all files in directory `production`.

Icon `Fabricaton Toolkit`, Options empty, check `Apply automatic translatons`, UNcheck `Exluce DNP components`.

Rename production folder and add version number

### Print schematics

Schematics, Menu `File -> Print`, check 'Print drawing sheet - Color`, `Print`, `All Paages`, `Print to File`.

Move `~/Documents/output.pdf` to `hardware/octoprobe_kicad_v0.1/production_v1.0/schematics.pdf`

### Upload to JLCPCB

Accept these warnings:
```
The below parts won't be assembled due to data missing.
J202,J203,J204,J103,J104,J101,J102,J105 designators don't exist in the BOM file.
```

```
BOM does not match.
```

Manual correction
 * USB Connectors: Manual postition
 * Various chips: rotate

