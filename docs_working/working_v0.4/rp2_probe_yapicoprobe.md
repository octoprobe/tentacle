# Yapicoprobe

* https://github.com/rgrr/yapicoprobe
* http://www.wikiservice.at/dse/wiki.cgi?HardyGriech
  ntbox@gmx.net
* https://www.linkedin.com/in/reinhard-griech-6b642295/


* Positive: Picoprobe with reset signal

  https://github.com/rgrr/yapicoprobe/blob/master/include/boards/pico.h
  #define PROBE_PIN_RESET 6

* Positive: Support for sigrok (somehow)

  https://github.com/rgrr/yapicoprobe/blob/master/doc/sigrok.adoc


* GPIO assignements
  * ![](https://raw.githubusercontent.com/rgrr/yapicoprobe/master/doc/png/board_schematic_bb.png)
  * SWD: GPIO1,4,5,6(reset)
  * UART: GPIO2,3
  * SIGROK digital: GPIO10-17
  * SIGROK analog: GPIO26,27,28

