# PicoProbe (Picoprobe and pico_2)

### Pin assignements for picoprobe hardware (not elected)

| # | CHAN_ | RP2 |
| - | - | - |
| 3 | 7-9 | GPIO9-11 |
| 9 | 15-23 | GPIO17-28 |

| # | CHAN_ | TXU0104PWR U# |
| - | - | - |
| 4 | 16-19 | U6 |
| 4 | 20-23 | U4 |

Channel = CHAN_x+1

### Pin assignements for pico_2 hardware (elected)

| # | CHAN_ | RP2 |
| - | - | - |
| 20 | 4-23 | GPIO6-24 |

| # | CHAN_ | RP2 | TXU0104PWR U# |
| - | - | - | - |
| 4 | 8-11 | GPIO10-13 | U1 |
| 4 | 12-15 | GPIO14-17 | U5 |


## DebugProbe (DebugProbe and RP2040)

### Links

* https://github.com/raspberrypi/debugprobe
* https://github.com/raspberrypi/debugprobe/blob/master/include/board_debug_probe_config.h
* https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html
* https://datasheets.raspberrypi.com/debug/raspberry-pi-debug-probe-schematics.pdf

### DebugProbe (not elected)

* positive: LEDS for SWD and UART activity
* negative: 2 expensive level shifters

| Function | Signal | RP2 |
| - | - | - |
| SWD | CLK | GPIO12 | 
| SWD | DIO | GPIO13 |
| SWD | DIO | GPIP14 |
| SWD | LED Green - PROBE_DAP_CONNECTED_LED | GPIO15 |
| SWD | LED Yellow - PROBE_DAP_RUNNING_LED | GPIO16 |
| ? | LED Red - PROBE_USB_CONNECTED_LED | GPIO02 |
| UART | TX | GPIO4 |
| UART | RX | GPIO5 |
| UART | RX | GPIO6 |
| UART | LED Green - PROBE_UART_RX_LED | GPIO7 |
| UART | LED Yellow - PROBE_UART_TX_LED | GPIO8 |

### RP2040 as Debug Probe (elected)

* positive: Less hardware, no level shifters, no LEDS

* See Figure 10 in https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf.
* See https://github.com/raspberrypi/debugprobe/blob/master/include/board_pico_config.h

| Function | Signal | RP2 |
| - | - | - |
| SWD | CLK | GPIO2 | 
| SWD | DIO | GPIO3 |
| UART | TX | GPIO4 |
| UART | RX | GPIO5 |
| USB Connected | LED Green | GPIO25 |


### JLC

* 74AUP1T17GW, JLC C545951, USD0.24, TSSOP-5-1.3mm
* W25Q16JVUXIQ, JLC C2843335, USD0.4, 16 MBit
* SM03B-SRSS-TB, JLC C160403, USD0.1
