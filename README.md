amazondailyapp
==============

Some code I put together to purchase the Free Amazon App of the day.

How to use
==========

Invoke it with the correct command line options:
<pre>python amazon.py --username=username --password=password</pre>

Use the keyring.py to setup your gnome keyring with your amazon credentials. Then use amazon.sh daily in your cronjobs with the correct path to amazon.py. This script makes sure that the gnome keyring is initialized before running amazon.py.

If you don't want to use gnome's keyring simply edit amazon.py and put your credentials there or use the command line options.

Dependencies
============

You need to have mechanize, BeautifulSoup and gnomekeyring for python installed

On Ubuntu Linux this should be enough:
<pre>pip install mechanize beautifulsoup</pre>
