Building Sphinx docs
====================

Install ``inotify-tools``::

    sudo apt-get install inotify-tools 

and then simply watch for changes in your docs directory::

    cd docs/
    while inotifywait -r -e modify -e create -e delete .
    do 
        make clean && make html
    done

.. author:: default
.. categories:: python
.. tags:: docs, Sphinx
.. comments::
