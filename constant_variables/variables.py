from constant_variables import lena

# commonly used resolutions, source: https://en.wikipedia.org/wiki/Graphics_display_resolution

# 16:9
resolution_16k = (17280, 4320)
resolution_8k = (7680, 4320)
resolution_5k = (5120, 2880)
resolution_uhd = resolution_4k = (3840, 2160)
resolution_wqhd = resolution_qhd = resolution_2k = resolution_1440p = (2560, 1440)
resolution_fhd = resolution_1080p = (1920, 1080)
resolution_hd = resolution_720p = (1280, 720)

# 4:3
resolution_xga = (1024, 768)
resolution_vga = (640, 480)

# Lena test image
lena_jpg = lena.jpg
lena_png = lena.png
lena_rgb_bin = lena.rgb
lena_bgr_bin = lena.bgr
lena_shape = (512, 512, 3)  # width, height, channels
