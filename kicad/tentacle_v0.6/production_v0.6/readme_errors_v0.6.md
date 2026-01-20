# Errors on v0.6

* D1501 is not required anymore
* R1503 0R -> 1K
* D201 is an extended part - replace by basic part
* C307/C308 is an extended part - replace by basic part


## Error: PROBEBOOT_LED does not go on

LED LED  LED
RUN BOOT ACTIVE
    inv
off off  off    op power --off proberun --on  probeboot --off led_active
on  off  on     op power --on  proberun --on  probeboot --on  led_active
off off  on     op power --off proberun --off probeboot --on  led_active
on  off  on     op power --on  proberun --off probeboot --on  led_active
    ^ short blink, then 1 V

The same with micropython code:
>>> import os
>>> import sys
>>> import time
>>> from machine import Pin, unique_id
>>> import ubinascii
>>> pin_PICO_PROBE_RUN = Pin('GPIO22', Pin.OUT) # Not connected on v0.3
>>> pin_PICO_PROBE_BOOT = Pin('GPIO21', Pin.OUT, value=1) # Not connected on v0.3
>>> pin_PICO_PROBE_BOOT.value(1); pin_PICO_PROBE_RUN.value(1) # app mode
>>> pin_PICO_PROBE_BOOT.value(1); pin_PICO_PROBE_RUN.value(0) # Off
>>> pin_PICO_PROBE_BOOT.value(0); pin_PICO_PROBE_RUN.value(1) # programming mode
>>> pin_PICO_PROBE_BOOT.value(1); pin_PICO_PROBE_RUN.value(0) # Off
>>> pin_PICO_PROBE_RUN.value(1); time.sleep(0.5); pin_PICO_PROBE_BOOT.value(0) # programming mode - DOES NOT WORK
>>> pin_PICO_PROBE_BOOT.value(1); pin_PICO_PROBE_RUN.value(0) # Off
>>> pin_PICO_PROBE_RUN.value(1); time.sleep(0.5); pin_PICO_PROBE_BOOT.value(0) # programming mode - DOES NOT WORK

**Problem identified**

When PICO_PROBE is running and now QSPI_SS is pulled down: WSPI_SS will power back so that RP2_PROBE_BOOT will only go to 1V, but should go to 0V.

Replacing R1503 0R with 1K will eliminate the problem.


## USB Hub

The tentacle is Bus-Powered.

Datasheet https://ww1.microchip.com/downloads/en/DeviceDoc/00001692C.pdf states that CFG_SEL[1] should be 1 for "Bus-powerered operation". However the current version is 0.

## LEDs

Compare LED_GREEN and LED_RED. Verify wether there physical size is correct.
