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

Update in all sheets (`*.kicad_*`)

`(date "2025-09-02")`

`(rev "0.5")`

### In pcb - final check and final commit

Menu `Tools -> Cleanup Tracks & Vias`, select all,  `Build Changes`, No violatons

Menu `Inspect -> Design Rules Checker`, check `Refill all zones`, button `Run DRC . No errors, no warnings.

Delete all files in directory `production`.

Icon `Fabricaton Toolkit`, Options empty, check `Apply automatic translatons`, check `Exluce DNP components`.

Rename production folder and add version number

### Print schematics

Schematics, Menu `File -> Print`, check 'Print drawing sheet - Color`, `Print`, `All Pages`, `Print to File`.

Move `~/Documents/output.pdf` to `hardware/octoprobe_kicad_v0.1/production_v0.1/schematics_tentacle_v0.1.pdf`

### Upload to JLCPCB

Tooling holes: `Added by Customer`

Accept these warnings:
```
The below parts won't be assembled due to data missing.
J1501,J1303,J202,UR701,UR601,J201,C216,J501,UR901,UR801,UR1101,J1502,UR1201,UR1001 designators don't exist in the BOM file.
```

BOM
 * Verify that the correct values, specially C and R, have been choosen.
 * J201, ...: Do not place.

Manual correction
 * USB Connectors: Manual postition
 * Various chips: rotate

