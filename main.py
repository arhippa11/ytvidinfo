import sys
import os
import time
from pytube import YouTube
from pytube import Playlist
from pytube import Channel
from pytube.cli import on_progress
from sys import argv
link = ""
def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def linkgathering():
    try:
        link = str(input("Enter the link of the video: "))
        yt = YouTube(link)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except:
        print("Link is not valid!")
        print("\nExiting...")
        sys.exit()
    linkglobal = link
    return linkglobal
linkglobal = linkgathering()
clean()
def maincommandhandler(linkglobal):
    try:
        command = str(input("youtube-dl> "))
        if command == "help":
            print("Commands:")
            print("help - Displays this message")
            print("download - Downloads the video")
            print("exit - Exits the program")
            print("link - Displays the current link")
            print("link-change - Changes the current link")
            maincommandhandler(linkglobal)
        elif command == "download":
            print("Downloading...")
            yt = YouTube(linkglobal,on_progress_callback=on_progress)
            yd = yt.streams.get_highest_resolution()
            yd.download("./YTfolder")
            print("\nDownloaded!")
            maincommandhandler(linkglobal)
        elif command == "exit":
            print("Exiting...")
            sys.exit()
        elif command == "":
            maincommandhandler(linkglobal)
        elif command == "link":
            print(linkglobal)
            maincommandhandler(linkglobal)
        elif command == "link-change":
            clean()
            linkglobal = linkgathering()
            maincommandhandler(linkglobal)
            clean()
        elif command == "clear":
            clean()
            maincommandhandler(linkglobal)
        elif command == "info":
            print("Link: ", linkglobal)
            print("Title: ", yt.title)
            print("Views: ", yt.views)
            print("Length: ", yt.length)
            print("Thumbnail URL: ", yt.thumbnail_url)
            print("Description: ", yt.description)

        else:
            print("Invalid command!")
            maincommandhandler(linkglobal)
        
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

maincommandhandler(linkglobal)

