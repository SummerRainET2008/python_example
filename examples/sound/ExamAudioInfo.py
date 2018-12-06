#!/usr/bin/env python
#coding: utf8
#author: Tian Xia (summer.xia1@pactera.com)

from mutagen.mp3 import MP3
from mutagen.flac import *
from Common import *
from multiprocessing import Pool
import audioread

AUDIO_EXTENSIONS = [
  "mp3",      # converted to wav
  "flac",
  "wav",
  "sph",      # converted to wav
]

STATUS_ERROR          = -1
STATUS_UNKNOWN        = -3

def seconds_to_str(seconds: float):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  seconds = int(seconds - hours * 3600 - minutes * 60)

  return f"{hours} h {minutes} m {seconds} s"

def get_music_length(in_file: str):
  ext = get_file_extension(in_file)
  try:
    if ext == "mp3":
      audio = MP3(in_file)

      out_file = in_file + ".wav"
      if os.path.exists(out_file):
        return get_music_length(out_file)

      cmd = f"ffmpeg -i {in_file} {out_file}"
      code = execute_cmd(cmd)
      if code == 0:
        return audio.info.length
      else:
        return STATUS_ERROR

    elif ext == "flac":
      audio = FLAC(in_file)
      return audio.info.length

    elif ext == "wav":
      audio = audioread.audio_open(in_file)
      return audio.duration

    elif ext == "sph":
      out_file = f"{in_file}.wav"
      if os.path.exists(out_file):
        return get_music_length(out_file)

      cmd = f"sox {in_file} {out_file}"
      code = execute_cmd(cmd)
      if code == 0:
        return get_music_length(out_file)

      cmd = "sph2pipe -f rif {file_name} {out_file}"
      code = execute_cmd(cmd)
      if code == 0:
        return get_music_length(out_file)

      return STATUS_ERROR

    else:
      return STATUS_UNKNOWN

  except:
    print(f"Exception occurred in reading '{in_file}'")
    return STATUS_ERROR

if __name__ == "__main__":
  parser = optparse.OptionParser(usage="cmd [optons] ..]")
  #parser.add_option("-q", "--quiet", action="store_true", dest="verbose",
                     #default=False, help="")
  parser.add_option("--folder")
  (options, args) = parser.parse_args()

  file_names = get_files_in_folder(options.folder,
                                   file_extensions=AUDIO_EXTENSIONS,
                                   resursive=True)
  file_names = list(file_names)
  print(f"There are {len(file_names)} files found.")

  durations = Pool().map(get_music_length, file_names)

  total_seconds = defaultdict(float)
  error_file_num = 0
  error_files = []
  for idx, (file_name, seconds) in enumerate(zip(file_names, durations)):
    if seconds < 0:
      if seconds in [STATUS_ERROR, STATUS_UNKNOWN]:
        error_file_num += 1
        error_files.append(file_name)

      continue

    time_str = seconds_to_str(seconds)
    # print(f"'{idx}:{file_name}': {time_str}")

    total_seconds[get_file_extension(file_name)] += seconds

  print(f"#exception files: {error_file_num}")
  print("\n".join(error_files), file=open("errors.txt", "w"))

  print(f"There are {len(file_names)} files found.")
  for ext in total_seconds:
    seconds = total_seconds[ext]
    time_str = seconds_to_str(seconds)
    print(f"type='{ext}', #time: {time_str}")

