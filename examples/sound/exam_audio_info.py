#!/usr/bin/env python
#coding: utf8
#author: Tian Xia (summer.xia1@pactera.com)

from mutagen.mp3 import MP3
from mutagen.flac import *
from common import *
from multiprocessing import Pool
import audioread
import typing
from audio.audio_helper import AudioHelper

def convert(in_file: str):
  return in_file, AudioHelper.convert_to_flac(in_file)

def get_file_length(in_file: str):
  return AudioHelper.get_music_length(in_file)

if __name__ == "__main__":
  parser = optparse.OptionParser(usage="cmd [optons] ..]")
  #parser.add_option("-q", "--quiet", action="store_true", dest="verbose",
                     #default=False, help="")
  parser.add_option("--folder")
  (options, args) = parser.parse_args()

  file_names = get_files_in_folder(options.folder,
                                   file_extensions=AudioHelper.AUDIO_EXTENSIONS,
                                   resursive=True)
  file_names = list(file_names)
  print(f"There are {len(file_names)} files found.")

  out = Pool().map(convert, file_names)
  failed_files = [in_file for in_file, out_file in out if out_file is None]
  print(f"#exception files: {len(failed_files)}")
  print("\n".join(failed_files), file=open("errors.txt", "w"))

  good_files = [out_file for in_file, out_file in out if out_file is not None]
  all_lengths = Pool().map(get_file_length, good_files)
  # print(all_lengths)
  total_seconds = sum(all_lengths)
  print(f"total length: {AudioHelper.seconds_to_str(total_seconds)}")

