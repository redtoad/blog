==============================================
Exception handling: Extracting local variables
==============================================

.. categories:: python
.. tags:: exceptions

In Python it is possible to go back one `frame`_ in a traceback to extract
state information like local variables (adapted from example `found here`_).


.. code-block:: python

    def f():
        a=3
        fail_here()

    def fail_here():
        try:
            raise NotImplementedError, 'Error!'
        except Exception, e:
            import sys, traceback
            exc_type, exc_value, exc_tb = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_tb, limit=2)
            # get local variables from f()
            frame = exc_tb.tb_frame
            print frame.f_back.f_locals

    f() 

This results in

.. code-block:: pytb

    Traceback (most recent call last):
      File "<stdin>", line 3, in fail_here
    NotImplementedError: Error!
    {'a': 3}

See also:

* http://blog.toidinamai.de/python/frame-objekte
* http://code.activestate.com/recipes/52215-get-more-information-from-tracebacks/

.. _frame: http://docs.python.org/reference/datamodel.html#frame-objects
.. _found here: http://www.scribd.com/doc/35240506/Making-Python-Fast-PyPy-and-Unladen-Swallow.
