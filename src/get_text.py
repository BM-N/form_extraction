import easyocr
import cv2
import numpy as np

def get_text_from_img(image_file) -> str:
    nparr = np.frombuffer(image_file, dtype=np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # imgr = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # for test purposes only.
    reader = easyocr.Reader(['pt'], gpu=True)
    text_list =  reader.readtext(img, detail = 0, paragraph=False)
    text = '\n'.join(text_list)
    return text