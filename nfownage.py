#!/usr/bin/python

# NFOwnage, by Chris Daniel  http://www.chrisdaniel.net
# Released under the BSD license (see below)
#
# Copyright (c) 2009, Chris Daniel
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#  * Neither the name of the software nor the names of its contributors may be
#    used to endorse or promote products derived from this software without
#    specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import getopt, sys, MP3Info
from MP3Info import MP3Info

# Files list
files = []

# Get ripper/poster name
name = sys.argv[1]

# Rest of arguments are files, supposedly
for mp3file in getopt.getopt(sys.argv[2:],'')[1]:
   file = MP3Info(open(mp3file,'rb'))
   files.append(file) # done in two steps so I can make this a dict sorted by tracknum later

artists = []
album = ''
tracks = {} # dict containing dict for each track with title, length (total), length (min), length (sec), bitrate, indexed by tracknum
numtracks = len(files)
year = ''
genre = ''
totalbitrates = 0
vbr = 0
longesttitlelen = 0
totaltime = 0

for file in files:
   if file.artist not in artists:
      artists.append(file.artist)

   album = file.album
   year = file.year
   genre = file.genre

   # ideally, the track string is '01' or '01/12' ... won't always be, though
   if(file.track.find("/") > 0):
      # for working around weird issue where track string is something like '\x0301/12'
      tracknum = int(file.track[file.track.find("/")-2:file.track.find("/")])
   else:
      tracknum = int(file.track)

   tracks[tracknum] = {
      'artist': file.artist,
      'title': file.title,
      'length': file.mpeg.__dict__['length'],
      'length_min': file.mpeg.__dict__['length_minutes'],
      'length_sec': file.mpeg.__dict__['length_seconds'],
      'bitrate': file.mpeg.__dict__['bitrate'] }
   totalbitrates += int(file.mpeg.__dict__['bitrate'])
   vbr += int(file.mpeg.__dict__['is_vbr'])
   if len(file.title) > longesttitlelen:
      longesttitlelen = len(file.title)
   totaltime += int(file.mpeg.__dict__['length'])

avg_bitrate = totalbitrates / numtracks
if(vbr > 0):
   bitratetype = "VBR"
else:
   bitratetype = "CBR"

artist = artists[0]

if len(artists) > 1:
   artist = "Artists   : " + artist
   for item in artists:
      artist += ", " + item
else:
   artist = "Artist    : " + artist

print artist
print "Album     : " + album
print "Year      : " + str(year)
print "Genre     : " + str(genre)
print "Bitrate   : " + str(avg_bitrate) + "kbps (" + bitratetype + ")\n"

print "Ripped by : %s\n" % (name)
print "Posted by : %s\n" % (name)

print "Track Listing"
print "-------------"

for i in range(1, tracknum):
   print "%2i. %s   (%2i:%02i)" % (
         i,
         tracks[i]['title'].ljust(longesttitlelen),
         tracks[i]['length_min'],
         tracks[i]['length_sec'])

print "\nTotal playing time: %i:%02i" % (totaltime / 60, totaltime % 60)

