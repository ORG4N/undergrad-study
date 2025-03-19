/*
 * Copyright (c) 2020 Arm Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "uop_msb.h"
#include "rtos/ThisThread.h"
#include "NTPClient.h"
#include "azure_c_shared_utility/xlogging.h"
#include <cstring>
#include <string.h>
#include "sensors.h"
#include "data_sample.h"
#include "sd.h"

#include <iostream>
using namespace std;

#define AN_LDR_PIN  PC_0

//using namespace uop_msb;
using namespace data_sample;
using namespace sensors;
using namespace sd;

extern NetworkInterface *_defaultSystemNetwork;

void thread();
void sampling();
void writing();
extern Sensor getSample();

Thread producer;
Thread consumer;
EventQueue queue;
List sample_list;

Semaphore sem1;
Semaphore sem2(10);

bool connect()
{
    LogInfo("Connecting to the network");

    _defaultSystemNetwork = NetworkInterface::get_default_instance();
    if (_defaultSystemNetwork == nullptr) {
        LogError("No network interface found");
        return false;
    }

    int ret = _defaultSystemNetwork->connect();
    if (ret != 0) {
        LogError("Connection error: %d", ret);
        return false;
    }
    LogInfo("Connection success, MAC: %s", _defaultSystemNetwork->get_mac_address());
    return true;
}

bool setTime()
{
    LogInfo("Getting time from the NTP server");

    NTPClient ntp(_defaultSystemNetwork);
    ntp.set_server("time.google.com", 123);
    time_t timestamp = ntp.get_timestamp();
    if (timestamp < 0) {
        LogError("Failed to get the current time, error: %ud", timestamp);
        return false;
    }
    LogInfo("Time: %s", ctime(&timestamp));
    set_time(timestamp);
    return true;
}

int main() {

    // START - UNCOMMENT THE FOLLOWING TWO LINES TO TEST YOUR BOARD AND SEE THE DEMO CODE WORKING
    //UOP_MSB_TEST  board;  //This class is purely for testing. Do no use it otherwise!!!!!!!!!!!
    //board.test();         //Look inside here to see how this works
    // END

    if (!connect()) return -1;

    if (!setTime()) return -1;


    // Start queue
    producer.start(thread);
    producer.set_priority(osPriorityRealtime);


    // Every 10 seconds run the getSample function to fetch Temp, Pressure and Light
    queue.call_every(10s, sampling);
    queue.call_every(60s, writing); // Write to SD every 60 seconds
}

void thread()
{
    queue.dispatch_forever();
}

// Sampling
void sampling(){

    // Get sample data object
    Sensor sample = getSample();
    string s = sample.toString(); // Convert to string

    // Add sample to buffer
    sample_list.Push(s);
}

// Writing thread
void writing(){

    SD_Card card;

    string data = sample_list.Pop();

    while(sample_list.counter > 0){
        string data = sample_list.Pop();
        card.Write(data);
    }
}