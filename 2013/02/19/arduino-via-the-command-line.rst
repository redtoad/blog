
Arduino via the command line
============================

.. categories:: project greenhouse
.. tags:: arduino, raspberry
.. comments::

For my `Project Greenhouse` I need to upload an Ardunio sketch from my Raspberry Pi.

::

    sudo apt-get install arduino-mk

Add a Makefile (following `these instructions`_) which will compile any file ``.ino`` in the same directory.

.. more::

.. literalinclude:: Makefile
    :language: make

Then a simple ::

    make
    make upload

and you're done.

Note: If you get an error saying ::

    stty: -hupcl: No such file or directory
    make: *** [reset] Error 1

you need to change your ``ARDUINO_PORT``.

.. _these instructions: http://mjo.tc/atelier/2009/02/arduino-cli.html


