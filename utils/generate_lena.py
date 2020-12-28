from urllib.request import urlopen, Request
from pathlib import Path
import cv2
import numpy as np


def download_lena_from_wikipedia():
    wiki_lena_download_link = (
        "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
    )
    request = Request(wiki_lena_download_link, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(request)
    img_fpath = "lena.png"
    with open(img_fpath, "wb") as f:
        f.write(response.read())
        return img_fpath


if __name__ == "__main__":
    lena_png_fpath = download_lena_from_wikipedia()
    if lena_png_fpath is None:
        raise RuntimeError("Failed to download lena png file.")

    np_png = np.fromfile(lena_png_fpath, dtype=np.uint8)
    np_bgr = cv2.imdecode(np_png, cv2.IMREAD_ANYCOLOR)
    cv2.imshow("lena", np_bgr)
    cv2.waitKey(5000)
    np_rgb = cv2.cvtColor(np_bgr, cv2.COLOR_BGR2RGB)
    _, np_jpg = cv2.imencode(".jpg", np_bgr)

    with open("constant_variables/lena.py", "w") as lena_file:
        lena_file.write("png = {}\n".format(np_png.tostring()))
        lena_file.write("jpg = {}\n".format(np_jpg.tostring()))
        lena_file.write("rgb = {}\n".format(np_rgb.tostring()))
        lena_file.write("bgr = {}\n".format(np_bgr.tostring()))

    Path(lena_png_fpath).unlink()