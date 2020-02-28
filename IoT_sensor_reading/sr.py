#import Adafruit_DHT
import blynklib
import BlynkLib
blynk = BlynkLib.Blynk()
#import pymongo
#import time

#sensor = Adafruit_DHT.DHT11
'''
db = pymongo.MongoClient("mongodb://47.47.47.46:27017/")["IoT"]
tempdb = db["temp_inside"]
temphourdb = db["time_inside_day"]
tempdaydb = db["time_inside_month"]
humidb = db["humi_inside"]
humihourdb = db["humi_inside_day"]
humidaydb = db["humi_inside_month"]
'''

GPIO = 5

while True:
    #temp, humi = Adafruit_DHT.read_retry(sensor, GPIO)
    #temp, humi = (47, 47)
    temp = 47
    humi = 47
    #print(temp)
    #print(humi)
    #if temp is not None and humi is not None:
       # print("Temp is " +str temp + " and humi is " + humi + ".")
    blynk.virtual_write(76, temp)
    blynk.virtual_write(77, humi)

    '''
    nowtime = time.asctime(time.localtime(time.time())).split()[2].split(":")
     if int(nowtime[2]) == 0 or int(nowtime[2]) == 1 or int(nowtime[2]) == 59:
        tempdb.insert_one({"temp" : temp, "time" : int(nowtime[1])})
        humidb.insert_one({"humi" : humi, "time" : int(nowtime[1])})
        if int(nowtime[1]) == 0:
            temphourdb.insert_one({"temp" : temp, "time" : int(nowtime[0])})
            humihourdb.insert_one({"humi" : humi, "time" : int(nowtime[0])})
            if int(nowtime[0]) == 0:
                tempdb.insert_one({"temp" : temp, "time" : int(time.asctime(time.localtime(time.time())).split()[1])})
                humidb.insert_one({"humi" : humi, "time" : })
    '''
    #else:
     #   print("ERROR:DON'T GET DATA")
     #   exit(1)
