
Running Django under Debian
===========================

.. categories:: python
.. tags:: Django, Debian
.. comments::

I've long been trying to get Django_ play nicely with lighttpd_ *and* start automatically under Debian. Recently I've stumbled across a init.d script on the `Django wiki`_ which does just that.

What I've altered is the ability to auto-detect if there is a virtualenv which should be used. This is the case if there is a directory in the configured virtualenv root bath which has the same name as the Django site *and* also has a Python binary.

In other words: If you have configured ``DJANGO_SITES="myapp myapp2 myapp3"`` which are Django projects lying in the ``SITES_PATH`` directory and you have a virtualenv, say ``/usr/local/virtualenvs/myapp``, and ``ENVIRONMENT_PATH`` set up to ``/usr/local/virtualenvs``, the init.d script will use ``/usr/local/virtualenvs/myapp/bin/python`` to run the fastcgi.

Here is the init.d script in full length:

.. literalinclude:: etc-init-d-django.txt
   :language: sh

The default values are set in ``/etc/default/django``.

.. literalinclude:: etc-default-django.txt
   :language: sh

.. _Django: http://www.djangoproject.com
.. _lighttpd: http://lighttpd.net
.. _Django wiki: httpS://code.djangoproject.com/wiki/InitdScriptForDebiaN
