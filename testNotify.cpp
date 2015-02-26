//************************************************************
// testNotify.cpp
//
// A trivial app for Spark Core to test notifications.
//
// CLI build:
//
// spark compile . --saveTo testNotify.bin
// spark flash --usb testNotify.bin
//
// electronut.in
//************************************************************

#include "application.h" 

// set up 
void setup()
{

}

int count = 0;
char strMsg[16];

// main loop
void loop()
{
    // send notification
    sprintf(strMsg, "Yo %d", count++);
    Spark.publish("mycore_notify", strMsg);

    // 5 sec sleep
    delay(5000);
    
}
