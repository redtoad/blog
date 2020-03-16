---
title: "Running Django under Debian"
date: "2009-11-19"
categories: ["Python"]
tags: ["Django", "Debian"]
---

I've long been trying to get Django_ play nicely with lighttpd_ *and* start automatically under Debian. Recently I've stumbled across a init.d script on the `Django wiki`_ which does just that.

What I've altered is the ability to auto-detect if there is a virtualenv which should be used. This is the case if there is a directory in the configured virtualenv root bath which has the same name as the Django site *and* also has a Python binary.

In other words: If you have configured ``DJANGO_SITES="myapp myapp2 myapp3"`` which are Django projects lying in the ``SITES_PATH`` directory and you have a virtualenv, say ``/usr/local/virtualenvs/myapp``, and ``ENVIRONMENT_PATH`` set up to ``/usr/local/virtualenvs``, the init.d script will use ``/usr/local/virtualenvs/myapp/bin/python`` to run the fastcgi.

Here is the init.d script in full length:

```bash
#! /bin/sh
### BEGIN INIT INFO
# Provides:          FastCGI servers for Django
# Required-Start:    networking
# Required-Stop:     networking
# Default-Start:     2 3 4 5
# Default-Stop:      S 0 1 6
# Short-Description: Start FastCGI servers with Django.
# Description:       Django, in order to operate with FastCGI, must be started
#                    in a very specific way with manage.py. This must be done
#                    for each Django web server that has to run.
### END INIT INFO
#
# Author:  Guillermo Fernandez Castellanos
#          <guillermo.fernandez.castellanos AT gmail.com>.
#
# Changed: Jannis Leidel
#          <jannis AT leidel.info>
#          Joost Cassee
#          <joost@cassee.net>
#          Sebastian Rahlf
#          <basti AT redtoad.de>
#
# Version: @(#)fastcgi 0.5 19-Nov-2009 basti AT redtoad.de
#

set -e

#### CONFIGURATION (override in /etc/default/django)

# django project names/directories
DJANGO_SITES=""

# path to the directory with your django projects
SITES_PATH=/var/lib/django

# path to the directory conrtaining all site-specific virtualenvs 
# (see http://pypi.python.org/pypi/virtualenv for more information)
ENVIRONMENT_PATH=$SITES_PATH/environment

# path to the directory for socket and pid files
RUNFILES_PATH=/var/run/django

# please make sure this is NOT root
# local user prefered, www-data accepted
RUN_AS=www-data

# maximum requests before fast-cgi process respawns
# (a.k.a. get killed and let live)
MAXREQUESTS=1000

#### END CONFIGURATION

# Include defaults if available
if [ -f /etc/default/django ] ; then
    . /etc/default/django
fi

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DESC="Django FastCGI servers"
NAME=$0
SCRIPTNAME=/etc/init.d/$NAME
mkdir -p $RUNFILES_PATH
chown -R $RUN_AS:$RUN_AS $RUNFILES_PATH

# A specific site can be started/stopped by appending its name
SITE=$2
if [ -n "$SITE" ]; then
    DJANGO_SITES=$SITE
fi

#
#       Function that starts the daemon/service.
#
d_start()
{
    # Starting all Django FastCGI processes
    for SITE in $DJANGO_SITES
    do
        echo -n " $SITE"

        # find python binary to use
        if [ -f $ENVIRONMENT_PATH/$SITE/bin/python ]; then
           PYTHON=$ENVIRONMENT_PATH/$SITE/bin/python
        else
           PYTHON=`which python`
        fi

        if [ -f $RUNFILES_PATH/$SITE.pid ]; then
            echo -n " already running"
        else
            start-stop-daemon --start --quiet \
                       --pidfile $RUNFILES_PATH/$SITE.pid \
                       --chuid $RUN_AS --exec /usr/bin/env -- $PYTHON \
                       $SITES_PATH/$SITE/manage.py runfcgi \
                       protocol=fcgi method=threaded maxrequests=$MAXREQUESTS \
                       socket=$RUNFILES_PATH/$SITE.socket \
                       pidfile=$RUNFILES_PATH/$SITE.pid
            chmod 400 $RUNFILES_PATH/$SITE.pid
        fi
        sleep 1
    done
}

#
#       Function that stops the daemon/service.
#
d_stop() {
    # Killing all Django FastCGI processes running
    for SITE in $DJANGO_SITES
    do
        echo -n " $SITE"
        start-stop-daemon --stop --quiet --pidfile $RUNFILES_PATH/$SITE.pid \
                          || echo -n " not running"
        if [ -f $RUNFILES_PATH/$SITE.pid ]; then
           rm -f $RUNFILES_PATH/$SITE.pid
        fi
        sleep 1
    done
}

ACTION="$1"
case "$ACTION" in
    start)
        echo -n "Starting $DESC:"
        d_start
        echo "."
        ;;

    stop)
        echo -n "Stopping $DESC:"
        d_stop
        echo "."
        ;;

    status)
        echo "Status of $DESC:"
        for SITE in $DJANGO_SITES
        do
            echo -n "  $SITE"
            if [ -f $RUNFILES_PATH/$SITE.pid ]; then
                echo " running ($(cat $RUNFILES_PATH/$SITE.pid))"
            else
                echo " not running"
            fi
        done
        ;;

    restart|force-reload)
        echo -n "Restarting $DESC: $NAME"
        d_stop
        sleep 2
        d_start
        echo "."
        ;;

    *)
        echo "Usage: $NAME {start|stop|restart|force-reload|status} [site]" >&2
        exit 3
        ;;
esac

exit 0
```

The default values are set in ``/etc/default/django``.

```bash
# django project names/directories
DJANGO_SITES="myapp myapp2 myapp3"

# path to the directory with your django projects
#SITES_PATH=/home/django/projects

# path to the directory conrtaining all site-specific virtualenvs 
# (see http://pypi.python.org/pypi/virtualenv for more information)
ENVIRONMENT_PATH=$SITES_PATH/environment

# path to the directory for socket and pid files
RUNFILES_PATH=$SITES_PATH/run

# please make sure this is NOT root
# local user prefered, www-data accepted
RUN_AS=django

# maximum requests before fast-cgi process respawns
# (a.k.a. get killed and let live)
MAXREQUESTS=100
```