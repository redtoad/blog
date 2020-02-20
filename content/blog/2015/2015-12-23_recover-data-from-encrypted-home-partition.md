---
title: "Recover data from encrypted home partition"
date: "2015-12-23"
tags: [admin, backup]
---

I've had an old desktop computer running Ubuntu sitting in my corner for quite some time. 
Now that I have a `HDD dock <http://amazon.de/dp/B0099PUVWO/>`_, it was time to see what could be salvaged!

Since I have not written down the mount passphrase (big mistake!), it took some searching...

Find /home and / partitions
------------------------------

Connect your old HDD and run

::

    $ sudo fdisk -l
    Disk /dev/mapper/cryptswap1: 7,9 GiB, 8432123904 bytes, 16468992 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 4096 bytes
    I/O size (minimum/optimal): 4096 bytes / 4096 bytes
    Disk /dev/sdb: 596,2 GiB, 640135028736 bytes, 1250263728 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x000e94b7

    Device     Boot      Start        End   Sectors   Size Id Type
    /dev/sdb1             2048  585936895 585934848 279,4G 83 Linux
    /dev/sdb2        585938942 1250263039 664324098 316,8G  5 Extended
    /dev/sdb5       1234638848 1250263039  15624192   7,5G 83 Linux
    /dev/sdb6        585938944 1234638847 648699904 309,3G 83 Linux

My partitions are ``/dev/sdb1`` (home) and ``/dev/sdb6`` (root).

Mount partitions
-------------------

So let's mount them in the right place for recovery::

    sudo umount /dev/sdb1
    sudo umount /dev/sdb6
    sudo mount /dev/sdb6 /mnt
    sudo mount /dev/sdb1 /mnt/home

    sudo mount -o bind /dev /mnt/dev
    sudo mount -o bind /dev/shm /mnt/dev/shm
    sudo mount -o bind /proc /mnt/proc
    sudo mount -o bind /sys /mnt/sys

and chroot it::

    $ sudo chroot /mnt
    root@sebastopol# su - basti
    basti@sebastopol$ ecrypt-mount-private
    Enter your login passphrase: ***


Recover data
------------

Now I can simply copy my data to anywhere on my old HDD, for instance in ``/mnt/data``.
Voilá!

Links and tutorials
-------------------

* https://help.ubuntu.com/community/EncryptedPrivateDirectory
* http://www.cyberciti.biz/faq/ubuntu-mounting-your-encrypted-home-from-livecd/
