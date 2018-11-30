#!/usr/bin/env python
#coding: utf8
#author: Tian Xia (summer.xia1@pactera.com)

from algorithm_3x import *
from mutagen.mp3 import MP3

def get_music_lenght(file_name: str):
  ext = file_name.partition(".")[-1].lower()
  if ext == "mp3":
    audio = MP3(file_name)
    return audio.info.length

  else:
    return -1

if __name__ == "__main__":
  os.system("clear")

  parser = optparse.OptionParser(usage="cmd [optons] ..]")
  #parser.add_option("-q", "--quiet", action="store_true", dest="verbose",
                     #default=False, help="")
  (options, args) = parser.parse_args()

  total_seconds = 0
  for file_name in args:
    seconds = get_music_lenght(file_name)
    if seconds < 0:
      print(f"unknow music format: '{file_name}'")
      continue

    total_seconds += seconds
    print(f"'{file_name}' lasts {seconds / 60:.3} minutes.")

  print(f"#time: {total_seconds / 60:.3} minutes.")

