def log_in(account, password):

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import time
    # 使用 Chromium 的 WebDriver
    s = Service('/usr/lib/chromium-browser/chromedriver')
    driver = webdriver.Chrome(service=s)

    # 開啟 Portal 首頁
    driver.get('https://portalx.yzu.edu.tw/PortalSocialVB/Login.aspx')

    #time.sleep(1)

    #email = driver.find_element_by_name('Txt_UserID')
    #password = driver.find_element_by_name('Txt_Password')
    acc_pos = driver.find_element("name", "Txt_UserID")
    pw_pos = driver.find_element("name", "Txt_Password")

    acc_pos.send_keys(account)
    pw_pos.send_keys(password)

    #button = driver.find_element_by_class_name('ibnSubmit')
    button = driver.find_element("name", "ibnSubmit")
    button.click()
    print("------------------------")
    input('Please press enter to close...')
    # 關閉瀏覽器
    # driver.close()