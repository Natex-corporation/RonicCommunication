import webbrowser
import time

while(True):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    url1 = "https://www.facebook.com/"
    url2 = "https://www.instagram.com/"
    url3 = "https://discord.com/channels/@me"
    url = [url2, url1, url3]

#webbrowser.get(chrome_path).open("https://www.google.com/")
    print ("am here0")

    for i in url:
        webbrowser.get(chrome_path).open_new(i)
        print ("am here1")
        time.sleep(1)

    time.sleep(86400)