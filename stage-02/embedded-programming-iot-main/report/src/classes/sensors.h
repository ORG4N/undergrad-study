#ifndef __SENSORS__
#define __SENSORS__

#include "mbed.h"
#include "Stream.h"
#include <chrono>
#include <cstdint>
#include <map>

using namespace std::chrono;

namespace sensors {

    #define AN_LDR_PIN  PC_0

    class Sensor {
        private:
            float temperature;
            float pressure;
            float lighting;

        public:

            Sensor(float t, float p, float l) { 
                temperature = t;
                pressure = p;
                lighting = l;
            };

            Sensor getSample();
            string toString();

            float getTemperature(){return temperature;};
            float getPressure(){return pressure;};
            float getLighting(){return lighting;};
    };
}

#endif