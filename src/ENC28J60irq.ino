// Testing ENC28J60 with arduino Micro 3.3v 8MHz
// use interrupt from ENC28J60 for read UDP data port 6000
// BVH@09132016

#include <UIPEthernet.h>

#define interruptPin 7

EthernetUDP udp;

void readData(){
  int size = udp.parsePacket();
  if(size > 0){
    char* msg = (char*)malloc(size+1);
    int len = udp.read(msg,size+1);
    msg[len]=0;
    Serial.println(msg);
    free(msg);
  }
}

void setup(){
  Serial.begin(38400);

  uint8_t mac[6] = {0x00,0x01,0x02,0x03,0x04,0x05};

  Ethernet.begin(mac,IPAddress(192,168,5,6));

  int success = udp.begin(6000);

  attachInterrupt(digitalPinToInterrupt(interruptPin), readData, FALLING);
}

void loop(){

}
