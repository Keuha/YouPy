#!/usr/bin/env python3
import argparse
import sys
import re
import os
import urllib.request
import pafy
import shutil
import time
import subprocess

FFMPEG_BIN = "ffmpeg"

class download:
    
    def __init__(self, url, video, playlist, artist, song, convert):
        self.url = url
        self.playlist = playlist
        if self.playlist:
            self.pafy = pafy.get_playlist(url)
        else:
            self.pafy = pafy.new(url)
        self.video = video
        
        if not artist and not self.playlist:
            limit = self.pafy.title.find("-")
            if limit > 0:
                self.artist = self.pafy.title[:limit]
        elif artist and not self.playlist:
            self.artist = artist
        else:
            self.artist = ""
        
        if not song and not self.playlist:
            limit = self.pafy.title.find("-")
            if limit > 0:
                self.song = self.pafy.title[limit + 1:]
        elif song and not self.playlist:
            self.song = song
        else:
            self.song = ""

        self.convert = convert

    def getGoodStuff(self, stream):
        if self.video:
            return stream.getbest()
        return stream.getbestaudio()

    def download(self):
        if self.playlist:
            self.downloadPlaylist()
        stuff = self.getGoodStuff(self.pafy)
        if not os.path.exists("./" + self.artist) or not os.path.isdir("./" + self.artist):
            os.makedirs("./" + self.artist)
            stuff.download(quiet=False, filepath="./" + self.artist)
        for fname in os.listdir("./" + self.artist):
            if fname.startswith(stuff.title):
                os.rename(os.path.dirname(os.path.realpath(__file__)) + "/" + self.artist + "/" + fname, os.path.dirname(os.path.realpath(__file__)) + "/" + self.artist + "/" + self.song + "." + stuff.extension)
            if not self.video and self.convert:
                print("converting ", self.pafy.title, " to MP3 format")
                self.convertingMP3(os.path.dirname(os.path.realpath(__file__)) + "/" + self.artist + "/" + self.song + "." + stuff.extension)
            else:
                print("no convert")

    def downloadPlaylist(self):
        length = len(self.pafy['items'])
        name = self.pafy['title']
        if not os.path.exists("./" + name) or not os.path.isdir("./" + name):
            os.makedirs("./" + name)
        for e in self.pafy['items']:
            print("downloading : ", e['pafy'].title)
            try:
                stuff = self.getGoodStuff(e['pafy'])
                if stuff:
                    stuff.download(quiet=False, filepath="./" + name)
                    if not self.video and self.convert:
                        print("\nconverting ", e['pafy'].title, " to MP3 format")
                        self.convertingMP3(os.path.dirname(os.path.realpath(__file__)) + "/" + name + "/" + e['pafy'].title + ".m4a")
                else:
                    print("failed to download : ", e['pafy'].title)
            except:
                print("\nsomething went wrong with : ", e['pafy'].title)
            time.sleep(.300)

    def convertingMP3(self, song):
        extension = len(song) - 3
        redir = open('/dev/null')
        if os.path.isfile(song[:extension] + 'mp3'):
            os.remove(song[:extension] + 'mp3')
        command = [FFMPEG_BIN, '-i', song, song[:extension] + 'mp3']
        subprocess.check_call(command, stdout=redir, stderr=redir)
        os.remove(song)
        print("Convert in MP3 successfuly")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, help="here paste a YouTube url")
    parser.add_argument("-v", "--video", help="download video mode", action="store_true")
    parser.add_argument("--artist", help="precise artiste name")
    parser.add_argument("--song", help="precise song name")
    parser.add_argument("--playlist", help="will download a whole playlist, can be use with -v --video", action="store_true")
    parser.add_argument("--convert", help="convert audio files in MP3, use ffmpeg", action="store_true")
    args = parser.parse_args()
    downloader = download(args.url, args.video, args.playlist, args.artist, args.song, arg.convert)
    downloader.download()
