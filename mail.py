def send_mail(gmail, correction):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from pathlib import Path
    import cv2
    import smtplib

    cam = cv2.VideoCapture(0)

    ret, image = cam.read()
    #cv2.imshow('preview',image)
    cv2.waitKey(0)
    cv2.imwrite('/home/pi/Desktop/IoT_final_proj/Face-Recognition-Raspberry-pi/gmail_photo/photo.jpg', image)

    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["from"] = "john03690248@gmail.com"  #寄件者
    content["to"] = gmail #收件者
    
    if not correction:
        content["subject"] = "警告！有不明人士登入您的帳號！"  #郵件標題
        content.attach(MIMEText("警告！有不明人士登入您的帳號！"))  #郵件內容
        content.attach(MIMEImage(Path("/home/pi/Desktop/IoT_final_proj/Face-Recognition-Raspberry-pi/gmail_photo/photo.jpg").read_bytes()))  # 郵件圖片內容
    else:
        content["subject"] = "已成功登入！"  #郵件標題
        content.attach(MIMEText("已成功登入！"))  #郵件內容

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("john03690248@gmail.com", "zdzephjwzjctcjzp")  # 登入寄件者gmail #zdzephjwzjctcjzp
            smtp.send_message(content)  # 寄送郵件
            #print("Complete!")
        except Exception as e:
            print("Error message: ", e)
            
    cam.release()
    cv2.destroyAllWindows()