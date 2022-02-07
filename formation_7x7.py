import yaml
import os

class Formation_7x7:
    # Huawei P30 Pro settings
    SOURCE_IMG_W = 1080
    SOURCE_IMG_H = 2340
    OFFSET_X = 84
    OFFSET_Y = 720
    TROOPS_SIZE_W = 140
    TROOPS_SIZE_H = 198

    formation_array = [ 
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
        ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ]

    def __init__(self):
        
        if os.path.isfile('config.yaml') == False:
            dict = {}
            dict.update({"SOURCE_IMG_W": self.SOURCE_IMG_W})
            dict.update({"SOURCE_IMG_H": self.SOURCE_IMG_H})
            dict.update({"OFFSET_X": self.OFFSET_X})
            dict.update({"OFFSET_Y": self.OFFSET_Y})
            dict.update({"TROOPS_SIZE_W": self.TROOPS_SIZE_W})
            dict.update({"TROOPS_SIZE_H": self.TROOPS_SIZE_H})
            with open('config.yaml', "w") as f:
                yaml.dump(dict, f)
            
    # 表示座標から 7x7 キャラクタ位置を返す
    def calc_disploc2charloc(self, disp_loc_x, disp_loc_y):
        x = int(((disp_loc_x + self.TROOPS_SIZE_W/2) - self.OFFSET_X) / self.TROOPS_SIZE_W)
        y = int(((disp_loc_y + self.TROOPS_SIZE_H/2) - self.OFFSET_Y) / self.TROOPS_SIZE_H)
        return x, y

    def set_char(self, loc_x, loc_y, troop):
        if loc_x >= 0 and loc_x <= 6 and loc_y >= 0 and loc_y <= 6:
            self.formation_array[loc_x][loc_y] = troop

    def get_formation_array(self):
        return self.formation_array

    def print_formation(self):
        for y in range(0,7):
            line_char = ""
            for x in range(0,7):
                line_char += (self.formation_array[x][y] + " ")
            print(line_char)

    def output_formation(self):
        f = open("out.txt", "w", encoding='UTF-8')
        for y in range(0,7):
            line_char = ""
            for x in range(0,7):
                line_char += (self.formation_array[x][y] + " ")
            f.write(line_char+"\n")
        f.close()
