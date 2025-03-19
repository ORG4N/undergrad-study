/*
------------------DR VASILIOS KELEFOURAS-----------------------------------------------------
------------------COMP2004 ------------------------------------------------------------------
------------------EMBEDDED PROGRAMMING AND THE INTERNET OF THINGS-------------------------------------------------
------------------UNIVERSITY OF PLYMOUTH, SCHOOL OF ENGINEERING, COMPUTING AND MATHEMATICS---
*/

// --------------- COMP2004 Coursework - Set of Exercises -------------------

/*
In this element of assessment you need to reduce the execution time of the ineffcient_routine(). 
This is an image processing routine written in an inefficient way.
First, read the code and understand what it does. Then, try to simplify the code (reduce its complexity), by eliminating redundant operations. Last, apply code optimizations such as scalar replacement, register blocking, loop merge and others. 

*/

// Part A
// 1. Fully unroll k loops
// 2. Strength reduction - remove redundant abs function
// 3. Simplify expressions and replacing M and N constants with raw values for readability (assuming that the program is only used when an image is 80x80 pixels)
// 4. Scalar replacement and register blocking using t1, t2, t3 integer variables
// 5. Redundant arrays removed: x_compute[x][y][0] = 0; xy_compute[x][y][0] = 0;
// 6. Remove redundant if/else and change for conditions to only iterate through non-border pixels (loop peeling)
// 7. Because the else is removed, these arrays are removed: x_image[x][y] = 0; xy_image[x][y] = 0;
// 8. Instead of doing an array lookup to find Filter values, simplify and use the raw value: Filter[0] becomes 99 etc. Strength reduction


// Part B
// 1. Fully unroll k loop
// 2. Remove redundant array: diff_compute[x][y][0] = 0;
// 3. Remove if/else and change for loop conditions to only iterate through non-border pixels (loop peeling)
// 4. Simplify expressions and replacing M and N constants with raw values for readability (assuming that the program is only used when an image is 80x80 pixels)
// 5. Scalar replacement and register blocking using t integer variables
// 6. Replace all x_offset and y_offset array lookups with their constant values.
// 7. Apply scalar replacement using x and y integer variables


// Part C
// 1. Remove outer if and else and change for loop conditions to only iterate through non-border pixels (loop peeling)
// 2. Rewrite while loop as for loop with (k=0; k<=7; k++)
// 3. Fully unroll k for loop and simplify expressions such as k, M and N.
// 4. Apply scalar replacement using t integer variables
// 5. Replace all x_offset and y_offset array lookups with their constant values. strength reduction
// 6. Apply scalar replacement using x and y integer variables


// Speed results
// Initial runtime on Nucelo board (debug)   = 21 msecs
// Optimised runtime on Nucelo board (debug) = 7 msecs

// Initial runtime on Nucelo board (release)   = 18 msecs
// Optimised runtime on Nucelo board (release) = 6 msecs

// Speedup on Nucelo board (debug)   = 3
// Speedup on Nucelo board (release) = 3
// Both cases show a 66.7% decrease in runtime


// Initial runtime on Personal Computer (debug)     = 1228 msecs
// Optimised runtime on Personal Computer (debug)   = 975 msecs

// Initial runtime on Personal Computer (release)   =  205 msecs
// Optimised runtime on Personal Computer (release) = 81 msecs

// Speedup on PC (debug)   = 1.3
// Speedup on PC (release) = 2.5

#include "mbed.h"


using namespace std::chrono;


#include "string.h"
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>


#define N 80 //image size 
#define M 80 //image size 

void initialization();
bool compare_images();


//the following variables never change their values. You could take this into advantage
const int C0=1;
const int C1=8;
const int x_offset[C1]={1,1,1,0,0,-1,-1,-1};
const int y_offset[C1]={1,0,-1,1,-1,1,0,-1};
const int Filter[]={99,68,35,10};

unsigned char input[N][M];
unsigned char output[N][M];
unsigned char x_image[N][M];
unsigned char xy_image[N][M];
unsigned char edge_image[N][M];
unsigned char diff_compute[N][M][C1+1];
unsigned short x_compute[N][M][(2 * C0) + 2];
unsigned short xy_compute[N][M][(2*C0)+2];
	
unsigned char maximum(unsigned char a, unsigned char b);
void inefficient_routine();




Timer timer;

int main() {
  

  printf("\n\r Programmed started \n\r");
	initialization();
	
	timer.start();
    
//YOU WILL OPTIMIZE THE FOLLOWING function
  inefficient_routine();
//------------------------------------------------------------------------------
	
 timer.stop();
printf("\nThe time taken was %llu msecs\n",duration_cast<milliseconds>(timer.elapsed_time()).count());

	bool outcome=compare_images();
	
	if (outcome==true)
		printf("\n\n\r -----  output is correct -----\n\r");
	else 
		printf("\n\n\r ----- output is INcorrect -----\n\r");

	return 0;
}

void initialization(){
	int i,j;
	
	for (i=0;i<N;i++)
	 for (j=0;j<M;j++)
	  input[i][j]=rand()%255;
	
	for (i=0;i<N;i++)
	   for (j=0;j<M;j++)
	    output[i][j]=0;
	
}


unsigned char maximum(unsigned char a, unsigned char b)
{
    return a > b ? a : b;
}

void inefficient_routine()
{
    int out_compute;
    int x, y, k; 
    int t1, t2, t3, t4, t5, t6, t7, t8; // Reused these 8 variables for Scalar replacement in each task
    int x1, x2, y1, y2;

    const unsigned short int total = 235;


    /*  Part A */
    for (x = 1; x < 79; ++x){
        x1 = x+1;
        x2 = x-1;
        for (y = 1; y < 79; ++y){

            t1 = x_compute[x][y][1];
            t2 = x_compute[x][y][2];
            t3 = x_compute[x][y][3];

            t1 = x_compute[x][y][0] + input[x2][y] * 68;
            t2 = t1 + input[x][y] * 99;
            t3 = t2 + input[x1][y] * 68;

            x_image[x][y] = t3 / total;
        }
    }

    for (x = 1; x < 79; ++x){
        for (y = 1; y < 79; ++y){
            t1 = xy_compute[x][y][1];
            t2 = xy_compute[x][y][2];
            t3 = xy_compute[x][y][3];

            t1 = xy_compute[x][y][0] + x_image[x][y - 1] * 68;
            t2 = t1 + x_image[x][y] * 99;
            t3 = t2 + x_image[x][y + 1] * 68;

            xy_image[x][y] = t3 / total;
        }
    }

    /*  Part B */
            
    for (x = 1; x < 79; ++x){
        x1 = x + 1;
        x2 = x - 1;
        
        for (y = 1; y < 79; ++y){

            t1 = diff_compute[x][y][1];
            t2 = diff_compute[x][y][2];
            t3 = diff_compute[x][y][3];
            t4 = diff_compute[x][y][4];
            t5 = diff_compute[x][y][5];
            t6 = diff_compute[x][y][6];
            t7 = diff_compute[x][y][7];
            t8 = diff_compute[x][y][8];

            y1 = y + 1;
            y2 = y - 1;

            t1 = maximum(abs(xy_image[x1][y1] - xy_image[x][y]), diff_compute[x][y][0]);
            t2 = maximum(abs(xy_image[x1][y] - xy_image[x][y]), t1);
            t3 = maximum(abs(xy_image[x1][y2] - xy_image[x][y]), t2);
            t4 = maximum(abs(xy_image[x][y1] - xy_image[x][y]), t3);
            t5 = maximum(abs(xy_image[x][y2] - xy_image[x][y]), t4);
            t6 = maximum(abs(xy_image[x2][y1] - xy_image[x][y]), t5);
            t7 = maximum(abs(xy_image[x2][y] - xy_image[x][y]), t6);
            t8 = maximum(abs(xy_image[x2][y2] - xy_image[x][y]), t7);

            edge_image[x][y] = t8;
        }   
    }


        //const int x_offset[C1]={1,1,1,0,0,-1,-1,-1};
        //const int y_offset[C1]={1,0,-1,1,-1,1,0,-1};

    /* Part C */
    for (x = 1; x < 79; ++x){
        x1 = x+1;
        x2 = x-1;
        for (y = 1; y < 79; ++y){

            y1 = y+1;
            y2 = y-1;
            out_compute = 255;
            t1 = edge_image[x][y];

            if (edge_image[x1][y1] < t1){out_compute = 0;}
            if (edge_image[x1][y] < t1){out_compute = 0;}
            if (edge_image[x1][y2] < t1){out_compute = 0;}
            if (edge_image[x][y1] < t1){out_compute = 0;}
            if (edge_image[x][y2] < t1){out_compute = 0;}
            if (edge_image[x2][y1] < t1){out_compute = 0;}
            if (edge_image[x2][y] < t1){out_compute = 0;}
            if (edge_image[x2][y2] < t1){out_compute = 0;}

            output[x][y] = out_compute;
        }
    }
}


//returns false/true, when the output image is incorrect/correct, respectively
bool compare_images(){
	

  unsigned char out_compute;
  int x,y,k;
  unsigned short total=0;


/* start layer 2 code */

  /*  GaussBlur(in_image, g_image); */
  for (k=-C0; k<=C0; ++k)  total += Filter[abs(k)];

  for (x=0; x<N; x++)
    for (y=0; y<M; y++)
     if (x>=C0 && x<=N-1-C0 && y>=C0 && y<=M-1-C0) {
      x_compute[x][y][0]=0;
      for (k=-C0; k<=C0; ++k)
        x_compute[x][y][C0+k+1] = x_compute[x][y][C0+k]
           + input[x+k][y]*Filter[abs(k)];
      x_image[x][y]= x_compute[x][y][(2*C0)+1]/total;
      }
     else
      x_image[x][y] = 0;

  for (x=0; x<N; x++)
    for (y=0; y<M; y++)
     if (x>=C0 && x<=N-1-C0 && y>=C0 && y<=M-1-C0) {
      xy_compute[x][y][0]=0;
      for (k=-C0; k<=C0; ++k)
        xy_compute[x][y][C0+k+1] = xy_compute[x][y][C0+k] +
           x_image[x][y+k]*Filter[abs(k)];
      xy_image[x][y]= xy_compute[x][y][(2*C0)+1]/total;
      }
     else
      xy_image[x][y] = 0;


 /*  ComputeEdges(g_image, c_image); */
  for (x=0; x<N; x++)
    for (y=0; y<M; y++)
     if (x>=C0 && x<=N-1-C0 && y>=C0 && y<=M-1-C0) {
      diff_compute[x][y][0] = 0;
      for (k=0; k<=C1-1; ++k)
        diff_compute[x][y][k+1] =
          maximum(abs(xy_image[x+x_offset[k]][y+y_offset[k]]
                    - xy_image[x][y]), diff_compute[x][y][k]);
      edge_image[x][y] = diff_compute[x][y][C1];
      }
     else
      edge_image[x][y] = 0;
  
  /*  DetectRoots(c_image, out_image); */
  for (x=0; x<N; x++)
    for (y=0; y<M; y++)
     if (x>=C0 && x<=N-1-C0 && y>=C0 && y<=M-1-C0) {
        out_compute = 255; 
        k = 0;
        while ((out_compute == 255) && (k <= C1-1)) {
          if (edge_image[x+x_offset[k]][y+y_offset[k]] <
              edge_image[x][y]) out_compute = 0;
          ++k; }
        if (output[x][y] != out_compute)
					return false;
        }
      else
          if (output[x][y] != 0)
					  return false;
		
					
					return true;
	}
	
