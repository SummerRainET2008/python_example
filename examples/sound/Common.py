def seconds_to_str(seconds: float):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  seconds = int(seconds - hours * 3600 - minutes * 60)

  return f"{hours} h {minutes} m {seconds} s"


if __name__ == "__main__":
  print(seconds_to_str(3800))