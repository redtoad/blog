---
title: "How to have applications start automatically in gnome"
date: "2009-09-29"
# tags:: gnome, autostart
# comments::
---

I'm running ubuntu jaunty on my office machine. For a 
while now I have wanted to start pidgin automatically 
at startup. 

Snooping around a bit, I found the command 
``gnome-session-properties`` which allows to do just that.
However, there is an easier way:

Simply copy the ``.desktop`` file of your application to
``~/.config/autostart``. In my case that was simply ::
  
  cp /usr/share/applications/pidgin.desktop ~/.config/autostart

This saves you the trouble of having to fill in all dialogue 
fields by hand - plus you have a nice icon.

