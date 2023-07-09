import shot
import face_recog
import ubidots_http_send
import mail
import web
import ubidots_http_get
import time
from gtts import gTTS
import os
import RPi.GPIO as GPIO
import time
import threading

def speaker(s):
    tts = gTTS(text=s, lang='zh-TW')
    tts.save('tip.mp3')
    os.system('omxplayer -o local -p tip.mp3 > /dev/null 2>&1')

LED_PIN = [12, 33, 32]
GPIO.setmode(GPIO.BOARD)
for i in range(3):
    GPIO.setup(LED_PIN[i], GPIO.OUT)
    GPIO.output(LED_PIN[i], GPIO.LOW)

#抓值
#登入介面
try:
    while True:
        database = ubidots_http_get.get_vars()
        count = database['count']
        users = database['results']

        names = list()
        accounts = list()
        passwords = list()
        gmails = list()

        for i in range(0, count):
            names.append(users[i]['name'])
            accounts.append(users[i]['last_value']['context']['account'])
            passwords.append(users[i]['last_value']['context']['password'])
            gmails.append(users[i]['last_value']['context']['gmail'])
            
        print("\n------------------------")
        print("請選擇您要登入的帳號:")
        print(0, '離開')
        for i in range(1, count + 1):
            print(i, accounts[i - 1])
        print(count + 1, '新增/編輯資料')
        index = int(input())
        print("------------------------")
        
        if not index:
            exit()
        elif index == count + 1:
            print("請輸入名字")
            add_name = input()
            print("\n請輸入帳號")
            add_acc = input()
            print("\n請輸入密碼")
            add_pw = input()
            print("\n請輸入email")
            add_gmail = input()
            #cloud.send(add_name, add_acc, add_pw, add_gmail)
            t_cloud = threading.Thread(target = ubidots_http_send.send, args = (add_name, add_acc, add_pw, add_gmail,))
            t_cloud.start()
            shot.shot(add_name)
        elif index not in range(1, count + 1):
            continue
        else:
            break


    while True:
        print('請輸入密碼')
        pw = input()
        if pw != passwords[index - 1]:
            print('密碼錯誤！')
            print("------------------------")
            speaker("密碼錯誤")
        else:
            break
        
#Face ID
    print("------------------------")
    s = '身份辨識中，請稍後...'
    print(s)
    GPIO.output(LED_PIN[1], GPIO.HIGH)
    t_speak = threading.Thread(target = speaker, args = (s,))
    t_speak.start()
    name = face_recog.faceRecog()
    #print(name)
    cor = name == names[index - 1]
    t_mail = threading.Thread(target = mail.send_mail, args = (gmails[index - 1], cor,))
    t_mail.start()
    #mail.send_mail(gmails[index - 1], cor)

#自動登入
    if not cor:
        print("------------------------")
        s = '身分辨識失敗！逮到你囉！'
        print(s)
        GPIO.output(LED_PIN[1], GPIO.LOW)
        GPIO.output(LED_PIN[0], GPIO.HIGH)
        t_speak = threading.Thread(target = speaker, args = (s,))
        t_speak.start()
        t_mail.join()
        t_speak.join()
        print("------------------------")
        input('Press enter to close...')
    else:
        print("------------------------")
        s = '身分辨識成功！'
        print(s)
        GPIO.output(LED_PIN[1], GPIO.LOW)
        GPIO.output(LED_PIN[2], GPIO.HIGH)
        t_speak = threading.Thread(target = speaker, args = (s,))
        t_speak.start()
        web.log_in(accounts[index - 1], passwords[index - 1])
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()