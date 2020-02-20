---
title: "Building Sphinx docs"
date: "2011-12-19"
---

Install ``inotify-tools``::

    sudo apt-get install inotify-tools 

and then simply watch for changes in your docs directory::

    cd docs/
    while inotifywait -r -e modify -e create -e delete .
    do 
        make clean && make html
    done

.. categories:: python
.. tags:: docs, Sphinx
.. comments::
