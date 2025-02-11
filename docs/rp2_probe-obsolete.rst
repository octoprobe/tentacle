Design of RP2 Probe (Obsolete)
===============================

* picoprobe: debugprobe_on_pico.uf2/board_pico_config.h
* yapicoprobe: https://github.com/rgrr/yapicoprobe
* sigrok: https://github.com/pico-coder
* ula: https://github.com/dotcypress/ula
* Logicanalyzer: https://github.com/gusmanb/logicanalyzer
* Bluetag: https://github.com/Aodrulez/blueTag
  
.. list-table:: Pads
   :width: 50%
   :header-rows: 1

   * - GPIO
     - LABEL
     - picoprobe
     - yapicoprobe
     - sigrok
     - ula
     - logicanalyzer
   * - 2
     - swd clk
     - ✓
     - ✓
     - ✗
     - ✗
     - ✗
   * - 3
     - swd dio
     - ✓
     - ✓
     - ✗
     - ✗
     - ✗
   * - 6
     - swd reset
     - ✗
     - ✓
     - ✗
     - ✗
     - ✗
   * - 1
     - swd dir
     - ✗
     - ✓
     - ✗
     - ✗
     - ✗
   * - 4
     - uart tx
     - ✓
     - ✓
     - ✗
     - ✗
     - ✗
   * - 5
     - uart rx
     - ✓
     - ✓
     - ✗
     - ✗
     - ✗
   * - 26-28
     - Analog 1-3
     - ✗
     - ✓
     - ✓ (to be verified)
     - ✗
     - ✗
   * - 10-17
     - Digital 1-8
     - ✗
     - ✓
     - ✓ (to be verified. channel numbers?)
     - ✓ only channel 11,12,13,14,15,16
     - ✓ channel 8,9,10,11,12,13,14,15
   * - 25
     - LED green
     - ✓
     - ✓
     - ✓ (to be verified)
     - ✓
     - ✗
