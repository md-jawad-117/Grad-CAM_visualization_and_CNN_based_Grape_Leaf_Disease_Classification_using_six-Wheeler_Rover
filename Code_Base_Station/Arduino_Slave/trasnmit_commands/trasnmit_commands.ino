#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>


RF24 radio(9, 10); // CE, CSN pins
const byte address[6] = "00001"; // Address of the receiver
int p=0;


void setup()
 {

  Serial.begin(9600); 
  radio.begin();
  radio.openWritingPipe(address);
  // radio.setPALevel(RF24_PA_LOW);
  radio.stopListening();
}

void loop() {
   if (Serial.available()) 
{
    int data = Serial.read();

    if (data==119)  // w
    {
       char dataToSend = 'w';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5); 
    }


    else if (data==115)   //s
    {
       char dataToSend = 's';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);   
    }


    else if (data==97)    // a
    {
       char dataToSend = 'a';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }


    else if (data==100)   //d
    {
       char dataToSend = 'd';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

///////////////////////////////////////////////////////////////////////////////////////
    else if (data==56)    //8
    {
       char dataToSend = '8';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }


    else if (data==54)    //6
    {
       char dataToSend = '6';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }


    else if (data==52)    //4
    {
       char dataToSend = '4';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }


    else if (data==50)     //2
    {
       char dataToSend = '2';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

// ////////////////////////////////////////////////////////////////////////////
    else if (data==116)     //t
    {
       char dataToSend = 't';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }


    else if (data==103)
    {
       char dataToSend = 'g';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }


    else if (data==104)
    {
       char dataToSend = 'h';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }


    else if (data==102)
    {
       char dataToSend = 'f';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }    
    
 //////////////////////////////////////////////////////////////////////////   
    else if (data==105)     //i
    {
       char dataToSend = 'i';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }    
    
    
    
    else if (data==106)     //j
    {
       char dataToSend = 'j';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }    
    
    
    
    else if (data==107)     //k
    {
       char dataToSend = 'k';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }    
    
    
    else if (data==108)    //l
    {
       char dataToSend = 'l';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }
//////////////////////////////////////////////////////////////////
     else if (data==32)    //space
    {
       char dataToSend = ' ';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }
    
///////////////////////////////////////////////////////////////////
     else if (data==122)    //z  (normal stream)
    {
       char dataToSend = 'z';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

     else if (data==120)    //x  ( detect disease)
    {
       char dataToSend = 'x';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

     else if (data==99)    //c  save data
    {
       char dataToSend = 'c';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

     else if (data==118)    //v store data
    {
       char dataToSend = 'v';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

     else if (data==98)    //b allign arm 90 degree
    {
       char dataToSend = 'b';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

     else if (data==110)    //n arm power
    {
       char dataToSend = 'n';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }

     else if (data==109)    //m wheel power
    {
       char dataToSend = 'm';
       radio.write(&dataToSend, sizeof(dataToSend));
       delay(5);
    }
    else
    {
      char dataToSend = 'pp';
      radio.write(&dataToSend, sizeof(dataToSend));
      delay(5);
    }
} 
} 
