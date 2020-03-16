---
title: "Arduino via the command line"
date: "2013-02-19"
series: ["project greenhouse"]
tags: ["arduino", "raspberry"]
---


For my `Project Greenhouse` I need to upload an Ardunio sketch from my Raspberry Pi.

    sudo apt-get install arduino-mk

Add a Makefile (following [these instructions](http://mjo.tc/atelier/2009/02/arduino-cli.html)) which will compile any file `.ino` in the same directory.

```makefile
# Arduino 0011 Makefile

ARDUINO_DIR   = /usr/share/arduino
ARDMK_DIR     = /usr
AVR_TOOLS_DIR = /usr

# BOARD_TAG
#   A tag identifying which type of Arduino you’re using. This only works
#   in version 0.6 and later.
# ARDUINO_PORT
#   The port where the Arduino can be found (only needed when uploading)
#   If this expands to several ports, the first will be used.
# ARDUINO_LIBS
#   A list of any libraries used by the sketch—we assume these are in
#   $(ARDUINO_DIR)/hardware/libraries.

BOARD_TAG    = uno
ARDUINO_PORT = /dev/ttyACM0
ARDUINO_LIBS = # Ethernet Ethernet/utility SPI

include $(ARDUINO_DIR)/Arduino.mk
```

Then a simple ::

    make
    make upload

and you're done.

Note: If you get an error saying 

    stty: -hupcl: No such file or directory
    make: *** [reset] Error 1

you need to change your `ARDUINO_PORT`.



