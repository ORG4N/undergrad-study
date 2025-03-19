/*
@ORG4N
Class for storing SD write function

*/

#ifndef __SD__
#define __SD__

#include "mbed.h"
#include "Stream.h"
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <map>
#include <string>
#include "sensors.h"
#include <cstdio>

#include <iostream>
#include "SDBlockDevice.h"
#include "FATFileSystem.h"


namespace sd{

    class SD_Card{
        public:
            int Write(string data){

                SDBlockDevice sd = {PB_5, PB_4, PB_3, PF_3};

                printf("Initialise and write to a file\n");
                int err;

                err=sd.init();
                if ( 0 != err) {
                    printf("Init failed %d\n",err);
                    return -1;
                }
                
                FATFileSystem fs("sd", &sd);
                FILE *fp = fopen("/sd/samples.txt","w");
                if(fp == NULL) {
                    error("Could not open file for write\n");
                    sd.deinit();
                    return -1;
                } 
                
                else {
                //Put some text in the file...
                fprintf(fp, "%s\n", data.c_str());
                //Tidy up here
                fclose(fp);
                printf("SD Write done... %s\n", data.c_str());
                sd.deinit();
                return 0;
            }
        }
    };
}


#endif