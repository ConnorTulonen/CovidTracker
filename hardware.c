Fully working prototype . Some parts of the code is inspired from individual developers from GitHub.



#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
 
// Replace with your network credentials
const char* ssid = "AB";
const char* password = "12345678";
ESP8266WebServer server(80);   //instantiate server at port 80 (http port)
 
String page = "";
String text = "";

//initials of the temp sensor
int ThermistorPin = 0;
int Vo;
float R1 = 10000;
float logR2, R2 ;
double data;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

void setup(void){
 pinMode(A0, INPUT);
 delay(1000);
 Serial.begin(115200);
 WiFi.begin(ssid, password); //begin WiFi connection
 Serial.println("");
 
 // Wait for connection
 while (WiFi.status() != WL_CONNECTED) {
 delay(500);
 Serial.print(".");
}
 
 Serial.println("");
 Serial.print("Connected to ");
 Serial.println(ssid);
 Serial.print("IP address: ");
 Serial.println(WiFi.localIP());
 server.on("/data.txt", [](){
   text = (String)data;
   server.send(200, "text/html", text);
 });
 server.on("/", [](){
   page = "<h1>Sensor to Node MCU Web Server</h1><h1>Data:</h1> <h1 id=\"data\">""</h1>\r\n";
   page += "<script>\r\n";
   page += "var x = setInterval(function() {loadData(\"data.txt\",updateData)}, 1000);\r\n";
   page += "function loadData(url, callback){\r\n";
   page += "var xhttp = new XMLHttpRequest();\r\n";
   page += "xhttp.onreadystatechange = function(){\r\n";
   page += " if(this.readyState == 4 && this.status == 200){\r\n";
   page += " callback.apply(xhttp);\r\n";
   page += " }\r\n";
   page += "};\r\n";
   page += "xhttp.open(\"GET\", url, true);\r\n";
   page += "xhttp.send();\r\n";
   page += "}\r\n";
   page += "function updateData(){\r\n";
   page += " document.getElementById(\"data\").innerHTML = this.responseText;\r\n";
   page += "}\r\n";
   page += "</script>\r\n";
   server.send(200, "text/html", page);
});
 
 server.begin();
 Serial.println("Web server started!");
}

void loop(void){


  Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  data = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  data = data - 273.15;
  data = (data * 9.0)/ 5.0 + 32.0;  
  delay(1000);
  server.handleClient();
}



Compilation and Uploading status:


Executable segment sizes:
IROM   : 261976          - code in flash         (default or ICACHE_FLASH_ATTR) 
IRAM   : 26980   / 32768 - code in IRAM          (ICACHE_RAM_ATTR, ISRs...) 
DATA   : 1292  )         - initialized variables (global, static) in RAM/HEAP 
RODATA : 1348  ) / 81920 - constants             (global, static) in RAM/HEAP 
BSS    : 25248 )         - zeroed variables      (global, static) in RAM/HEAP 
Sketch uses 291596 bytes (27%) of program storage space. Maximum is 1044464 bytes.
Global variables use 27888 bytes (34%) of dynamic memory, leaving 54032 bytes for local variables. Maximum is 81920 bytes.
Invalid library found in C:\Users\2021\Documents\Arduino\libraries\Adafruit_Sensor-master: no headers files (.h) found in C:\Users\2021\Documents\Arduino\libraries\Adafruit_Sensor-master
Invalid library found in C:\Users\2021\Documents\Arduino\libraries\ESPAsyncTCP-master: no headers files (.h) found in C:\Users\2021\Documents\Arduino\libraries\ESPAsyncTCP-master
Invalid library found in C:\Users\2021\Documents\Arduino\libraries\ESPAsyncWebServer-master: no headers files (.h) found in C:\Users\2021\Documents\Arduino\libraries\ESPAsyncWebServer-master




@cornor. Feel free to make any changes.
Prototype is Ready . Assembly and integration left.
