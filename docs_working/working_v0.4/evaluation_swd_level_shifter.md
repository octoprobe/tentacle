## Links

* https://yeah.nah.nz/electronics/jtag-level-shifter/

  Using some LSF0204D bidirectional level translators, I built some full JTAG level shifters

### Chat GPT

Q: I need a voltage level shifter for a picoprobe running swd.

```text
For a picoprobe running SWD (Serial Wire Debug), you often need a voltage level shifter to safely translate signal levels between the debugger (like the Raspberry Pi Pico) and the target device. Here's what you should consider:

### Requirements for a Level Shifter in SWD:
1. **Voltage Range**: Ensure it supports the voltage levels of both the target device and the picoprobe (typically 1.8V to 5V).
2. **Speed**: SWD signals can operate at high frequencies, so the level shifter should support fast signal transitions (at least 10 MHz is typical for SWD).
3. **Directionality**: SWD primarily requires bidirectional level shifting for the **SWDIO** line and unidirectional for **SWCLK**.
4. **Low Propagation Delay**: For reliable debugging, the level shifter must introduce minimal delay.

### Recommended Solutions:
1. **Dedicated Level Shifter ICs**:
   - **TXS0102 or TXS0104**: These are great for bidirectional level shifting and are fast enough for SWD.
   - **SN74LVC2T45**: A small, high-speed bidirectional level shifter that works well for single-line bidirectional communication like SWDIO.
   - **PCA9306**: Although often used for I2C, it works well for bidirectional lines if the speed isn't extreme.

2. **MOSFET-Based Level Shifter**:
   - A simple and cost-effective solution for low-speed or moderately high-speed applications. Use a BSS138 MOSFET or similar with pull-up resistors on both sides. This is a DIY option and might struggle at very high SWD speeds.

3. **Custom Circuit with Voltage Dividers and Buffers**:
   - For **SWCLK** (unidirectional), you can use a simple resistor divider.
   - For **SWDIO** (bidirectional), use a buffer IC like a 74LVC1T45, which can handle level shifting with direction control.

4. **Pre-Made Modules**:
   - Modules like the **SparkFun Bi-Directional Logic Level Converter** are ready-made solutions that work well for prototyping.

### Example Circuit for SWD:
- **SWCLK**: Use a voltage divider or unidirectional level shifter (e.g., 74LVC1G17).
- **SWDIO**: Use a bidirectional level shifter (e.g., TXS0102).

### Additional Notes:
- If your target device operates at 3.3V and the picoprobe also operates at 3.3V, you may not need a level shifter at all.
- Ensure pull-up resistors are properly configured on the SWDIO and SWCLK lines if required by your setup.

Let me know if you'd like a specific schematic or further advice!
```

Q: swd level converter using swd_dir

```text
Here’s a detailed explanation of how you can set up an **SWD level converter** using the **SWD_DIR** signal for controlling direction. I'll describe the schematic design based on common components (like BSS138 MOSFETs) and explain the connections.

---

### Components Required
1. **N-channel MOSFETs** (e.g., BSS138) - 2 for bidirectional level shifting.
2. **Resistors**:
   - Pull-up resistors (10kΩ) for SWD_CLK, SWD_IO, and SWD_DIR.
3. **Voltage Sources**:
   - Debugger voltage level (VDD_H, e.g., 3.3V).
   - Target device voltage level (VDD_L, e.g., 1.8V).
4. **Direction Control Logic**:
   - Use SWD_DIR to control the bidirectional flow of SWD_IO.

---

### Schematic Design
#### 1. **SWD_CLK (Unidirectional)**
- A simple voltage-divider or level-shifter IC is sufficient for SWD_CLK since it's unidirectional.
- **Connections**:
  - Debugger’s SWD_CLK → Resistor divider (or level-shifter IC) → Target device's SWD_CLK.

---

#### 2. **SWD_IO (Bidirectional)**
- Use a MOSFET-based bidirectional level shifter.
- **Connections**:
  - Debugger's SWD_IO connects to the **Source** of MOSFET #1.
  - Target device's SWD_IO connects to the **Drain** of MOSFET #1.
  - A pull-up resistor (10kΩ) connects to the VDD_H on the debugger side.
  - Another pull-up resistor (10kΩ) connects to the VDD_L on the target side.
  - The **Gate** of MOSFET #1 is tied to VDD_L (target voltage).
  - SWD_DIR connects to the control logic for selecting communication flow.

---

#### 3. **SWD_DIR Control**
- Add a direction control circuit (e.g., using a buffer or an AND/OR gate) to interpret SWD_DIR signals.
- **Logic**:
  - When SWD_DIR = 1 (high), configure the level shifter to allow communication from Debugger → Target.
  - When SWD_DIR = 0 (low), configure the level shifter to allow communication from Target → Debugger.

---

Would you like me to prepare a visual schematic for this? If yes, I can create one based on this description!
```

## Ti buying guide

https://www.ti.com/lit/sg/slyy165a/slyy165a.pdf


## TXS0102

* https://www.adafruit.com/product/395
* https://www.ti.com/lit/ds/symlink/txb0108.pdf

==> VORSICHT, zu langsam

Links

* TXS0108E

## SN74LVC245APWR

JLC C7848
https://www.ti.com/lit/ds/symlink/sn74lvc245a.pdf

Links

* https://electronics.stackexchange.com/questions/673434/how-to-read-the-sn74lvc245a-datasheet

==> The 74LVC245 cannot (alone) do what you need

==> 
Fast level shifters always require two supply voltages. There are many level translators that work like the '245 transceivers; this is usually indicated by a "T" in the name, for example, SN74LXC8T245.

## SN74LXC8T245

SN74LXC8T245PWR
JLC C4363995, USD 1, TSSOP-24

Links

* https://www.ti.com/product/SN74LXC8T245
* https://www.ti.com/lit/an/spradm1/spradm1.pdf

  Schematic Checklist - A Guide to Designing With Fixed or
Direction Control Translators
  ==> 2.7 Recommended Translator by Interface

## TXB0108

* https://www.adafruit.com/product/395
* https://github.com/sparkfun/TXB0104_breakout

Links

* https://www.ti.com/product/TXB0108
* https://www.ti.com/lit/ds/symlink/txb0108.pdf
* https://www.youtube.com/watch?v=JRNbOPWspfA

JlC C53406, USD 0.25, TSSOP-20

## TXS0108

JLC C17206, USD 0.22, TSSOP-20

 * https://www.ti.com/lit/ds/symlink/txs0108e.pdf

==> Nein: Open-Drain

## STLINK-V3SET

https://www.waveshare.com/wiki/STLINK-V3SET

## SN74AXC4T774

0.65 Vto 3.6 V

JLC C1849454, USD 1, UQFN-16

Links

* https://www.ti.com/lit/an/scea065b/scea065b.pdf
* https://www.ti.com/product/de-de/SN74AXC4T

## Testing level shifting

https://micropython.org/download/PCA10059/

https://docs.nordicsemi.com/bundle/ncs-1.0.0/page/zephyr/boards/arm/nrf52840_pca10059/doc/index.html


* https://devzone.nordicsemi.com/f/nordic-q-a/110502/flashing-nrf52840-dongle-through-swd-interface
* https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dongle
* https://docs.nordicsemi.com/bundle/ncs-1.0.0/page/zephyr/boards/arm/nrf52_blenano2/doc/index.html

