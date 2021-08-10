#include "DHT.h"
#include "WiFi.h"
#include <HTTPClient.h>
#include <ArduinoJson.h>

//WiFi credintials
const char* ssid = "";
const char* password = "";

const unsigned long eventInterval = 10000;
unsigned long previousTime = 0;

#define DHTPIN 16
#define DHTTYPE DHT11

//Type of sensor
DHT dht(DHTPIN, DHTTYPE);

int    HTTP_PORT   = 80;
String HTTP_METHOD = "POST"; // or "POST"
char   HOST_NAME[] = ""; // hostname of web server:
String PATH_NAME   = "";

WiFiClient client;

String readDHTTemperature() {
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  if (isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return "--";
  }
  else {
   
    return String(t);
  }
}

String readDHTHumidity() {
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  if (isnan(h)) {
    Serial.println("Failed to read from DHT sensor!");
    return "--";
  }
  else {
    Serial.println(h);
    return String(h);
  }
}

void wifiConnect() {
  //Connect to WiFi
  delay(4000);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connecting to WiFi..");
  }

  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());

}
void setup() {

  Serial.begin(115200);
  Serial.println(F("STARTING SMART MAILBOX!"));

  dht.begin();
  wifiConnect();
  curlRequest();
}

void curlRequest() {

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    HTTPClient http;
    String dhtT = readDHTTemperature();
    String json = "{\"temp\":\""+dhtT+"\"}";
    http.begin("http://"); //Specify destination for HTTP request
    http.addHeader("Authorization", "Token ");
    http.addHeader("Content-Type", "application/json");
    int httpCode = http.POST(json);
    //int httpCode =http.GET();
    if (httpCode > 0) {
      Serial.print("Http response code: ");
      Serial.println(httpCode);
      Serial.println(json);
      //String payload = http.getString();
      //Serial.println(payload);
      if (httpCode == 201) {
        Serial.println("Success!");
      }
    }
  }
}

void loop() {

  unsigned long currentTime = millis();
  if( currentTime - previousTime >= eventInterval){
    curlRequest();
    previousTime = currentTime;
    
  }
}
