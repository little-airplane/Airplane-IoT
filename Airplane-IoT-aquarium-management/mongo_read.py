import pymongo
import BlynkLib
import datetime.datetime as datetime
temp = []
tianjiayushi = False
blynk = BlynkLib.Blynk()
db = pymongo.MongoClient("mongodb://47.47.47.46:27017/")["IoT"]
ffu = db["FishFeendingUse"]
WCT = db["WCTofAquarium"]
for i in ffu.find():
    temp.append(i)
ffutime = temp[len(temp) - 1]["time"]
ffunum = temp[len(temp) - 1]["rem"]
temp = []
for i in WCT.find():
    temp.append(i)
WCTtime = temp[len(temp) - 1]["time"]
temp = []

@blynk.VIRTUAL_WRITE(86)
def yijiashui(value):
    if value[0] == "1":
        WCT.insert_one({"time":datetime()})

@blynk.VIRTUAL_WRITE(89)
def yijiashui(value):
    if value[0] == "1":
        tianjiayushi = True

@blynk.VIRTUAL_WRITE(88)
def yijiashi(value):
    if tianjiayushi == True:
        global ffunum
        ffu.insert_one({"use" : false, "num" : value, "rem" : ffunum + value, "time" : datetime()})
        tianjiayushi = False

#导入轮子
def is_leap_year(year):
    """
    判断当前年份是不是闰年，年份公元后，且不是过大年份
    :param year: 年份
    :return: True 闰年， False 平年
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False
def validate_param(year, month, day):
    """
    参数校验
    :param year: 年份
    :param month: 月份
    :param day: 日期
    :return: error_msg 错误信息，没有为空
    """
    error_msg = u''
    if not isinstance(year, int) or year < 1:
        error_msg = u'年份输入不符合要求'
    if not isinstance(month, int) or month < 1 or month > 12:
        error_msg = u'月份输入不符合要求'
    if not isinstance(day, int) or day < 1 \
            or (month in month_of_days31 and day > 31) \
            or (month in month_of_days30 and day > 30) \
            or (month == feb_month and (day > 29 if is_leap_year(year) else day > 28)):
        error_msg = u'日期输入不符合要求'
    return error_msg
def get_day_of_year(year, month, day):
    """
    获取一个日期在这一年中的第几天
    :param year: 年份
    :param month: 月份
    :param day: 日期
    :return: 在这一年中的第几天
    """
    # 参数校验
    error_msg = validate_param(year, month, day)
    if error_msg:
        return error_msg

    if month == 1:
        return day

    if month == 2:
        return day + 31

    days_of_31_num = 0
    days_of_30_num = 0
    # 31天月份数
    for days_of_31 in month_of_days31:
        if days_of_31 < month:
            days_of_31_num += 1
        else:
            break

    # 30天月份数
    for days_of_30 in month_of_days30:
        if days_of_30 < month:
            days_of_30_num += 1
        else:
            break

    return days_of_31_num * 31 + days_of_30_num * 30 + (29 if is_leap_year(year) else 28) + day

while True:
    for i in ffu.find():
        temp.append(i)
    if temp[len(temp) - 1]["time"] != ffutime:
        ffutime = temp[len(temp) - 1]["time"]
        send = str(ffutime).split()[1].split(":")
        send = int(send[0] + "." + send[1])
        blynk.virtual_write(83, send)
    if temp[len(temp) - 1]["rem"] != ffunum:
        ffunum = temp[len(temp) - 1]["rem"]
        send = ffunum
        blynk.virtual_write(84, send)
    temp = []
    for i in WCT.find():
        temp.append(i)
    if temp[len(temp) - 1]["time"]:
        WCTtime = temp[len(temp) - 1]["time"]
        send = str(WCTtime).split()[0].split("-")
        temp = get_day_of_year(send[0], send[1], send[2])
        dt = str(datetime()).split()[0].split("-")
        nowday = get_day_of_year(dt[0], dt[1], dt[2])
        if nowday - temp <= 1:
            if is_leap_year(send[0]):
                send = nowday + 366 - temp
            else:
                send = nowday + 365 - temp
        else:
            send = nowday - temp
        blynk.virtual_write(85, send)
    temp = []
