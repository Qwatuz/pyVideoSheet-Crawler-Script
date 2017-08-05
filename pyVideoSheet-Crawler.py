#!/usr/bin/python

import os

for root, dirnames, filenames in os.walk('/home/user/path/'):
  for filename in filenames:
    if filename.lower().endswith(('.m4v', '.mov', '.mpeg', 'mp4')):
      ifile = os.path.join(root, filename)
      ofile = os.path.splitext(ifile)[0] + ".jpg"
      try:
        with open(ofile) as f: pass
      except IOError as e:
        print "Generating thumbnail for: " + ifile

#        fftoptions = "-s0 -f"
        command = 'python -m pyVideoSheet.create --font /usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf 20 --bgcolour 15 219 76 1 --textcolour 0 0 0 1 -t 300 300 -c 6 --header 120 -n 72 -i 15 "%s" -o "%s"' % (ifile, ofile)

        p = os.popen(command,"r")
        while 1:
          line = p.readline()
          if not line: break
          print line
