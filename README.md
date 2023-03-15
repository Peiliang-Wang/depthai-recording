# depthai-video-recording

```
Record RGB and stereo video with DepthAI OAK-D

options:
  -h, --help       show this help message and exit
  -p, --preview    Show preview, nothing will be recorded
  -c, --codec      Available codec: ["h265", "mjpeg", "lossless"], default="h265"
  -q, --quality    Encoding quality, default="100"
  -m, --mp4        Convert the stream files to MP4 after recording (Require ffmpeg be installed)
  -o, --out        Output directory path, default="output"
  --rgbres         RGB camera resolution: ["12mp", "4k", "1080p"], default="1080p"
  --monores        Mono camera resolution: ["800p", "720p", "400p"], default="800p"
```

## Requirements

* ffmpeg (Required if specify option `-m`)

## Dependencies

* depthai
* numpy
* opencv-python

## License

[![AGPLv3](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.html)

Licensed under the [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.html).
