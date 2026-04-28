# Errors on v0.7

## Power up ramp too slow

For the ESP32 C3 the power up ramp (100ms/3V3) seems to be too slow.

See also:

  * https://esp32.com/viewtopic.php?t=42468

  * https://esp32.com/viewtopic.php?t=43392

A workaround is to desolder C217/1uF.

Changes:

  * Before:   C217/1uF 0402
  * Proposal: C217/1uF 0805

  * Before:   -
  * Proposal: Removable soldering bridge in series to C217

  * Before:   -
  * Proposal: 100nF parallel to C217

  * Before:   Schematics: Goal: 3V3/100ms
  * After:    Schematics: Goal: 5V/150ms

  * Before:   -
  * Proposal: Silkscreen: 5V/150ms (5V/15ms without bridge)
