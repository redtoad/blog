
82% test coverage! Yeah!
========================

:date: 2009-12-09
:category: python
:tags: amazon, tests, nose

I've recently started to add unittests to `python-amazon-product-api <{tag}amazon>`_. Amazon how happy a simple number can make feel!

::

    $ nosetests --with-coverage --cover-package=amazonproduct xml-responses.py
    .............
    Name            Stmts   Exec  Cover   Missing
    ---------------------------------------------
    amazonproduct     172    142    82%   43-44, 79, 180-181, 229-239, 339, 422, 451-462, 535-536, 545-546, 555-556
    ----------------------------------------------------------------------
    Ran 13 tests in 0.074s

    OK

