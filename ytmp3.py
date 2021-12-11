#YT MP3 Downloader
#Brady Hatch

from __future__ import unicode_literals
import youtube_dl
from cfonts import render
import time
import sys
import os

#cool ass banner that ur gonna look at this source code to see
#how to do nerd
banner = render("MP3", colors=['red', 'blue'], align = 'center')
print(banner)

#self advertisement >:)
print("xxxxxxxxxxxPOGGERSxxxxxxxxxxx")
print("\n")

print("||||||| Made by:brxdy |||||||")
print("\n")

print("xxxxxxxxxxxPOGGERSxxxxxxxxxxx")
print("\n")

#getting URL from user
url = input("Paste YT link and press enter nerd 8====D- :")
print("\n")

#display starting message
print("starting the pirating")

#YT Downloader Options
DL_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Music'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': DL_PATH + '/%(title)s.%(ext)s',
}

#main download function
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    
print("\n")
print("Thank you for pirating music")