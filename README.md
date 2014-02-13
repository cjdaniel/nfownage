NFOwnage
========

This is just a little script that generates a nice text file summary (what the cool kids call an NFO file), given a name, plus a list of MP3 files. Here's how you roll:

    % ./nfownage.py "Chris Daniel" /Users/chris/Music/Emily\ Haines/Cut\ in\ Half\ and\ \(Also\)\ Double/*.mp3
    Artist    : Emily Haines
    Album     : Cut in Half and (Also) Double
    Year      : 1996
    Genre     : None
    Bitrate   : 192kbps (CBR)
    
    Ripped by : Chris Daniel
    
    Posted by : Chris Daniel
    
    Track Listing
    -------------
     1. Dog               ( 2:27)
     2. Bore              ( 2:29)
     3. Eden              ( 3:32)
     4. Pretty Head       ( 2:53)
     5. Freak             ( 4:45)
     6. The View          ( 2:48)
     7. Eau de Toilette   ( 3:19)
     8. Carpet            ( 2:48)
    
    Total playing time: 30:02

If you want that in a file, redirect the output like this:

    % ./nfownage.py [...] > file.nfo

Included in this repository is a copy of MP3Info.py. I did not write this. But the version included definitely works with nfownage.py. There are later versions available, like the one at https://github.com/res0nat0r/edna/blob/master/MP3Info.py -- I haven't tested with anything else.
