import mediapipe as mp
import cv2
import numpy as np
import time
from pynput.keyboard import Key ,Controller
import webbrowser
import pyautogui  # screenshot
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from warnings import filterwarnings
from datetime import datetime


filterwarnings("ignore")

# Consts
handmarks = False
leftArea = 115
max_x, max_y = 398 +leftArea, 50
button = ""
onTime = True # time event
radius = 40  # circle radius
var_inits = False  # main finger checker
keyboard = Controller()
text = ""
counter_portf = 0
counter_coding = 0
counter_mail = 0
counter_selen = 0
counter_rock = 0
mails = ["mutkumese", "cinkirm999", "omerozler8", "spaci", "example"]


#  get buttons
def getTool(x):
    if x < 50 + leftArea:
        return "volumeUp"

    elif x< 100 + leftArea:
        return "volumeDown"

    elif x < 150 + leftArea:
        return "portfolio"

    elif x < 200 + leftArea:
        return "mail"

    elif x < 250 + leftArea:
        return "selenium"

    elif x < 300 + leftArea:
        return "screenshot"

    elif x < 350 + leftArea:
        return "coding"

    else:
        return "close"


def index_raised(yi, y9):
    if (y9 - yi) > 40:
        return True

    return False


hands = mp.solutions.hands
hand_landmark = hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6, max_num_hands=2)  # max_num_hands hand count
draw = mp.solutions.drawing_utils

tools = cv2.imread("buttons.png")
tools = tools.astype('uint8')

mask = np.ones((480, 640)) * 255
mask = mask.astype('uint8')

cap = cv2.VideoCapture(0)

while True:
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
    op = hand_landmark.process(rgb)


    if op.multi_hand_landmarks:

        if len(op.multi_hand_landmarks) == 2:
            text = "SELAM!"
        else: text = ""

        for i in op.multi_hand_landmarks:

            if handmarks:
                draw.draw_landmarks(frm, i, hands.HAND_CONNECTIONS)  # handmarks settings
            x, y = int(i.landmark[8].x * 640), int(i.landmark[8].y * 480)  # main finger position

            x4, y4 = int(i.landmark[4].x * 640), int(i.landmark[4].y * 480)
            x12, y12 = int(i.landmark[12].x * 640), int(i.landmark[12].y * 480)
            x3, y3 = int(i.landmark[3].x * 640), int(i.landmark[3].y * 480)
            x20, y20 = int(i.landmark[20].x * 640), int(i.landmark[20].y * 480)
            x11, y11 = int(i.landmark[11].x * 640), int(i.landmark[11].y * 480)
            x15, y15 = int(i.landmark[15].x * 640), int(i.landmark[15].y * 480)
            x5, y5 = int(i.landmark[5].x * 640), int(i.landmark[5].y * 480)


            if y4 < y and y5 < y12 and y5 < y20: # handmark selector
                time.sleep(0.1)
                handmarks = not handmarks

            if y < y4 and y < y3 and y < y20 and y < y12 and y4 > y12 and y4 > y20 and y4 > y and y4 > y3:
                text = "<3"

                print("kalp")
            else:
                if text == "<3":
                    text = ""
                elif len(op.multi_hand_landmarks) == 1:
                    text == ""

            cv2.putText(frm, text, (100 + leftArea, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 100), 4)

            if y < y12 and y20 < y12 and y20 < y4 and y11 > y5 and y15 > y5 and y3 > y4 and x4 > x: # rock selector
                if counter_rock == 0:
                    time.sleep(0.1)
                    webbrowser.open('https://www.youtube.com/watch?v=-qEla3eow3c&ab_channel=RockCollection')
                    counter_rock = 1
                print("rock")

            if x < max_x and y < max_y and x > leftArea:
                if onTime:
                    ctime = time.time()
                    onTime = False
                ptime = time.time()

                cv2.circle(frm, (x, y), radius, (0, 255, 255), 1)
                radius -= 1

                if (ptime - ctime) > 0.8:
                    button = getTool(x)
                    print("Secilen buton : ", button)
                    onTime = True
                    radius = 40

            else:
                onTime = True
                radius = 40

            if button == "volumeUp":
                if x < 50 + leftArea and y < 50:
                    keyboard.press(Key.media_volume_up)
                    keyboard.release(Key.media_volume_up)
                    time.sleep(0.01)

            elif button == "volumeDown":
                if x < 100 + leftArea and x > 50 + leftArea and y < 50:
                    keyboard.press(Key.media_volume_down)
                    keyboard.release(Key.media_volume_down)
                    time.sleep(0.01)

            elif button == "portfolio":
                if x < 150 + leftArea and x > 100 + leftArea and y < 50:
                    webbrowser.open('https://utku-mese.github.io/')
                    time.sleep(1)


            elif button == "mail":
                if counter_mail == 0:
                    os.system("start C:\\Users\\Utku\\Desktop\\Posta.lnk")
                    time.sleep(2)
                    for i in range(3):
                        keyboard.press(Key.tab)
                        keyboard.release(Key.tab)
                        time.sleep(0.5)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    time.sleep(1)
                    for i in mails:
                        pyautogui.typewrite(i)
                        pyautogui.hotkey("altright", "q")
                        pyautogui.typewrite("gmail.com;  ")

                    time.sleep(0.5)
                    for i in range(3):
                        keyboard.press(Key.tab)
                        keyboard.release(Key.tab)
                        time.sleep(0.5)
                    pyautogui.typewrite("Gunluk Borsa Analiziniz")
                    time.sleep(0.5)
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                    time.sleep(0.5)
                    with keyboard.pressed(Key.ctrl):
                        keyboard.press('a')
                        keyboard.release('a')
                        time.sleep(0.2)
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                    time.sleep(1)
                    pyautogui.write('''
	Klasik				4.405,39	4.447,51	4.476,81	4.518,93	
	Fibonacci			4.447,51	4.474,79	4.491,65	4.518,93	
	Camarilla			4.486,46	4.493,01	4.499,55	4.518,93	
	Woodie				4.398,97	4.444,30	4.470,39	4.515,72	
	Demark				4.518,93	4.493,01	4.462,16	4.511,60

	Temel Analiz 
	
	Bist100 endeksi gunu yuzde 1,15 dususle 5261,41 seviyesinden kapatirken sirketlerin 
	yuzde 51’inin gunu negatif olarak sonlandirdigini izlemekteyiz. 
	Burada endeksin yukselisine puan bazli en fazla destek veren sirketler ISCTR, BIMAS, TOASO ve
	ODAS olurken, yukselisi sinirlandiran hatta negatif bolgeye ceken sirketlerse THYAO, EREGL ve 
	SASA olarak kaydedilmistir. Sirket fiyat degisimlerinden sektorlere gectigimizde gunluk bazda en
	iyi performans sergileyenleri SPOR ve GIDA ICECEK olurken gunun zayif halkalari MADENCILIK ve 
	TAS TOPRAK olarak kaydedilmistir.\n
					''', interval = 0.0000001)
                    time.sleep(0.1)
                    pyautogui.typewrite("""
               XU100, 5350 seviyesine ulasmasi ardindan gerceklestirdigi realizasyon ile dikkat cekerken ilgili gerilemeye ragmen
               22 ile 55 gunluk ussel hareketli ortalamalarin (5030 – 5125 bolgesi) uzerindeki fiyatlama reaksiyonu ile psikolojik
               5000 seviyesi uzerinde yukselisine devam etme dusuncesini gundeminde tutmayi surdurmektedir. Endeksin 5705 zirvesine
               dogru yeni bir yolcul uk yapma beklentilerinin on planda yer aldigi bir ortamda ilgili gelismeyi destekleyecek
                haber akislarinin hedefe ulasma surecini kisaltacagini, desteklemeyecek haber akislari ile de trend icin onemli
               olarak izah ettigimiz seviyelerde destek gorevi gorup gormeyeceginin sorgulanacagini belirtebiliriz.
               Kisa vadeli olarak 5705 oncesindeki ara direnc seviyeleri 5350 basta olmak uzere 5415 ve 5500 olarak kaydedilmistir.
            
            
               Gunun onemli Seviyesi: 5125
            
               Destekler: 5195 – 5125 – 5030 – 4950  
               Direncler: 5350 – 5415 – 5500 – 5570
                    """, interval = 0.0000001)
                    time.sleep(1)
                    counter_mail += 1


            elif button == "selenium":
                if counter_selen == 0:
                    driver = webdriver.Chrome(r"C:\Users\Utku\Downloads\chromedriver_win32\chromedriver.exe")
                    driver.set_window_size(1150, 540)
                    driver.set_window_position(0, 0)
                    driver.get("https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx")

                    table = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0"]')

                    rows = table.find_elements(By.TAG_NAME, "tr")

                    file = open("C:\\Users\\Utku\\Desktop\\Proje\\Web-Data\\hisse_senedi_bilgileri.txt", "w")
                    file.write(f"VERİ TARİHİ: {datetime.now()}\n")
                    file.write("\n")

                    for row in rows:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        if len(cells) >= 5:
                            hisse_adi = cells[0].text
                            hisse_fiyati = cells[1].text
                            hisse_degisim = cells[3].text
                            hisse_hacim = cells[4].text

                            print(f"Hisse Adı: {hisse_adi}")
                            print(f"Hisse Fiyatı: {hisse_fiyati}")
                            print(f"Değişim: {hisse_degisim}")
                            print(f"Hacim: {hisse_hacim}")
                            print("")

                            file.write(f"Hisse Adi: {hisse_adi}\n")
                            file.write(f"Hisse Fiyati: {hisse_fiyati}\n")
                            file.write(f"Degisim: {hisse_degisim}\n")
                            file.write(f"Hacim: {hisse_hacim}\n")
                            file.write("\n")

                    file.close()

                    driver.quit()
                    os.startfile(r"C:\Users\Utku\Desktop\Proje\Web-Data")
                    counter_selen += 1

            elif button == "screenshot":
                if counter_portf == 0:
                    myScreenshot = pyautogui.screenshot()
                    os.startfile(r"C:\Users\Utku\Desktop\Proje\Screenshots")
                    myScreenshot.save(r'C:\Users\Utku\Desktop\Proje\Screenshots\screenshot.png')
                    counter_portf += 1;

            elif button == "coding":
                if counter_coding == 0:
                    os.system("start C:\\Users\\Utku\\AppData\\Local\\Programs\\MicrosoftVSCode\\Code.exe")
                    time.sleep(0.5)
                    os.system("start C:\\Users\\Utku\\Desktop\\Spotify.lnk")
                    time.sleep(2)
                    for i in range(2):
                        keyboard.press(Key.tab)
                        keyboard.release(Key.tab)
                        time.sleep(0.5)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    counter_coding += 1

            elif button == "close":
                if x < 398 + leftArea and x > 350 + leftArea and y < 50:
                    cv2.destroyAllWindows()
                    cap.release()
                    break

    op = cv2.bitwise_and(frm, frm, mask=mask)
    frm[:, :, 1] = op[:, :, 1]
    frm[:, :, 2] = op[:, :, 2]

    frm[:max_y, leftArea:max_x] = cv2.addWeighted(tools, 0.7, frm[:max_y, leftArea:max_x], 0.3, 0)

    cv2.imshow("hand app", frm)

    if cv2.waitKey(1) == 27:  # press esc: close
        cv2.destroyAllWindows()
        cap.release()
        break
