#!/usr/bin/env python
#coding: utf8
#author: Tian Xia (summer.xia1@pactera.com)

from algorithm_3x import *
from mutagen.mp3 import MP3
import examples.sound.common as music_common
import Common as nlp_common
from multiprocessing import Pool

def get_music_lenght(file_name: str):
  ext = file_name.rpartition(".")[-1].lower()
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
  parser.add_option("--folder")
  (options, args) = parser.parse_args()

  file_names = nlp_common.get_files_in_folder(options.folder,
                                              file_exts=["mp3"],
                                              resursive=True)
  file_names = list(file_names)
  print(f"There are {len(file_names)} files found.")
  durations = Pool().map(get_music_lenght, file_names)

  total_seconds = 0
  for idx, (file_name, seconds) in enumerate(zip(file_names, durations)):
    if seconds < 0:
      print(f"unknow music format: '{idx}:{file_name}'")
      continue

    total_seconds += seconds
    time_str = music_common.seconds_to_str(seconds)
    print(f"'{idx}:{file_name}': {time_str}")

  time_str = music_common.seconds_to_str(total_seconds)
  print(f"#time: {time_str}")

