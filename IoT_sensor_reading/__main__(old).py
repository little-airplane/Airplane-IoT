import serial
from time import sleep
import time
import sys
import pymongo
import datetime
whileexit = True
db_con = pymongo.MongoClient("mongodb://localhost:27017")
db = db_con["IoT"]
while whileexit:
    comport = input("请输入传感器集成器的串口号：")
    try:
        bps = 9500
        com_connect = serial.Serial(comport, bps)
        whileexit = False
    except:
        print("出错了！请重新连接！")

loginsuesssheet = db["sensor_login"]
print("成功连接到" + comport)
print("正在检查此设备是否为传感器集成器")
com_connect.write("TestIfCGQModule".encode("gbk"))
print("验证信息已发送至串口设备：" + comport)
readline = com_connect.readline()
if readline != "+Ok.IAm.":
    readline = com_connect.readline()
    print("第一次验证失败")
    if readline != "+Ok.IAm.":
        print("第二次验证开始...")
        sleep(2)
        readline = com_connect.readline()
        if readline != "+Ok.IAm.":
            print("此设备不是传感器集成器！或者该设备软件或硬件损坏")
            loginsuesssheet.insert_one({"host" : "localhost", "port" : comport, "time" : time.strftime('%Y-%m-%d %H:%M:%S'), "suess" : False})
            print("已自动退出")
            sys.exit()
print("经验证，" + comport + "是合法的传感器集成器")
loginsuesssheet.insert_one({"host" : "localhost", "port" : comport, "time" : datetime.datetime(), "suess" : True})
tempbase = db["DHT11Temp"]
temp = 0
humibase = db["DHT11Humi"]
humi = 0
sunbase = db["Sun"]
sun = 0
while True:
    info = com_connect.readline()
    if "DHT11" in info:
        if "Temp" in info:
            temp = info.split(":")[2]
            if time.time() % (60 ** 1) == 0:
                tempbase.insert_one({"host" : "localhost", "port" : comport, "time" : datetime.datetime(), "Temp" : temp})
        elif "Humi" in info:
            humi = info.split(":")[2]
            if time.time() % (60 ** 1) == 0:
                humibase.insert_one({"host" : "localhost", "port" : comport, "time" : datetime.datetime(), "Humi" : humi})
    elif "sun" in info:
        sun = info.split(":")[1]
        if time.time() % (60 ** 1) == 0:
            sunbase.insert_one({"host" : "localhost", "port" : comport, "time" : datetime.datetime(), "Sun" : sun})
