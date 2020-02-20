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
