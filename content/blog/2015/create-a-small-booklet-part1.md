---
title: "Create a small booklet"
date: 2015-12-23
#tags: [pstools, pdf, booklet]
---

We have quite a number of addresses in various locations both digital and offline. 
In order to do away with this chaos, I wanted to produce a comprehensive, offline, old school, paper address book
because it is much easier to handle even for not so digital savy people.

I'm using OpenOffice/LibreOffice and the format I'm going for is **A4 folded length-wise (297x105mm)**.

After some reasearch involving pdfjam, pdftk, Multivalent.jar
I went back to over plain old psutils (via https://gist.github.com/antlypls/847095).

# The individual steps

First I store my address book as PDF and convert the PDF into PS using:

    $ pdf2ps ~/Desktop/addresses.pdf addresses.ps

Now I can re-arrange the pages for booklet printing. ``pdfbook`` works directly on
PDFs but I could not for the life of me figure out how to make it work with my
unusual format. So I used

    $ psbook addresses.ps addresses.book.ps
    [*] [1] [2] [*] [26] [3] [4] [25] [24] [5] [6] [23] [22] [7] [8] [21] [20] 
    [9] [10] [19] [18] [11] [12] [17] [16] [13] [14] [15] 
    Wrote 28 pages, 1456897 bytes

That was the easy bit. Now for joining the pages:

    $ pstops -pa4 "2:0@1+1@1(10.5cm,0)" addresses.book.ps addresses.joined.ps
    [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] 
    Wrote 14 pages, 1467145 bytes

This will combine two pages (``2:___+___``) both un-scaled (``@1``; you could 
leave this out) on the same page (that's the ``+``) with the second one
translated to the right (``(10.5cm,0)``).

After that it's simply converting it back to PDF again:

    $ ps2pdf addresses.joined.ps addresses.book.pdf

# Putting everything together

All tools in psutils usually deal with stdin, so it's easy to chain them:

    pdf2ps ~/Desktop/addresses.pdf - | \
    psbook | \
    pstops -pa4 "2:0@1+1@1(10.5cm,0)" | \
    ps2pdf - ~/Desktop/addresses-booklet.pdf 

And that's it!


