import depthai as dai

# Camera
rgbRes = dai.ColorCameraProperties.SensorResolution.THE_1080_P
monoRes = dai.MonoCameraProperties.SensorResolution.THE_720_P
fps: int = 30

# Encoder
encoderProfile = dai.VideoEncoderProperties.Profile.H265_MAIN
encoderQuality: int = 100