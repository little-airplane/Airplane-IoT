import blynklib
blynk = blynklib.Blynk()
import socket
s = socket.socket()
host = socket.gethostname()
port = 15001
s.bind((host, port))
s.listen(1)
sc, scaddr = s.accept()
import time

@blynk.VIRTUAL_WRITE(27)
def ystwlps(value):
    global ystwlpsg
    ystwlpsg = value

@blynk.VIRTUAL_WRITE(28)
def wysj1(value):
    time = value[0]
    hour = int(str(time / 3600).split(".")[0])
    min = int(str(time % 3600 / 60).split(".")[0])
    global wysj1g
    wysj1g = (hour, min)

@blynk.VIRTUAL_WRITE(29)
def wysj2(value):
    time = value[0]
    hour = int(str(time / 3600).split(".")[0])
    min = int(str(time % 3600 / 60).split(".")[0])
    global wysj2g
    wysj2g = (hour, min)

@blynk.VIRTUAL_WRITE(30)
def wysj3(value):
    time = value[0]
    hour = int(str(time / 3600).split(".")[0])
    min = int(str(time % 3600 / 60).split(".")[0])
    global wysj3g
    wysj3g = (hour, min)

@blynk.VIRTUAL_WRITE(32)
def jysj1(value):
    time = value[0]
    hour = int(str(time / 3600).split(".")[0])
    min = int(str(time % 3600 / 60).split(".")[0])
    global jysj1g
    jysj1g = ((hour, min), value[1] - value[0])

@blynk.VIRTUAL_WRITE(33)
def jysj2(value):
    time = value[0]
    hour = int(str(time / 3600).split(".")[0])
    min = int(str(time % 3600 / 60).split(".")[0])
    global jysj2g
    jysj2g = ((hour, min), value[1] - value[0])

@blynk.VIRTUAL_WRITE(0)
def weiyu(value):
    if value[0] == "1":
        SendCmd_Ws()

def CheckTime_Om(nowtime):
    if nowtime == jysj1g[0]:
        SendCmd_Om(nowtime, jysj1g[0])
    elif nowtime == jysj2g[0]:
        SendCmd_Om(nowtime, jysj2g[0])

def CheckTime_Ws(nowtime):
    if nowtime == jysj1g or jysj2g or jysj3g:
        SendCmd_Om(nowtime)

def SendCmd_Om(exittime):
    sc.send("o")
    time.sleep(exittime)
    sc.send("x")

def SendCmd_Ws():
    sc.send(ystwlpsg)

def main():
    while True:
        nowtime = time.localtime(time.time())
        nowtime = (nowtime.tm_hour, nowtime.tm_min)
        CheckTime_Om(nowtime)
        CheckTime_Ws(nowtime)

if __name__ == '__main__':
    main()
