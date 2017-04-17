# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:02:09 2016

@author: emadezzeldin
"""

#from bs4 import BeautifulSoup
#import requests
#import re
import os
import selenium
import lxml.html
import csv
from bs4 import BeautifulSoup
import requests
import re


def OpenBrowser () : 
    global browser
    current_directory = os.getcwd()
    path_to_chromedriver = current_directory + '/chromedriver'
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)

def update_root ():
    global root
    root = lxml.html.fromstring(browser.page_source)
    print (root)
    
def PeopleFinder (Name):
    url ='http://peoplefinder.gmu.edu/index.php?name='+Name+'&email=&group=all&title=&unit=&room=&building=&phone=&fax=&msn=&mode=advanced&x=0&y=0'
    browser.get(url)
    update_root ()
   
def nextPage ():
    nextButton =  browser.find_element_by_css_selector ( '#page > div.content > ul > li.next > a' ) 
    nextButton.click() 
    update_root ()
    
def getEmails     ():   
    Emails     =   []
    PageEmails =   browser.find_elements_by_class_name ('email-link')
    #PageEmails =   browser.find_element_by_class_name ('email-link').text
    #url ='http://peoplefinder.gmu.edu/index.php?name='+Name+'&email=&group=all&title=&unit=&room=&building=&phone=&fax=&msn=&mode=advanced&x=0&y=0'
    #People_HTML = requests.get(url)
    #People_Soup = BeautifulSoup(People_HTML.text)
    #print People_Soup.prettify ()
    for email in  PageEmails :
        Emails.append (str (email.text)) 
    return Emails
    
def getFullcontent ():
    Fullconent =   browser.find_element_by_class_name ('content').text   
    return Fullconent

    
#E.*edu
#page > div.content > div:nth-child(2) > p.email-link > a
#//*[@id="page"]/div[3]/div[1]/p[4]/a

#browser.close()
#browser.quit ()
#OpenBrowser ()
#PeopleFinder ('U')
##dictionary = {}
#for i in range (0,4000):
#    dictionary [i,'U'] = getEmails ()
#    nextPage ()
#
#
#
#Emails = []
#for key in dictionary:
#    for item in dictionary[key]:
#            spaceindex = item.find (" ")
#            item = item [spaceindex+1 : ]
#            Emails.append (item)
#            
#def writecsv():
#    with open("Emails.csv", "wb") as f:
#         writer = csv.writer(f)
#         writer.writerows([['Emails']]) 
#         for row in Emails:
#             writer.writerows([[row]]) 
#writecsv()                    