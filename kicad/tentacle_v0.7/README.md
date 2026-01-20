# Octoprobe Tentacle v0.5

![tentacle](production_v0.5/pcb_top_3D.png)

[schematics](production_v0.5/schematics_tentacle_v0.5.pdf)

## History v0.4 -> v0.5

* Remove silkscreen: R301, U302, R1401, R1505
* Breadbord pads: Only one ground line to leave more space for DUT-boards
* Breadbord: Enlarged for big boards
* buffering capacitor on HUB+5V
* GPIO Pads equal to Tentacle v3
* LEDS less bright (Green LEDs 2k2 -> 4k7)
* Power DUT via PICO-Infra?
  * + DUT is not powerered when Tentacle is plugged in.
* Power PICO-Probe via PICO-Infra?
  * + PICO-Probe is by default off.
  * + PICO-Probe Boot pin would be controlled by PICO-Infra.
* DUT may be powerered via a jumper
* RP2_INFRA_BOOT via USB Port 2
* RP2_PROBE_BOOT via GPIO
* RP2_PROBE_RUN via GPIO

## History v0.5 -> v0.6

 * New: Pad for scope ground
 * Labels level shifter are currently below the pins and covered by the soldered cables: They should be on top of the pins!
 * 2 level shifters
 * LED for proberun and probeboot
 * DUT was powerered 3V3, now 5V
