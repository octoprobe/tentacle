#

## USB Hub

### New port assignement

| | v0.3 | v.04 |
| - | - | - |
| Port 1 | RP2 Infra | RP2 Probe |
| Port 2 | RP2 Boot | RP2 Infra |
| Port 3 | DUT | DUT |
| Port 4 | LED Error | RP2 Boot |

Detection of v0.3/v0.4 boards.

* v0.3: NO device on port 2: Take serial from port 1.
* v0.4: RP2 on port 2: Take serial from port 2.

## CPU `RP2 Probe`

* Schematic based on
  * Chapter *Debug with a second Pico or Pico 2* in [getting-started-with-pico.pdf](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
  * [logicanalyzer](https://github.com/gusmanb/logicanalyzer)

Power: The `RP2 Probe` is powered from the `RP2 Boot`.
Boot mode: The `RP2 Probe` boot mode is connected to `RP2 Boot` which is port 4.

### Use as DebugProbe

* https://github.com/raspberrypi/debugprobe/releases/download/debugprobe-v2.2.1/debugprobe_on_pico.uf2
* Features: SWT and UART

### Use as logicanalyzer

* https://github.com/gusmanb/logicanalyzer/releases
* Features: 8 daq channels

### Usa as sigrok logicanalyzer

* https://github.com/pico-coder/sigrok-pico
