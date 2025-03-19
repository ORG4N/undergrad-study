/*
@ORG4N
Class for getting samples and storing them within an instance
Also, a function to convert an instance to a string so it can be easily written to SD

*/

#include "sensors.h"
using namespace sensors;

#include "uop_msb.h"
using namespace uop_msb;

#include <iostream>
using namespace std;


// Gets the data from the board, creates an instance and then prints values
Sensor getSample(){
    AnalogIn ldr(AN_LDR_PIN);
    EnvSensor env;

    // Get sample data
    float temp = env.getTemperature();
    float pres = env.getPressure();
    float lux = ldr.read();

    printf("T=%.2f, P=%.2f, L=%.2f\n", temp, pres, lux);

    Sensor s(temp, pres, lux);
    return s;
}

string Sensor::toString(){

    string str = "Temperature: " + to_string(temperature) + ", Pressure: " + to_string(pressure) + ", Light: " + to_string(lighting) + "\n";
    return str;
}