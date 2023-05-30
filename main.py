import sys
import os
import time
from pytube import YouTube
from pytube import Playlist
from pytube import Channel
from pytube.cli import on_progress
from sys import argv
link = ""
linkglobal = ""
linkplaylist = ""
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
def playlistlinkgathering():
    try:
        link = str(input("Enter the link of the playlist: "))
        playlist = Playlist(link)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except:
        print("Link is not valid!")
        print("\nExiting...")
        sys.exit()
    linkplaylist = link
    return linkplaylist
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
            yt = YouTube(linkglobal)
            print("Link: ", linkglobal)
            print("Title: ", yt.title)
            print("Views: ", yt.views)
            print("Length: ", yt.length)
            print("Thumbnail URL: ", yt.thumbnail_url)
            print("Description: ", yt.description)
            maincommandhandler(linkglobal)

        else:
            print("Invalid command!")
            maincommandhandler(linkglobal)
        
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
def maincommandhandlerplaylist(linkplaylist):
    try:
        command = str(input("youtube-dl (playlist mode)> "))
        if command == "help":
            print("Commands:")
            print("help - Displays this message")
            print("download - Downloads the video")
            print("exit - Exits the program")
            print("link - Displays the current link")
            print("link-change - Changes the current link")
            maincommandhandlerplaylist(linkplaylist)
        elif command == "download":
            print("Downloading...")
            yt = Playlist(linkplaylist)
            for video in yt.videos:
                video.register_on_progress_callback(on_progress)
                print("\nDownloading: ", video.title)
                video.streams.get_highest_resolution().download("./YTfolder")
            print("\nDownloaded!")
            maincommandhandlerplaylist(linkplaylist)
        elif command == "exit":
            print("Exiting...")
            sys.exit()
        elif command == "":
            maincommandhandlerplaylist(linkplaylist)
        elif command == "link":
            print(linkplaylist)
            maincommandhandlerplaylist(linkplaylist)
        elif command == "link-change":
            clean()
            linkplaylist = playlistlinkgathering()
            maincommandhandlerplaylist(linkplaylist)
            clean()
        elif command == "clear":
            clean()
            maincommandhandlerplaylist(linkplaylist)
        elif command == "info":
            yt = Playlist(linkplaylist)
            print("Link: ", linkplaylist)
            print("Title: ", yt.title)
            maincommandhandlerplaylist(linkplaylist)

        else:
            print("Invalid command!")
            maincommandhandlerplaylist(linkplaylist)
        
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

print("Welcome to youtube-dl!")
playlistorvideo = str(input("Is it a playlist or a video? (playlist/video): "))
if playlistorvideo == "playlist":
    playlistorvideo = "playlist"
    linkplaylist = playlistlinkgathering()
elif playlistorvideo == "video":
    playlistorvideo = "video"
    linkglobal = linkgathering()
if playlistorvideo == "playlist":
    maincommandhandlerplaylist(linkplaylist)
elif playlistorvideo == "video":
    maincommandhandler(linkglobal)

