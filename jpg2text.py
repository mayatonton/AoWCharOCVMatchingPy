import os, sys
import cv2
import numpy
import formation_7x7

ROOT_PATH = os.path.dirname(__file__)
SOURCE_IMG_DIR = "source_img"
#TEMP_IMG_DIR = "temp_img_iphonese"
TEMP_IMG_DIR = "temp_img_huaweiP30Pro"

source_img_path = ""

# temp_assassin_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "ASSASSIN.jpg")
# temp_bakudan_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "BAKUDAN.jpg")
# temp_bear_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "BEAR.jpg")
# temp_capapult_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "CATAPULT.jpg")
# temp_daemon_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "DAEMON.jpg")
# temp_defender_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "DEFENDER.jpg")
# temp_fmeiji_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "FMEIJI.jpg")
# temp_fune_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "FUNE.jpg")
# temp_gakusha_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "GAKUSHA.jpg")
# temp_goburin_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "GOBURIN.jpg")
# temp_gorem_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "GOREM.jpg")
# temp_hohe_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "HOHE.jpg")
# temp_hone_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "HONE.jpg")
# temp_hyoketu_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "HYOKETU.jpg")
# temp_icemeiji_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "ICEMEIJI.jpg")
# temp_iwa_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "IWA.jpg")
# temp_jigoku_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "JIGOKU.jpg")
# temp_junrei_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "JUNREI.jpg")
# temp_kamikaze_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "KAMIKAZE.jpg")
# temp_kemono_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "KEMONO.jpg")
# temp_kenshi_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "KENSHI.jpg")
# temp_majo_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "MAJO.jpg")
# temp_minarai_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "MINARAI.jpg")
# temp_necro_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "NECRO.jpg")
# temp_ogre_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "OGRE.jpg")
# temp_paladin_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "PALADIN.jpg")
# temp_pharaoh_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "PHARAOH.jpg")
# temp_pmeiji_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "PMEIJI.jpg")
# temp_pumpkin_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "PUMPKIN.jpg")
# temp_sabo_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "SABO.jpg")
# temp_sai_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "SAI.jpg")
# temp_senkusha_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "SENKUSHA.jpg")
# temp_soko_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "SOKO.jpg")
# temp_soul_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "SOUL.jpg")
# temp_syudo_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "SYUDO.jpg")
# temp_temple_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "TEMPLE.jpg")
# temp_toteki_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "TOTEKI.jpg")
# temp_totem_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "TOTEM.jpg")
# temp_tozoku_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "TOZOKU.jpg")
# temp_varistor_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "VARISTOR.jpg")
# temp_viking_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "VIKING.jpg")
# temp_voodoo_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "VOODOO.jpg")
# temp_yari_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "YARI.jpg")
# temp_yasha_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "YASHA.jpg")
# temp_yumi_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "YUMI.jpg")
# temp_zombie_path = os.path.join(ROOT_PATH, TEMP_IMG_DIR, "ZOMBIE.jpg")

temp_assassin_path = "./" + TEMP_IMG_DIR + "/" + "ASSASSIN.jpg"
temp_bakudan_path = "./" + TEMP_IMG_DIR + "/" +  "BAKUDAN.jpg"
temp_bear_path = "./" + TEMP_IMG_DIR + "/" +  "BEAR.jpg"
temp_capapult_path = "./" + TEMP_IMG_DIR + "/" +  "CATAPULT.jpg"
temp_daemon_path = "./" + TEMP_IMG_DIR + "/" +  "DAEMON.jpg"
temp_defender_path = "./" + TEMP_IMG_DIR + "/" +  "DEFENDER.jpg"
temp_fmeiji_path = "./" + TEMP_IMG_DIR + "/" +  "FMEIJI.jpg"
temp_fune_path = "./" + TEMP_IMG_DIR + "/" +  "FUNE.jpg"
temp_gakusha_path = "./" + TEMP_IMG_DIR + "/" +  "GAKUSHA.jpg"
temp_goburin_path = "./" + TEMP_IMG_DIR + "/" +  "GOBURIN.jpg"
temp_gorem_path = "./" + TEMP_IMG_DIR + "/" +  "GOREM.jpg"
temp_hohe_path = "./" + TEMP_IMG_DIR + "/" +  "HOHE.jpg"
temp_hone_path = "./" + TEMP_IMG_DIR + "/" +  "HONE.jpg"
temp_hyoketu_path = "./" + TEMP_IMG_DIR + "/" +  "HYOKETU.jpg"
temp_icemeiji_path = "./" + TEMP_IMG_DIR + "/" +  "ICEMEIJI.jpg"
temp_iwa_path = "./" + TEMP_IMG_DIR + "/" +  "IWA.jpg"
temp_jigoku_path = "./" + TEMP_IMG_DIR + "/" +  "JIGOKU.jpg"
temp_junrei_path = "./" + TEMP_IMG_DIR + "/" +  "JUNREI.jpg"
temp_kamikaze_path = "./" + TEMP_IMG_DIR + "/" +  "KAMIKAZE.jpg"
temp_kemono_path = "./" + TEMP_IMG_DIR + "/" +  "KEMONO.jpg"
temp_kenshi_path = "./" + TEMP_IMG_DIR + "/" +  "KENSHI.jpg"
temp_majo_path = "./" + TEMP_IMG_DIR + "/" +  "MAJO.jpg"
temp_minarai_path = "./" + TEMP_IMG_DIR + "/" +  "MINARAI.jpg"
temp_necro_path = "./" + TEMP_IMG_DIR + "/" +  "NECRO.jpg"
temp_ogre_path = "./" + TEMP_IMG_DIR + "/" +  "OGRE.jpg"
temp_paladin_path = "./" + TEMP_IMG_DIR + "/" +  "PALADIN.jpg"
temp_pharaoh_path = "./" + TEMP_IMG_DIR + "/" +  "PHARAOH.jpg"
temp_pmeiji_path = "./" + TEMP_IMG_DIR + "/" +  "PMEIJI.jpg"
temp_pumpkin_path = "./" + TEMP_IMG_DIR + "/" +  "PUMPKIN.jpg"
temp_sabo_path = "./" + TEMP_IMG_DIR + "/" +  "SABO.jpg"
temp_sai_path = "./" + TEMP_IMG_DIR + "/" +  "SAI.jpg"
temp_senkusha_path = "./" + TEMP_IMG_DIR + "/" +  "SENKUSHA.jpg"
temp_soko_path = "./" + TEMP_IMG_DIR + "/" +  "SOKO.jpg"
temp_soul_path = "./" + TEMP_IMG_DIR + "/" +  "SOUL.jpg"
temp_syudo_path = "./" + TEMP_IMG_DIR + "/" +  "SYUDO.jpg"
temp_temple_path = "./" + TEMP_IMG_DIR + "/" +  "TEMPLE.jpg"
temp_toteki_path = "./" + TEMP_IMG_DIR + "/" +  "TOTEKI.jpg"
temp_totem_path = "./" + TEMP_IMG_DIR + "/" +  "TOTEM.jpg"
temp_tozoku_path = "./" + TEMP_IMG_DIR + "/" +  "TOZOKU.jpg"
temp_varistor_path = "./" + TEMP_IMG_DIR + "/" +  "VARISTOR.jpg"
temp_viking_path = "./" + TEMP_IMG_DIR + "/" +  "VIKING.jpg"
temp_voodoo_path = "./" + TEMP_IMG_DIR + "/" +  "VOODOO.jpg"
temp_yari_path = "./" + TEMP_IMG_DIR + "/" +  "YARI.jpg"
temp_yasha_path = "./" + TEMP_IMG_DIR + "/" +  "YASHA.jpg"
temp_yumi_path = "./" + TEMP_IMG_DIR + "/" +  "YUMI.jpg"
temp_zombie_path = "./" + TEMP_IMG_DIR + "/" +  "ZOMBIE.jpg"

def matching(src_img, temp_img, out_img, color, char_name):
    width, height = temp_img.shape[::-1]

    #テンプレートマッチングの実行(比較方法cv2.TM_CCORR_NORMED)
    result = cv2.matchTemplate(src_img, temp_img, cv2.TM_CCORR_NORMED)
    loc = numpy.where (result > 0.98)
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
    temp_bakudan = cv2.imread(temp_bakudan_path, 0)
    temp_bear = cv2.imread(temp_bear_path, 0)
    temp_capapult = cv2.imread(temp_capapult_path, 0)
    temp_daemon = cv2.imread(temp_daemon_path, 0)
    temp_defender = cv2.imread(temp_defender_path, 0)
    temp_fmeiji = cv2.imread(temp_fmeiji_path, 0)
    temp_fune = cv2.imread(temp_fune_path, 0)
    temp_gakusha = cv2.imread(temp_gakusha_path, 0)
    temp_goburin = cv2.imread(temp_goburin_path, 0)
    temp_gorem = cv2.imread(temp_gorem_path, 0)
    temp_hohe = cv2.imread(temp_hohe_path, 0)
    temp_hone = cv2.imread(temp_hone_path, 0)
    temp_hyoketu = cv2.imread(temp_hyoketu_path, 0)
    temp_icemeiji = cv2.imread(temp_icemeiji_path, 0)
    temp_iwa = cv2.imread(temp_iwa_path, 0)
    temp_jigoku = cv2.imread(temp_jigoku_path, 0)
    temp_junrei = cv2.imread(temp_junrei_path, 0)
    temp_kamikaze = cv2.imread(temp_kamikaze_path, 0)
    temp_kemono = cv2.imread(temp_kemono_path, 0)
    temp_kenshi = cv2.imread(temp_kenshi_path, 0)
    temp_majo = cv2.imread(temp_majo_path, 0)
    temp_minarai = cv2.imread(temp_minarai_path, 0)
    temp_necro = cv2.imread(temp_necro_path, 0)
    temp_ogre = cv2.imread(temp_ogre_path, 0)
    temp_paladin = cv2.imread(temp_paladin_path, 0)
    temp_pharaoh = cv2.imread(temp_pharaoh_path, 0)
    temp_pmeiji = cv2.imread(temp_pmeiji_path, 0)
    temp_pumpkin = cv2.imread(temp_pumpkin_path, 0)
    temp_sabo = cv2.imread(temp_sabo_path, 0)
    temp_sai = cv2.imread(temp_sai_path, 0)
    temp_senkusha = cv2.imread(temp_senkusha_path, 0)
    temp_soko = cv2.imread(temp_soko_path, 0)
    temp_soul = cv2.imread(temp_soul_path, 0)
    temp_syudo = cv2.imread(temp_syudo_path, 0)
    temp_temple = cv2.imread(temp_temple_path, 0)
    temp_toteki = cv2.imread(temp_toteki_path, 0)
    temp_totem = cv2.imread(temp_totem_path, 0)
    temp_tozoku = cv2.imread(temp_tozoku_path, 0)
    temp_varistor = cv2.imread(temp_varistor_path, 0)
    temp_viking = cv2.imread(temp_viking_path, 0)
    temp_voodoo = cv2.imread(temp_voodoo_path, 0)
    temp_yari = cv2.imread(temp_yari_path, 0)
    temp_yasha = cv2.imread(temp_yasha_path, 0)
    temp_yumi = cv2.imread(temp_yumi_path, 0)
    temp_zombie = cv2.imread(temp_zombie_path, 0)

    matching(img_gray, temp_assassin ,img, (255, 255, 255), "ア")
    matching(img_gray, temp_bakudan ,img, (255, 255, 255), "爆")
    matching(img_gray, temp_bear ,img, (255, 255, 255), "熊")
    matching(img_gray, temp_capapult ,img, (255, 255, 255), "石")
    matching(img_gray, temp_daemon ,img, (255, 255, 255), "デ")
    matching(img_gray, temp_defender ,img, (255, 255, 255), "壁")
    matching(img_gray, temp_fmeiji ,img, (255, 255, 255), "火")
    matching(img_gray, temp_fune ,img, (255, 255, 255), "船")
    matching(img_gray, temp_gakusha ,img, (255, 255, 255), "学")
    matching(img_gray, temp_goburin ,img, (255, 255, 255), "砲")
    matching(img_gray, temp_gorem ,img, (255, 255, 255), "ゴ")
    matching(img_gray, temp_hohe ,img, (255, 255, 255), "歩")
    matching(img_gray, temp_hone ,img, (255, 255, 255), "骨")
    matching(img_gray, temp_hyoketu ,img, (255, 255, 255), "氷")
    matching(img_gray, temp_icemeiji ,img, (255, 255, 255), "凍")
    matching(img_gray, temp_iwa ,img, (255, 255, 255), "岩")
    matching(img_gray, temp_jigoku ,img, (255, 255, 255), "獄")
    matching(img_gray, temp_junrei ,img, (255, 255, 255), "巡")
    matching(img_gray, temp_kamikaze ,img, (255, 255, 255), "攻")
    matching(img_gray, temp_kemono ,img, (255, 255, 255), "獣")
    matching(img_gray, temp_kenshi ,img, (255, 255, 255), "剣")
    matching(img_gray, temp_majo ,img, (255, 255, 255), "魔")
    matching(img_gray, temp_minarai ,img, (255, 255, 255), "習")
    matching(img_gray, temp_necro ,img, (255, 255, 255), "ネ")
    matching(img_gray, temp_ogre ,img, (255, 255, 255), "オ")
    matching(img_gray, temp_paladin ,img, (255, 255, 255), "パ")
    matching(img_gray, temp_pharaoh ,img, (255, 255, 255), "神")
    matching(img_gray, temp_pmeiji ,img, (255, 255, 255), "プ")
    matching(img_gray, temp_pumpkin ,img, (255, 255, 255), "瓜")
    matching(img_gray, temp_sabo ,img, (255, 255, 255), "サ")
    matching(img_gray, temp_sai ,img, (255, 255, 255), "突")
    matching(img_gray, temp_senkusha ,img, (255, 255, 255), "駆")
    matching(img_gray, temp_soko ,img, (255, 255, 255), "装")
    matching(img_gray, temp_soul ,img, (255, 255, 255), "ソ")
    matching(img_gray, temp_syudo ,img, (255, 255, 255), "修")
    matching(img_gray, temp_temple ,img, (255, 255, 255), "テ")
    matching(img_gray, temp_toteki ,img, (255, 255, 255), "投")
    matching(img_gray, temp_totem ,img, (255, 255, 255), "ト")
    matching(img_gray, temp_tozoku ,img, (255, 255, 255), "盗")
    matching(img_gray, temp_varistor ,img, (255, 255, 255), "ヴ")
    matching(img_gray, temp_viking ,img, (255, 255, 255), "バ")
    matching(img_gray, temp_voodoo ,img, (255, 255, 255), "ブ")
    matching(img_gray, temp_yari ,img, (255, 255, 255), "槍")
    matching(img_gray, temp_yasha ,img, (255, 255, 255), "夜")
    matching(img_gray, temp_yumi ,img, (255, 255, 255), "弓")
    matching(img_gray, temp_zombie ,img, (255, 255, 255), "ゾ")



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

    formation_7x7.output_formation()


if __name__ == "__main__":

    source_img_path = sys.argv[1]
    main()
    #print(cv2.__file__)