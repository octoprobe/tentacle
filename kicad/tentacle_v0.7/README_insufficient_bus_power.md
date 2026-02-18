# Bug on the first 10 tentacles v0.7

## Output when connecting tentacle v0.7

```bash
su dmesg --follow
[126648.334788] usb 3-7: new high-speed USB device number 21 using xhci_hcd
[126648.457906] usb 3-7: New USB device found, idVendor=0424, idProduct=2514, bcdDevice= b.b3
[126648.457912] usb 3-7: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[126648.459557] hub 3-7:1.0: USB hub found
[126648.459606] hub 3-7:1.0: 4 ports detected
[126649.333743] usb 3-7.1: new full-speed USB device number 22 using xhci_hcd
[126649.420136] usb 3-7.1: New USB device found, idVendor=2e8a, idProduct=0003, bcdDevice= 1.00
[126649.420142] usb 3-7.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[126649.420143] usb 3-7.1: Product: RP2 Boot
[126649.420144] usb 3-7.1: Manufacturer: Raspberry Pi
[126649.420146] usb 3-7.1: SerialNumber: E0C9125B0D9B
[126649.420251] usb 3-7.1: rejected 1 configuration due to insufficient available bus power
[126649.420253] usb 3-7.1: no configuration chosen from 1 choice
```

lsusb -d 0424:2514 -v
  Bus 003 Device 081: ID 0424:2514 Microchip Technology, Inc. (formerly SMSC) USB 2.0 Hub
  MaxPower 100mA

lsusb -d 2e8a:0003 -v
  Bus 003 Device 082: ID 2e8a:0003 Raspberry Pi RP2 Boot
  MaxPower 500mA

lsusb -d 2e8a:0005 -v
  Bus 003 Device 084: ID 2e8a:0005 MicroPython Board in FS mode
  MaxPower 250mA

## Rationale why `insufficient available bus power`

The hub registers itself with 100mA, however the pico_infra with 500mA.

The ubuntu kernel realizes this conflict and does not power pico_infra.

Solution: Configure the hub to be self powered (which is wrong)
