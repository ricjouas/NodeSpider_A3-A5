#include "DHT.h"
#include "WiFi.h"
#include <HTTPClient.h>
#include <ArduinoJson.h>

//WiFi credintials
const char* ssid = "";
const char* password = "";

const unsigned long eventInterval = 60000;
unsigned long previousTime = 0;

int motion = 0;
int pirState = LOW;

#define DHTPIN 16
#define DHTTYPE DHT11
#define pirPin 2

//Type of sensor
DHT dht(DHTPIN, DHTTYPE);

WiFiClient client;

String readDHTTemperature() {
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
  float h = dht.readHumidity();
  if (isnan(h)) {
    Serial.println("Failed to read from DHT sensor!");
    return "--";
  }
  else {
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
  pinMode(pirPin, INPUT);
  dht.begin();
  wifiConnect();
  
}

void PIRSensor() {
   if(digitalRead(pirPin) == HIGH) {
    if(pirState==LOW){
       Serial.println("YOU'VE GOT MAIL!!");
        if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
          HTTPClient http;
          String message = "YOU'VE GOT MAIL!!";
          String json = "{\"motion\":\""+message+"\"}";
          http.begin("http://ricjouas.pagekite.me/api/motion/"); //Specify destination for HTTP request
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
       pirState=HIGH;
       delay(100);
      }       
   }else{
    if (pirState==HIGH){
      pirState=LOW;
    }
   }
}

void tempCurlRequest() {

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    HTTPClient http;
    String dhtT = readDHTTemperature();
    String json = "{\"temp\":\""+dhtT+"\"}";
    http.begin("http://ricjouas.pagekite.me/api/temperature/"); //Specify destination for HTTP request
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

void humidCurlRequest() {

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    HTTPClient http;
    String dhtH = readDHTHumidity();
    String json = "{\"humidity\":\""+dhtH+"\"}";
    http.begin("http://ricjouas.pagekite.me/api/humidity/"); //Specify destination for HTTP request
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
  PIRSensor();
  unsigned long currentTime = millis();
  if( currentTime - previousTime >= eventInterval){
    tempCurlRequest();
    humidCurlRequest();
    previousTime = currentTime;
    
  }
}
