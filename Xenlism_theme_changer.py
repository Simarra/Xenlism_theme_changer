#!/usr/bin/python3
#-*-coding:utf-8-*-
from time import localtime
from subprocess import call

class c_theme_changer:

    def __init__(self):

        self.themeday = {'0':'Xenlism-Wildfire-MonDay',
        '1':'Xenlism-Wildfire-TuesDay',
        '2':'Xenlism-Wildfire-WednesDay',
        '3': 'Xenlism-Wildfire-ThursDay',
        '4' : 'Xenlism-Wildfire-FriDay',
        '5': 'Xenlism-Wildfire-SaturDay',
        '6': 'Xenlism-Wildfire-SunDay'}




    def get_date_day(self):
        self.the_day = str(localtime()).split(' ')[2].split('=')[1].replace(',','')
        return self.the_day

    def get_match(self):
        print ('voici le match')
        self.matching = self.themeday[self.get_date_day()]
        return self.matching
        
    def change_icons(self):
        call ("gsettings set org.gnome.desktop.interface icon-theme {0}".format(self.get_match()),shell=True)

if __name__ == '__main__'
    c_theme_changer().change_icons()

