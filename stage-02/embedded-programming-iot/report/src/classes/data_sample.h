/*
@ORG4N
Header file defining List FIFO data structure used to store samples.

*/

#ifndef __DATA_SAMPLE__
#define __DATA_SAMPLE__

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

using namespace std;

using namespace sensors;

using namespace std::chrono;

namespace data_sample {

    // Data is stored within nodes
    struct Node{
        string data;
        Node* next; // Pointer to next Node in list
    };
    
    // FIFO data structure for buffering
    class List {

        private:
            Node *head, *tail;

            Semaphore sem1;
            Semaphore sem2 = {360};

        public:
            Mutex countLock;
            uint16_t counter = 0;

            List(){
                head = NULL;
                tail = NULL;
            }

            void Push(string sample){
                Node *t = new Node;
                t->data = sample; 
                t->next = NULL;

                sem2.acquire(); //Decrement
                countLock.lock();
                counter++;
                countLock.unlock();
                sem1.release(); //Increment

                if(head == NULL)
                {
                    head = t;
                    tail = t;
                }
                else
                {
                    tail->next = t;
                    tail = tail->next;

                }
            }

            string Pop(){

                if(head != NULL){
                    Node *t = head;
                    head = head->next;
                    free(t);

                    sem1.acquire(); //Decrement
                    countLock.lock();
                    counter--;
                    countLock.unlock();
                    sem2.release(); //Increment

                    return head->data;
                }

                return "Error";
            }

            void Clear(){
                head = NULL;
                tail = NULL;
                counter = 0;
            }

            void Display()
            {
                Node *t;
                t = head;
                while (t != NULL)
                {
                    cout << t->data << "\n";
                    t = t->next;
                }
            }
    };

}
#endif