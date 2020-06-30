from qiniu.auth import QiniuMacAuth
from qiniu import Sms
import random

access_key = 't6NtVqaJUrGvx4CYK9qLUyVHtjMiJB4XqoyMmQIH'
secret_key = '0FunAzOYpwsNxscIRVocC7AGv8yvn7YPT7Tn8C5G'
from ext import redis
def generate_code():
    captcha = ""
    for i in range(4):
        captcha += str(random.randint(0, 9))
    print(captcha)
    return captcha

def send_code(phone,code):
    # 初始化Auth状态
    q = QiniuMacAuth(access_key, secret_key)

    # 初始化Sms
    sms = Sms(q)


    # sms.createSignature("doyd1238")
    req, info = sms.sendMessage("1209711903257923584", [phone], {"code": code})
    print(req)
    print(info)
    print(info.exception)



    return info.status_code == 200
