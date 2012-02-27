Migrating to Google Apps
========================

There is a nice piece of software called `imapsync`_. Unfortunately, the author
decided to stop releasing the package as OpenSource but rather sell it.  42
Euros seemed a tad high for my use case, especially since I'm planning to use
this only once.

Luckily, there is still an older version `available in the debian archive`_. A simple ::

    sudo apt-get install libmail-imapclient-perl
    sudo dpkg -i ~/Downloads/imapsync_1.315+dfsg-1_all.deb 

will install the dependencies, after which you can simply start the copying
process with ::

    imapsync \
      --host1 <original imap server> --user1 <girlfriend> --password1 **** \
      --host2 imap.googlemail.com --user2 <girfriend> --password2 **** \
       --ssl1 --ssl2 --useheader 'Message-Id' --skipsize --noauthmd5 \
      --reconnectretry1 1 --reconnectretry2 1

To make sure that the e-mails end up in the right place, you need to run the
same command but this time with the following addendum::

    imapsync ... \
      --prefix2 '[Gmail]/' --folder 'INBOX.Sent' \
      --regextrans2 's/Sent/Gesendet/'

and ::

    imapsync ... \
      --prefix2 '[Gmail]/' --folder 'INBOX.Drafts' \
      --regextrans2 's/Drafts/Entw&APw-rfe/'

That should be all that's needed. Please note that this process can take a
while!

Further information:

* http://www.ducea.com/2010/08/09/howto-migrate-your-email-to-google-apps-over-the-weekend/
  (where I got most of my information from)
* http://www.hanselman.com/blog/MigratingAFamilyToGoogleAppsFromGmailThunderbirdOutlookAndOthersTheDefinitiveGuide.aspx

.. _imapsync: http://imapsync.lamiral.info/
.. _available in the debian archive: http://snapshot.debian.org/package/imapsync/1.315%2Bdfsg-1/

.. author:: default
.. categories:: admin
.. tags:: google apps, e-mail
.. comments::
