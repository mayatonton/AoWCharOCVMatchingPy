import os

ROOT_PATH = os.path.dirname(__file__)
SOURCE_IMG_DIR = "source_img"
TEMP_IMG_DIR = "temp_img"


class troops:
    def __init__(self):
        self.temp_path = ""
        self.x = 0
        self.y = 0

    def set_disploc(self, x, y):
        self.disp_x = x
        self.disp_y = y

    def get_loc(img_width, img_height):
        offset_x = 0
        offset_y = 0
        # 7 x 7


class iwa(troops):
    def __init__(self):
        super().__init__()
        self.temp_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "IWA.jpg")

class minarai(troops):
    def __init__(self):
        super().__init__()
        self.temp_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "MINARAI.jpg")