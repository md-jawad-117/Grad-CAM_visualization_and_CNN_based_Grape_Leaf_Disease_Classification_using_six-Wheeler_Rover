#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include<Servo.h>

//create an RF24 object
RF24 radio(9, 53);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";
int data;


int t=0;
int leftm_f=38 ;
int leftm_b= 39;
int rightm_f= 40;
int rightm_b= 41;
// int left= 42;
// int right= 43;
// #define arm_pow=;
// #define wheel_pow=;
// int pow1=1;
// int pow2=1;
// int speed=255;
int p=0;     //0 mean move left
int q=0;     // means move right

int r=0;
int s=0;
Servo  base;            // joystick 2
Servo  sh1;             // joystick 2
int base_=90;
int sh_1=40;            

Servo  sh2;             // joystick 3             // joystick 3
int sh_2=10;

Servo  gripper;         // joystick 4
int gripper_=0;     //open

Servo wheel1;
Servo wheel2;
Servo wheel3;
Servo wheel4;
int wheel_1=67;
int wheel_2=64;
int wheel_3=56;
int wheel_4=62;



void setup() {
  Serial.begin(9600);
  radio.begin(

  );
  //set the address
  radio.openReadingPipe(0, address);
  //Set module as receiver
  radio.startListening();


  base.attach(30);
  sh1.attach(31);
  sh2.attach(32);
  gripper.attach(33);
  wheel1.attach(34);
  wheel2.attach(35);
  wheel3.attach(36);
  wheel4.attach(37);

  base.write(base_);
  sh1.write(sh_1);
  sh2.write(sh_2);
  gripper.write(gripper_);
  wheel1.write(wheel_1);
  wheel2.write(wheel_2);
  wheel3.write(wheel_3);
  wheel4.write(wheel_4);


  pinMode(leftm_f,OUTPUT);
  pinMode(leftm_b,OUTPUT);
  pinMode(rightm_f,OUTPUT);
  pinMode(rightm_b,OUTPUT);
  // pinMode(left,OUTPUT);
  // pinMode(right,OUTPUT);
  digitalWrite(leftm_f,0);
  digitalWrite(leftm_b,0);
  digitalWrite(rightm_f,0);
  digitalWrite(rightm_b,0);
  // analogWrite(left,speed);
  // analogWrite(right,speed);

  // digitalWrite(arm_pow,1);
  // digitalWrite(wheel_pow,1);


}

void loop() {
  if (radio.available())
{
   
    radio.read(&data, sizeof(data));
    Serial.println(data);

    if (data==119)  // w
    {
      if (r==1) 
      {                   //stop
        digitalWrite(leftm_f,0);
        digitalWrite(leftm_b,0);
        digitalWrite(rightm_f,0);
        digitalWrite(rightm_b,0);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
        r=0;
      
    }
     else if (r==0) 
      {                   //forward
        digitalWrite(leftm_f,1);
        digitalWrite(leftm_b,0);
        digitalWrite(rightm_f,1);
        digitalWrite(rightm_b,0);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
        r=1;
    }
    }


    else if (data==115)   //s
    {
           if (s==1) 
      {                   //stop
        digitalWrite(leftm_f,0);
        digitalWrite(leftm_b,0);
        digitalWrite(rightm_f,0);
        digitalWrite(rightm_b,0);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
        s=0;
        
    }
     else if (s==0) 
      {                   //forward
        digitalWrite(leftm_f,0);
        digitalWrite(leftm_b,1);
        digitalWrite(rightm_f,0);
        digitalWrite(rightm_b,1);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
        s=1;
    }}


    else if (data==97)    // a
    {
          if (p==1)  //move center
        {
          wheel1.write(wheel_1);
          wheel2.write(wheel_2);
          wheel3.write(wheel_3);
          wheel4.write(wheel_4);
          p=0;  
        }

        else if (p==0)    //move left
        {
          wheel1.write(wheel_1-25);
          wheel2.write(wheel_2-25);
          wheel3.write(wheel_3+25);
          wheel4.write(wheel_4+25);
          p=1;
        }
    }


    else if (data==100)   //d
    {
      if (q==1)  //move center
        {
          wheel1.write(wheel_1);
          wheel2.write(wheel_2);
          wheel3.write(wheel_3);
          wheel4.write(wheel_4);
          q=0;
        }

        else if (q==0)  // move right
        {
          wheel1.write(wheel_1+25);
          wheel2.write(wheel_2+25);
          wheel3.write(wheel_3-25);
          wheel4.write(wheel_4-25);
          q=1;
        }
    }

//////////////////////////////////////////////////////////////////
    else if (data==56)   // shoulder1 up
    {
      if (sh_1>40)
      {
        sh_1--;
        sh1.write(sh_1);
        delay(30);
      }
    }

// clockwise e kme
    else if (data==50)  // shoulder1 down 
    {
      if (sh_1<130)
      {
        sh_1++;
        sh1.write(sh_1);
        delay(30);
      }
    }


    else if (data==52)     // base  left
    {
      if (base_<180)
      {
        base_++;
        base.write(base_);
        delay(15);
      }
    }


    else if (data==54)     //base right
    {
      if (base_>0)
      {
        base_--;
        base.write(base_);
        delay(15);
      }
    }

/////////////////////////////////////////////////////////////////
    else if (data==116)     // shoulder 2 up
    {
      if (sh_2>0)
      {
        sh_2--;
        sh2.write(sh_2);
        delay(30);
      }
    }


    else if (data==103)     //shoulder 2 down
    {
      if (sh_2<120)
      {
        sh_2++;
        sh2.write(sh_2);
        delay(30);
      }
    }


    else if (data==104)                // gripper release
    {
      if (gripper_>0)
      {
        gripper_--;
        gripper.write(gripper_);
        
      }
    }


    else if (data==102)                 // // gripper grab
    {
      if (gripper_<110)
      {
        gripper_++;
        gripper.write(gripper_);
      
      }
    }

/////////////////////////////////////////////////////////////////
    else if (data==105)                    // wheel cross
    {
        wheel1.write(wheel_1);
      wheel2.write(wheel_2);
      wheel3.write(wheel_3);
      wheel4.write(wheel_4);
        digitalWrite(leftm_f,0);
        digitalWrite(leftm_b,0);
        digitalWrite(rightm_f,0);
        digitalWrite(rightm_b,0);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
     
    }


    else if (data==107)              // wheel normal
    {
      
    }

    
    else if (data==106)   // rotate left
    {   wheel1.write(wheel_1+45);
      wheel2.write(wheel_2-45);
      wheel3.write(wheel_3-45);
      wheel4.write(wheel_4+45);
     
        digitalWrite(leftm_f,0);
        digitalWrite(leftm_b,1);
        digitalWrite(rightm_f,1);
        digitalWrite(rightm_b,0);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
    }


    else if (data==108)    //rotate right
    {
       wheel1.write(wheel_1+45);
      wheel2.write(wheel_2-45);
      wheel3.write(wheel_3-45);
      wheel4.write(wheel_4+45);
        digitalWrite(leftm_f,1);
        digitalWrite(leftm_b,0);
        digitalWrite(rightm_f,0);
        digitalWrite(rightm_b,1);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
    }
    

////////////////////////////////////////////////////////////////////
    else if (data==32)                //brake
    {
        digitalWrite(leftm_f,0);
        digitalWrite(leftm_b,0);
        digitalWrite(rightm_f,0);
        digitalWrite(rightm_b,0);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
    }

///////////////////////////////////////////////////////////////////
    else if (data==122)   //run camera
    {

    }

    else if (data==98)    // alogn arm 90 degree     b
    {  
      base_=90;
      sh_1=170;
      sh_2=90;
      
      base.write(base_);
      sh1.write(sh_1);
      sh2.write(sh_2);
    }


     else if (data==98)    // get and send sensor data
    {  
      base_=90;
      sh_1=170;
      sh_2=90;
      
      base.write(base_);
      sh1.write(sh_1);
      sh2.write(sh_2);
    }


    else
    {
        digitalWrite(leftm_f,0);
        digitalWrite(leftm_b,0);
        digitalWrite(rightm_f,0);
        digitalWrite(rightm_b,0);
        // analogWrite(left,speed);
        // analogWrite(right,speed);
    }

}  
}
