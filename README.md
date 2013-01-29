amazondailyapp
==============

Some code I put together to purchase the Free Amazon App of the day.

How to use
==========

Use the keyring.py to setup your gnome keyring with your amazon credentials. Then use amazon.sh daily in your cronjobs with the correct path to amazon.py

If you don't want to use gnome's keyring simply edit amazon.py and put your credentials there or use the command line options.

Dependencies
============

You need to have mechanize, BeautifulSoup and keyring for python installed
