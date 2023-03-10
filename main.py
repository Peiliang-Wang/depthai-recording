#!/usr/bin/env python3

from parsecli import *
from recorder import *

from pathlib import Path

if __name__ == "__main__":
  scriptPath = Path(__file__).parent

  # Init
  print("Init...")
  cliArgs = parseCli()
  recorder = Recorder(cliArgs.rgbres, cliArgs.monores, 30)
  if cliArgs.preview:
    recorder.preview()
  else:
    recorder.record(
        Path(cliArgs.out), cliArgs.mp4, cliArgs.codec, cliArgs.quality)
