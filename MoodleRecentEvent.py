import requests
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import lxml

session = requests.Session()
url_page = 'https://ummoodle.um.edu.mo/my/'

cookieFile = open('Cookie.txt','r')
Cookie = cookieFile.read()

header2 = {
    'Referer': 'https://websso.um.edu.mo/adfs/ls/?SAMLRequest=jVJdSwMxEPwrR957uYtV29AWqkUs+FFs9cEX2Uu2NnBJzmzix7/3elWsoCLkIWxmdmYnOyKwdSOnKW7cDT4lpJi92tqR7B7GLAUnPZAh6cAiyajkcnp5IUVeyCb46JWv2R7lbwYQYYjGO5bNZ2P2IEooKg1Hqj/oCxiCFgIHh2V5fKyHelAIdVDBYaUEapbdYaCWOWZto5ZOlHDuKIKLbakQolcW7VkVA9kfyuLgnmWzdhrjIHasTYwNSc5fsCLyebI56pRbz0GvidfEWTb9dHfqHSWLYYnh2Si8vbn44idrvdc17ndo0+Pb4QWnZnfpgaK82TQ/wFm2+MjtxDht3OPfkVU7EMnz1WrRW1wvV2wy2mrILoIw+bcxixE0RNj6GvH9FqPdFly14vPZwtdGvWVnPliIv3sr87KrGN1bd1CZHDWozNpsf2ta1/7lNCBEHLMYEjI+2Yl+37bJOw==&RelayState=https://ummoodle.um.edu.mo/my/&SigAlg=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256&Signature=XrxD9BXwUipRw/bzLBSHnhlUYfU2jYa67lbvpyq4g+xuVozZhJ2hF/zoA+qY3p4mD41XdxriNHOUmqcC5Xp3Y6r5h5M4519FQaUpxeL8vzDiBlwkKOzC0TsNz9bfRHV4X3zL1xDWslpnmsfebfdQl2VYs7t7Bvd4FujPvKvfFc69+em0DuVXUrLrfUshy4sBaHlzOsiUaTrxV796pq0ERKP8W0ylUu3CLK6UoTPyBOFn41flTPRlvfAKZRo1+vgnlbSDI6d3crJhL28x3s/5eyO9iDGQsSsxqoU/WMTrCDukdWeJreda6JUnKqJXkhfA9oKZTpmos1Gs4oOLGqGXsw==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34',
    'host' : 'ummoodle.um.edu.mo',
    'Cookie': Cookie
}


def mail(title, content):
    mail_title = title
    mail_content = content
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1419009509@qq.com"  # 用户名
    mail_pass = "spcfscjowcefbaag"  # 口令

    receivers = 'skititingChen@gmail.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    msg = MIMEMultipart()
    msg['Subject'] = Header(mail_title, 'utf-8')
    msg['From'] = mail_user
    msg['To'] = receivers

    # main body
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    smtp = smtplib.SMTP_SSL(mail_host)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(mail_user, "1419009509@qq.com", msg.as_string())
    smtp.quit()

#获取近期事件
try:
    page = session.get(url_page, headers=header2)
    soup = BeautifulSoup(page.text, 'lxml')
    eventIn = soup.find_all(class_='event')

    a=''
    for p in eventIn:
        print(p.text)
        a = a + p.text
    print(a)

    mail('Event Mention',a)
    time.sleep(86400)
except:
    mail('Error Occured','Moodle Recent Event')