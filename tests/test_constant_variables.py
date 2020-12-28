import constant_variables as cvar
import numpy as np
import cv2

img = np.reshape(np.frombuffer(cvar.lena_bgr_bin, dtype=np.uint8), cvar.lena_shape)
cv2.imshow("lena", img)
cv2.waitKey(0)

img = cv2.imdecode(np.frombuffer(cvar.lena_png, dtype=np.uint8), cv2.IMREAD_ANYCOLOR)
cv2.imshow("lena", img)
cv2.waitKey(0)