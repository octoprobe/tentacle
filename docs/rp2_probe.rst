Design of RP2 Probe
=========================

The CPU `RP2 Probe` may be used to probe the DUT.
Depending on the use case, one of the following firmwares may be used:

* debugprobe: debugprobe_on_pico.uf2/board_pico_config.h
* yapicoprobe: https://github.com/rgrr/yapicoprobe
* pico-coder: https://github.com/pico-coder
  * Digital channels are PICO board pins GP2-GP22 and are named accordingly in sigrok. Channels must be enabled (via Pulseview or sigrokcli) starting at D2 and continuously set towards D22
  * A0: GP26, A1: GP27, A2: GP28
* ula: https://github.com/dotcypress/ula
* Logicanalyzer: https://github.com/gusmanb/logicanalyzer
  
.. list-table:: Assignment of the firmware features to the solder pads
   :width: 50%
   :header-rows: 1

   * - GPIO\_PROBE\_
     - debugprobe
     - yapicoprobe
     - ula
       channel
       (ch1-..)
     - pico-coder (D2-D22)
     - logicanalyzer
       channel
       (ch1-..)
   * - 0
     - ✗
     - ✗
     - ch 1
     - ✗
     - ✗
   * - 1
     - ✗
     - swd dir
     - ch 2
     - ✗
     - ✗
   * - 2
     - swd clk
     - swd clk
     - ch 3
     - D2
     - ch 1
   * - 3
     - swd dio
     - swd dio
     - ch 4
     - D3
     - ch 2
   * - 4
     - uart tx
     - uart tx
     - ch 5
     - D4
     - ch 3
   * - 5
     - uart rx
     - uart rx
     - ch 6
     - D5
     - ch 4
   * - 6
     - ✗
     - swd reset
     - ch 7
     - D6
     - ch 5
   * - 7-9
     - ✗
     - ✗
     - ch 8
     - D7-9
     - ch 6-8
   * - 10-17
     - ✗
     - digital 1-8
     - ch 11-16
     - D10-17
     - ch 9-16
   * - 18-20
     - ✗
     - ✗
     - ✗
     - D18-20
     - ch 17-19
   * - 21,22
     - ✗
     - ✗
     - ✗
     - D21,22
     - ch 20,21
   * - 26-28
     - ✗
     - analog 1-3
     - ✗
     - analog 1-3
     - ch 22-24

Notes
^^^^^^^

* GPIO 21,22 have no pads. Rationale: Limit pads to #24.
* Other firmware which might be used:

  * Bluetag: https://github.com/Aodrulez/blueTag
  * Micropython


Level shifter
----------------

Bereits verdrahtet:

* uart RX: DUT -> Probe
* uart TX: Probe -> DUT
* swd CLK: Probe -> DUT
* swd DIO: Probe <-> DUT

logicanalyzer
* 4 channel DUT