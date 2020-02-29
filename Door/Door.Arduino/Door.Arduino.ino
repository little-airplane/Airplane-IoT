int gms = 2;
int bell = 3;
int human = 4;
int belltest = 0;
void setup()
{
    Serial.begin(115200);
    pinMode(gms, INPUT);
    pinMode(bell, INPUT);
    pinMode(human, INPUT);
}
void loop()
{
    if (digitalRead(gms) == HIGH)
    {
        Serial.print("DOOR:CLOSE")
    }
    if (digitalRead(gms) == LOW)
    {
        Serial.print("DOOR:OPEN")
    }
    if (digitalRead(gms) == HIGH and belltest == 0)
    {
        Serial.print("DOOR:CLOSE")
        int belltest = 1;
    }
    if (digitalRead(gms) == LOW and belltest ==  1)
    {
        int belltest = 0;
    }
}