#!/usr/bin/env python
#coding: utf8
#author: Tian Xia (summer.xia1@pactera.com)

from algorithm_3x import *
from mutagen.mp3 import MP3
from mutagen.flac import *
import examples.sound.common as music_common
import Common as nlp_common
from multiprocessing import Pool
import audioread

AUDIO_EXTENSIONS = [
  "mp3",
  "flac",
  "wav"
]

def get_file_extension(file_name: str):
  return file_name.rpartition(".")[-1].lower()

def get_music_lenght(file_name: str):
  ext = get_file_extension(file_name)
  try:
    if ext == "mp3":
      audio = MP3(file_name)
      return audio.info.length

    elif ext == "flac":
      audio = FLAC(file_name)
      return audio.info.length

    elif ext == "wav":
      audio = audioread.audio_open(file_name)
      return audio.duration

    else:
      return -1

  except:
    print(f"Exception occurred in reading '{file_name}'")
    return -1

if __name__ == "__main__":
  os.system("clear")

  parser = optparse.OptionParser(usage="cmd [optons] ..]")
  #parser.add_option("-q", "--quiet", action="store_true", dest="verbose",
                     #default=False, help="")
  parser.add_option("--folder")
  (options, args) = parser.parse_args()

  file_names = nlp_common.get_files_in_folder(options.folder,
                                              file_exts=AUDIO_EXTENSIONS,
                                              resursive=True)
  file_names = list(file_names)
  print(f"There are {len(file_names)} files found.")
  durations = Pool().map(get_music_lenght, file_names)

  total_seconds = defaultdict(float)
  error_file_num = 0
  for idx, (file_name, seconds) in enumerate(zip(file_names, durations)):
    if seconds < 0:
      error_file_num += 1
      continue

    time_str = music_common.seconds_to_str(seconds)
    # print(f"'{idx}:{file_name}': {time_str}")

    total_seconds[get_file_extension(file_name)] += seconds

  print(f"#exception files: {error_file_num}")
  for ext in total_seconds:
    seconds = total_seconds[ext]
    time_str = music_common.seconds_to_str(seconds)
    print(f"type='{ext}', #time: {time_str}")

