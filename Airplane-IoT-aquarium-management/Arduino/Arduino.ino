/*
#include <ESP8266WiFi.h>
#define SSID "CMCC-2018"
#define PASSWORD "PWD"
#define HOST_NAME "192.168.0.100"
#define HOST_PORT (15001)
*/
int oxy = 2;
int food = 3;
int inByte;
void setup() {
    Serial.begin(115200);
    pinMode(oxy, OUTPUT);
    pinMode(food, OUTPUT);
    //Serial.print('AT+CWJAP="CMCC-2018", "PWD"');
    //Serial.print("AT+CIPMODE=1");
    //Serial.print('AT+CIPSTART="TCP", "192.168.0.100", 15001')
}
void loop() 
{
    if (Serial.available() > 0)
    {
        inByte = Serial.read();
        if (inByte == '5')
        {
            //转一圈
            digitalWrite(food, LOW);
            delay(1000);
            digitalWrite(food, HIGH);
        }
        if (inByte == '6')
        {
            //转两圈
            digitalWrite(food, LOW);
            delay(2000);
            digitalWrite(food, HIGH);
        }
        if (inByte == '7')
        {
            //转三圈
            digitalWrite(food, LOW);
            delay(3000);
            digitalWrite(food, HIGH);
        }
        if (inByte == '8')
        {
            //转四圈
            digitalWrite(food, LOW);
            delay(4000);
            digitalWrite(food, HIGH);
        }
        if (inByte == '9')
        {
            //转五圈
            digitalWrite(food, LOW);
            delay(5000);
            digitalWrite(food, HIGH);
        }
        if (inByte == 'o')
        {
            digitalWrite(oxy, LOW); //开始加氧
        }
        if (inByte == 'x') 
        {
            digitalWrite(oxy, HIGH); //停止加氧
        }
    }
}