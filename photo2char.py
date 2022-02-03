import os, sys
import cv2
import numpy
import formation_7x7

ROOT_PATH = os.path.dirname(__file__)
SOURCE_IMG_DIR = "source_img"
TEMP_IMG_DIR = "temp_img"

source_img_path = os.path.join(ROOT_PATH, SOURCE_IMG_DIR, "A.jpg")

temp_assassin_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "ASSASSIN.jpg")
temp_fune_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "FUNE.jpg")
temp_goburin_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "GOBURIN.jpg")
temp_gorem_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "GOREM.jpg")
temp_hone_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "HONE.jpg")
temp_hyoketu_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "HYOKETU.jpg")
temp_iwa_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "IWA.jpg")
temp_kemono_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "KEMONO.jpg")
temp_kenshi_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "KENSHI.jpg")
temp_majo_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "MAJO.jpg")
temp_minarai_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "MINARAI.jpg")
temp_pumpkin_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "PUMPKIN.jpg")
temp_toteki_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "TOTEKI.jpg")
temp_varistor_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "VARISTOR.jpg")
temp_yasha_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "YASHA.jpg")
temp_zombie_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "ZOMBIE.jpg")

temp_icemeiji_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "ICEMEIJI.jpg")
temp_syudo_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "SYUDO.jpg")
temp_pmeiji_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "PMEIJI.jpg")


def matching(src_img, temp_img, out_img, color, char_name):
    width, height = temp_img.shape[::-1]

    #テンプレートマッチングの実行(比較方法cv2.TM_CCORR_NORMED)
    result = cv2.matchTemplate(src_img, temp_img, cv2.TM_CCORR_NORMED)
    loc = numpy.where (result > 0.965)
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
    temp_assassin = cv2.imread(temp_assassin_path, 0)
    temp_fune = cv2.imread(temp_fune_path, 0)
    temp_goburin = cv2.imread(temp_goburin_path, 0)
    temp_gorem = cv2.imread(temp_gorem_path, 0)
    temp_hone = cv2.imread(temp_hone_path, 0)
    temp_hyoketu = cv2.imread(temp_hyoketu_path, 0)
    temp_iwa = cv2.imread(temp_iwa_path, 0)
    temp_kemono = cv2.imread(temp_kemono_path, 0)
    temp_kenshi = cv2.imread(temp_kenshi_path, 0)
    temp_majo = cv2.imread(temp_majo_path, 0)
    temp_minarai = cv2.imread(temp_minarai_path, 0)
    temp_pumpkin = cv2.imread(temp_pumpkin_path, 0)
    temp_toteki = cv2.imread(temp_toteki_path, 0)
    temp_varistor = cv2.imread(temp_varistor_path, 0)
    temp_yasha = cv2.imread(temp_yasha_path, 0)
    temp_zombie = cv2.imread(temp_zombie_path, 0)
    temp_icemeiji = cv2.imread(temp_icemeiji_path, 0)
    temp_pcemeiji = cv2.imread(temp_pmeiji_path, 0)
    temp_syudo = cv2.imread(temp_syudo_path, 0)

    matching(img_gray, temp_assassin, img, (255, 255, 255), "ア")
    matching(img_gray, temp_fune, img, (255, 255, 255), "船")
    matching(img_gray, temp_goburin, img, (255, 255, 255), "砲")
    matching(img_gray, temp_gorem, img, (255, 255, 255), "ゴ")
    matching(img_gray, temp_hone, img, (255, 255, 255), "骨")
    matching(img_gray, temp_hyoketu, img, (255, 255, 255), "弓")
    matching(img_gray, temp_iwa, img, (255, 255, 255), "岩")
    matching(img_gray, temp_kemono, img, (255, 255, 255), "獣")
    matching(img_gray, temp_kenshi, img, (255, 255, 255), "剣")
    matching(img_gray, temp_majo, img, (255, 255, 255), "魔")
    matching(img_gray, temp_minarai, img, (255, 255, 255), "習")
    matching(img_gray, temp_pumpkin, img, (255, 255, 255), "パ")
    matching(img_gray, temp_toteki, img, (255, 255, 255), "投")
    matching(img_gray, temp_varistor, img, (255, 255, 255), "バ")
    matching(img_gray, temp_yasha, img, (255, 255, 255), "夜")
    matching(img_gray, temp_zombie, img, (255, 255, 255), "ゾ")
    matching(img_gray, temp_icemeiji, img, (255, 255, 255), "凍")
    matching(img_gray, temp_pcemeiji, img, (255, 255, 255), "プ")
    matching(img_gray, temp_syudo, img, (255, 255, 255), "修")

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