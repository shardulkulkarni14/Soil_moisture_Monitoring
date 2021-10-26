#include <ESP8266WiFi.h>

String apiKey = "IHQLW6FOBNK27SYP";     //  Enter your Write API key from ThingSpeak

const char *ssid =  "Bhandara 2.4G";     // replace with your wifi ssid and wpa2 key
const char *pass =  "sherlocked";
const char* server = "api.thingspeak.com";

const int sensor_pin = A0;

WiFiClient client;

void setup()
{
  Serial.begin(115200);
  delay(10);

  Serial.println("Connecting to ");
  Serial.println(ssid);


  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  delay(4000);
}

void loop()
{
  int moisture_percentage;
  moisture_percentage = (100.00 - ((analogRead(sensor_pin)/1023.00)*100.00));

  Serial.print("Soil Moisture(in Percentage) =");
  Serial.print(moisture_percentage);
  Serial.println("%");
  if (client.connect(server, 80))  //   "184.106.153.149" or api.thingspeak.com
  {

    String postStr = apiKey;
    postStr += "&field3=";
    postStr += String(moisture_percentage);
    postStr += "\r\n";

    client.print("POST /update HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n");
    client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
    client.print("Content-Type: application/x-www-form-urlencoded\n");
    client.print("Content-Length: ");
    client.print(postStr.length());
    client.print("\n\n");
    client.print(postStr);

    Serial.print("Data send to Thingspeak");

  }
  client.stop();

  Serial.println("Waiting...");

  // thingspeak needs minimum 15 sec delay between updates, i've set it to 20 seconds
  delay(2000);
}
