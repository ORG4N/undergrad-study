/*
------------------COMP1001 COURSEWORK ------------------------------------------------------------------
gcc: error: unrecognized command-line option ‘-0’
------------------COMPUTER SYSTEMS MODULE-------------------------------------------------
------------------UNIVERSITY OF PLYMOUTH, SCHOOL OF ENGINEERING, COMPUTING AND MATHEMATICS---
*/

//THIS CODE RUNS ON LINUX ONLY

//compile with gcc coursework_pthreads.c -o exec -lpthread
//run with ./exec

#include <stdio.h>      //for printf
#include <stdlib.h>
#include <pthread.h>    //for pthreads
#include <math.h>       //for fabs()
#include <time.h>	/* for clock_gettime */
#include <stdint.h>	/* for uint64 definition */

#define TIMES 1
#define BILLION 1000000000L
#define EPSILON 0.01
#define NUM_THREADS 4

#define P 4095 //input size
double A2[P][P], test4[P][P], u1[P], v1[P], u2[P], v2[P] ;

void initialization();
unsigned short int gemver_default();
unsigned short int Compare_Gemver();
void *gemver_parallel(void *rank);
inline unsigned short int equal(double const a, double const b);



int main() {

   unsigned short int output;
   int t;
   struct timespec start, end; //timers
   uint64_t diff;

	long int thread_num;
	pthread_t thread_handles[NUM_THREADS];

	time_t start1, end1;
	struct timeval start2, end2;

	//initialize the arrays
	initialization();


	/* measure monotonic time */
      clock_gettime(CLOCK_MONOTONIC, &start);	/* mark start time */

	for(int iter=0; iter<TIMES; iter++){
		for(thread_num=0; thread_num<NUM_THREADS; thread_num++){
			pthread_create(&thread_handles[thread_num], NULL, gemver_parallel, (void*) thread_num );
		}
		
		for(thread_num=0; thread_num<NUM_THREADS; thread_num++){
		pthread_join(thread_handles[thread_num], NULL);
		}
	}

       clock_gettime(CLOCK_MONOTONIC, &end);	/* mark the end time */

	diff = BILLION * (end.tv_sec - start.tv_sec) + end.tv_nsec - start.tv_nsec;
	printf("elapsed time = %llu nanoseconds\n", (long long unsigned int) diff);
        printf("elapsed time = %llu mseconds\n", (long long unsigned int) diff/1000000);

	//this code is for testing
        if (Compare_Gemver() == 0) //this function checks whether the result is correct or not
		printf("\n\n\r -----  output is correct -----\n\r");
        else
		printf("\n\n\r ----- output is INcorrect -----\n\r");

       
return 0;
}


void initialization() {

	double e = 0.1234, p = 0.7264, r = 0.11;

	//gemver
	for (int i = 0; i < P; i++)
		for (int j = 0; j < P; j++) {
			A2[i][j] = 0.0;
			test4[i][j] = 0.0;
		}

	for (int j = 0; j < P; j++) {
		u1[j] = e + (j % 9);
		v1[j] = e - (j % 9);
		u2[j] = p + (j % 9);
		v2[j] = p - (j % 9);
	}

	
}


//------------ THIS IS THE ROUTINE THAT YOU WILL PARALLELIZE -------------------
unsigned short int gemver_default() {

       //this is the loop to parallelize
	for (int i = 0; i < P; i++)
		for (int j = 0; j < P; j++)
			A2[i][j] += u1[i] * v1[j] + u2[i] * v2[j];

	return 0;
}

void *gemver_parallel(void* thread_num) {

       long int my_thread_num = (long) thread_num;
       int i, j;
       
       int local = P/NUM_THREADS;
       int remainder = P % NUM_THREADS;
       
       int starting_element = my_thread_num * local;
       int ending_element = starting_element + local - 1;
       
       if (remainder!=0 && my_thread_num == NUM_THREADS-1){ // or i could do my_thread_num == 3 because this code will use 4 threads
		int extra = P - ending_element - 1;
		ending_element += extra;  
       }
       
       for(i=starting_element; i<= ending_element; i++){
       		for(j=0; j<P; j++){
       			A2[i][j] += u1[i] * v1[j] + u2[i] * v2[j];
       		}
       }
        printf("\n%li: %i TO %i",my_thread_num ,starting_element, ending_element);
        
	return 0;
}

unsigned short int Compare_Gemver() {

	for (int i = 0; i < P; i++)
		for (int j = 0; j < P; j++)
			test4[i][j] += u1[i] * v1[j] + u2[i] * v2[j];

	for (int i = 0; i < P; i++)
		for (int j = 0; j < P; j++)
			if (equal(A2[i][j], test4[i][j]) == 1)
				return -1;

	return 0;
}






unsigned short int equal(double const a, double const b) {
	double temp = a - b;
	//printf("\n %f  %f", a, b);
	if (fabs(temp) < EPSILON)
		return 0; //success
	else
		return 1;
}

