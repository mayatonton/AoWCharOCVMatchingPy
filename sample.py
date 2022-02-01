import os
import cv2
import numpy

ROOT_PATH = os.path.dirname(__file__)
SOURCE_IMG_DIR = "source_img"
TEMP_IMG_DIR = "temp_img"

source_img_path = os.path.join(ROOT_PATH, SOURCE_IMG_DIR, "B.jpg")

temp_iwa_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "IWA.jpg")
temp_minarai_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "MINARAI.jpg")

def matching(src_img, temp_img, out_img, color):
    width, height = temp_img.shape[::-1]

    #テンプレートマッチングの実行(比較方法cv2.TM_CCORR_NORMED)
    result = cv2.matchTemplate(src_img, temp_img, cv2.TM_CCORR_NORMED)
    loc = numpy.where (result > 0.95)
    for pt in zip(*loc[::-1]):
        # pt[0], pt[1] がそれぞれ検出された画像の左上のx,y座標となるので
        # テンプレートを一致させた分の幅・高さを足して、1pixelの赤線で矩形を書く
        cv2.rectangle(out_img, pt, (pt[0] + width, pt[1] + height), color, 2)
        print(pt)

def main():
    # 検索先読み込み
    img = cv2.imread(source_img_path) 
    img_gray = cv2.imread(source_img_path,0)

    # 検索ネタ読み込み
    temp_iwa = cv2.imread(temp_iwa_path, 0)
    temp_minarai = cv2.imread(temp_minarai_path, 0)

    matching(img_gray, temp_iwa, img, (0, 0, 255))
    matching(img_gray, temp_minarai, img, (255, 0, 0))

    # 結果を表示
    # cv2.namedWindow('result', cv2.WINDOW_NORMAL)
    # cv2.imshow("result",img)

    # cv2.waitKey(0) #キー入力待ち
    # cv2.destroyAllWindows() #ウインドウを閉じる

    # 画像保存
    cv2.imwrite('./out_b.jpg', img)



if __name__ == "__main__":
    main()