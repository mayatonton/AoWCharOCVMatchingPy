import os, sys
import cv2
import numpy
import formation_7x7

ROOT_PATH = os.path.dirname(__file__)
SOURCE_IMG_DIR = "source_img"
TEMP_IMG_DIR = "temp_img"

source_img_path = os.path.join(ROOT_PATH, SOURCE_IMG_DIR, "A.jpg")

temp_iwa_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "IWA.jpg")
temp_minarai_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "MINARAI.jpg")
temp_fune_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "FUNE.jpg")

def matching(src_img, temp_img, out_img, color, char_name):
    width, height = temp_img.shape[::-1]

    #テンプレートマッチングの実行(比較方法cv2.TM_CCORR_NORMED)
    result = cv2.matchTemplate(src_img, temp_img, cv2.TM_CCORR_NORMED)
    loc = numpy.where (result > 0.96)
    for pt in zip(*loc[::-1]):
        # pt[0], pt[1] がそれぞれ検出された画像の左上のx,y座標となるので
        # テンプレートを一致させた分の幅・高さを足して、1pixelの赤線で矩形を書く
        cv2.rectangle(out_img, pt, (pt[0] + width, pt[1] + height), color, 2)
        x,y = formation_7x7.calc_disploc2charloc(int(pt[0]), int(pt[1]))
        formation_7x7.set_char(x,y,char_name)

def main():
    # 検索先読み込み
    img = cv2.imread(source_img_path) 
    img_gray = cv2.imread(source_img_path,0)

    # 検索ネタ読み込み
    temp_iwa = cv2.imread(temp_iwa_path, 0)
    temp_minarai = cv2.imread(temp_minarai_path, 0)
    temp_fune = cv2.imread(temp_fune_path, 0)

    matching(img_gray, temp_iwa, img, (0, 0, 255), "岩")
    matching(img_gray, temp_minarai, img, (255, 0, 0), "習")
    matching(img_gray, temp_fune, img, (0, 255, 0), "船")

    # 結果を表示
    # cv2.namedWindow('result', cv2.WINDOW_NORMAL)
    # cv2.imshow("result",img)

    # cv2.waitKey(0) #キー入力待ち
    # cv2.destroyAllWindows() #ウインドウを閉じる

    fname = os.path.basename(source_img_path)
    print(f"----[{fname}]------------")
    formation_7x7.print_formation()
    print("------------------------")

    # 画像保存
    cv2.imwrite('./out_b.jpg', img)



if __name__ == "__main__":

    source_img_path = sys.argv[1]

    main()