# YouPy
a youtube video/audio/playlist downloader made in python 3 using Pafy

Still in progress

To use it:

chmod +x YouPy.Py

./YouPy.py [-option]

Option:

* --url : paste a youtube URL here
* --video : if you want to download the video clip
* --playlist : if you want to dowload a whole playlist
* --artist : inform artist name (won't work with --playlist)
* --song : informe song name (won't work with --playlist)
* --convert : convert audio track in MP3 (use ffmpeg)
* --playname : give a name to playlist
* --album : add a folder into artist / playlist folder, save content into

Example : 

./YouPy --url http://youtube.com/thingsthatyouwantodownload --playlist --playname "bar" --album "foo" --convert

YouPy will create a repository named after the artist name and put the song downloaded in it.
All files will be downloaded on maximum available YouTube quality
While downloading a playlist, repository will be named after playlist name.

I know that a lot of software already do it, but i wanted to do one by myself.

Feel free to fork me ! 

#to do

- [ ] user interface
- [ ] installer
- [ ] more test
