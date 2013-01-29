#!/usr/bin/python

import sys
from optparse import OptionParser
import mechanize
from BeautifulSoup import BeautifulSoup
import time,random
from keyring import Keyring
import os

didIbuy = False

def getOptions():
    arguments = OptionParser()
    arguments.add_options(["--username", "--password", "--firstyear"])
    return arguments.parse_args()[0]

def find_appstore(html):
    soup = BeautifulSoup(html)
    for link in soup.findAll("a", {"class":"nav_a nav_item"}):
        if link.find(text="Apps"):
            return link["href"]
    return None

def isappfree(soup):
    if soup.find("span", {"class":"new-price"}, text="Free") == "Free":
        return True
    return False

def getfreeapp(html, br):
    global didIbuy
    soup = BeautifulSoup(html)
    for widget in soup.findAll("div", {"class":"fad-widget-large"}):
        if isappfree(widget):
            br.select_form(name="handleBuy")
            appurchached = br.submit().read()
            #print appurchached
            didIbuy = True
        else:
            print "Free app not free!"

if __name__ == '__main__':

    kr = Keyring()
    #time.sleep(random.randint(1,120))
    options = getOptions()

    br = mechanize.Browser()
#   br.set_proxies({"http":"localhost:8080"})
    br.set_handle_robots(False)
    br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

    sign_in = br.open("http://www.amazon.com/gp/flex/sign-out.html")

    br.select_form(name="sign-in")
    if options.username != None:
        br["email"] = options.username
        br["password"] = options.password
    else:
        while kr.get_user("Amazon") is None:
            user = raw_input('Amazon user name:')
            password = raw_input('Amazon password:')
            ok = raw_input('Save (y/N)?').lower().startswith('y')
            if ok:
                kr.set_password("Amazon", user, password)
    # set your static credentials here if you want
    br["email"] = kr.get_user("Amazon")
    br["password"] = kr.get_password("Amazon")
    logged_in = br.submit().read()

    error_str = "The e-mail address and password you entered do not match any accounts on record."
    if error_str in logged_in:
        print error_str
        sys.exit(1)
    #print "Successfully logged in!"
    appstore_url = find_appstore(logged_in)
    if appstore_url == None:
        print "Appstore not found. Amazon site has changed!"
        sys.exit(0)
    for i in range(0,5):
        if appstore_url:
          appstore_html = br.open(appstore_url).read()
          getfreeapp(appstore_html,br)
        if didIbuy:
            sys.exit(0)
    print "I didn't buy the free app today! What's wrong with me? :("
