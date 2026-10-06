# USBHUB-Power (on/off) vs Ramp

## History

* tentacle <= v0.4: Uses on/off
* tentacle >= v0.5: Uses ramp chip
* tentacle >= v0.9: Uses on/off

## Comparison

Electronics
* on/off: ✅ Simpler schematic, less components
* ramp: power ramp

Control
* on/off: USB
* ramp: pico

USB
* on/off: As USB standard
* ramp: ⛔ need MUX for D+/D-

USB load
* on/off: ⛔ Additional load for USB stack
* ramp: Less load for USB stack

Poweron
* on/off: ⛔ Linux switches DUT on when connected
* ramp: DUT is off by default

Poweron fix in electronics
* on/off: ⛔ possible phantom powering of the DUT

Poweron fix in kernel
* on/off: ⛔ tricky kernel coding


https://jlcpcb.com/partdetail/GuangdongHottech-1N5819WS/C191023

