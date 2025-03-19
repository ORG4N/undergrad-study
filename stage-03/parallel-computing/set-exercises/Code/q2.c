/*
------------------DR VASILIOS KELEFOURAS-----------------------------------------------------
------------------COMP3001 ------------------------------------------------------------------
------------------COMPUTER SYSTEMS MODULE-------------------------------------------------
------------------UNIVERSITY OF PLYMOUTH, SCHOOL OF ENGINEERING, COMPUTING AND MATHEMATICS---
*/

//compile with gcc q2.c -o p -O3 -D_GNU_SOURCE  -march=native -mavx -lm -D_GNU_SOURCE

#include <stdio.h>
#include <stdint.h>	/* for uint64 definition */
#include <immintrin.h>
#include <math.h>
#include <stdio.h>
#include <emmintrin.h>
#include <limits.h>
#include <pmmintrin.h>

#include <sched.h>
#include <pthread.h>
#include <sys/syscall.h>
#include <sys/mman.h>


#define N 8192
#define TIMES 1
#define BILLION 1000000000L
#define EPSILON 0.0001

#define ARITHMETICAL_OPS (N*N + N*N + N + N*N) * 14

void initialize();
void initialize_again();
void slow_routine(float alpha, float beta);//you will optimize this routine
unsigned short int Compare(float alpha, float beta);
unsigned short int equal(float const a, float const b) ;


float A[N][N], AT[N][N], u1[N], u2[N], v1[N], v2[N], x[N], y[N], w[N], z[N], test[N] __attribute__((aligned(64))); ;
	

int main(){

float alpha=0.23, beta=0.45;


struct timespec start, end;
uint64_t diff;
double gflops;

//THIS CODE FORCES THIS PROCESS TO RUN ON CORE #0 ONLY
cpu_set_t mask;
CPU_ZERO(&mask);
CPU_SET(0,&mask);
if(sched_setaffinity(0,sizeof(mask),&mask) == -1)
       printf("WARNING: Could not set CPU Affinity, continuing...\n");

	  
initialize();



clock_gettime(CLOCK_MONOTONIC, &start);	/* mark start time */

for (unsigned int t=0;t<TIMES;t++)
 slow_routine(alpha,beta);

clock_gettime(CLOCK_MONOTONIC, &end);	/* mark the end time */
diff = BILLION * (end.tv_sec - start.tv_sec) + end.tv_nsec - start.tv_nsec;
printf("elapsed time = %llu nanoseconds or %llu msecs\n", (long long unsigned int) diff, (long long unsigned int) diff/1000000);


gflops = (double) ARITHMETICAL_OPS / (diff / TIMES); //ARITHMETICAL_OPS /(nanoseconds/TIMES)
printf("\n%f GigaFLOPS achieved\n", gflops);

if (Compare(alpha,beta) == 0)
	printf("\nCorrect Result\n");
else 
	printf("\nINcorrect Result\n");


return 0;
}

void initialize(){

unsigned int    i,j;

//initialization
for (i=0;i<N;i++)
for (j=0;j<N;j++){
A[i][j]= 1.1;

}

for (i=0;i<N;i++){
z[i]=(i%9)*0.8;
x[i]=0.1;
u1[i]=(i%9)*0.2;
u2[i]=(i%9)*0.3;
v1[i]=(i%9)*0.4;
v2[i]=(i%9)*0.5;
w[i]=0.0;
y[i]=(i%9)*0.7;
}

}

void initialize_again(){

unsigned int    i,j;

//initialization
for (i=0;i<N;i++)
for (j=0;j<N;j++){
A[i][j]= 1.1;

}

for (i=0;i<N;i++){
z[i]=(i%9)*0.8;
x[i]=0.1;
test[i]=0.0;
u1[i]=(i%9)*0.2;
u2[i]=(i%9)*0.3;
v1[i]=(i%9)*0.4;
v2[i]=(i%9)*0.5;
y[i]=(i%9)*0.7;
}

}

// AVX is 256 bits, 8 elements can be vectorized

// GFLOPS before: 4.65
// GFLOPS after: 3.47

//you will optimize this routine
void slow_routine(float alpha, float beta){

unsigned int i,j, J1, J2, J3, J4, J5, J6, J7;

__m256 ALPHA, BETA, THREE; // alpha, beta, 3.22f

__m256 num0, num1, num2, num3, num4, num5, num6, ymm0;
__m128 xmm0;

  ALPHA = _mm256_set1_ps(alpha);
  BETA = _mm256_set1_ps(beta);
  THREE = _mm256_set1_ps(3.22f);
  
  
 // A[i][j] += alpha * u1[i] * v1[j] + u2[i] * v2[j];
  for (i = 0; i < N; i++){
    
    num0 = _mm256_set1_ps(u1[i]);
    num1 = _mm256_set1_ps(u2[i]);
    
    for (j = 0; j < ((N/8)*8); j+=8){
      
      num2 = _mm256_load_ps(&A[i][j]);
      num3 = _mm256_load_ps(&v1[j]);
      num4 = _mm256_load_ps(&v2[j]);
      
      num5 = _mm256_mul_ps(num1, num4); // mulitply u2[i] with v2[j] and store in arrV2
      num6 = _mm256_mul_ps(num0, num3); // multiply u1[i] with v1[j] 
      num6 = _mm256_mul_ps(ALPHA, num6); // and then multiply the previous line's result with alpha
      num6 = _mm256_add_ps(num5, num6); // add both results (arrv1 and arrv2)
      num6 = _mm256_add_ps(num6, num2); // add the total result to A[i][j]
      
      
      _mm256_store_ps(&A[i][j], num6);
    }
    
    for(j=(N/8)*8; j<N; j++){
    	A[i][j] += alpha * u1[i] * v1[j] + u2[i] * v2[j];
    }
  }	

  for (j = 0; j < N; j+=8){
    J1 = j+1;
    J2 = j+2;
    J3 = j+3;
    J4 = j+4;
    J5 = j+5;
    J6 = j+6;
    J7 = j+7;
    
    for (i = 0; i < N; i++){
    
      // Transpose A
      AT[i][j] = A[j][i];
      AT[i][J1] = A[J1][i];
      AT[i][J2] = A[J2][i];
      AT[i][J3] = A[J3][i];
      AT[i][J4] = A[J4][i];
      AT[i][J5] = A[J5][i];
      AT[i][J6] = A[J6][i];
      AT[i][J7] = A[J7][i];
    }
  }


//x[i] += A[j][i] * y[j] + beta;
  for (i = 0; i < N; i++){
  
    num3 = _mm256_setzero_ps();
    
    for (j = 0; j < ((N/8)*8); j+=8){
    
      num0 = _mm256_load_ps(&AT[i][j]); // Load AT[i][j]
      num1 = _mm256_load_ps(&y[j]); // Load y[j]
      
      num4 = _mm256_mul_ps(num0, num1); // A[j][i] * y[j]
      num3 = _mm256_add_ps(num3, num4); // x[i] += A[j][i] * y[j]
      num3 = _mm256_add_ps(num3, BETA); // x[i] += A[j][i] * y[j] + beta
    
    }
    
    // AVX MVM solution
    ymm0 = _mm256_permute2f128_ps(num3, num3, 1);
    num3 = _mm256_add_ps(num3, ymm0);
    num3 = _mm256_hadd_ps(num3, num3);
    num3 = _mm256_hadd_ps(num3, num3);
    xmm0 = _mm256_extractf128_ps(num3, 0);
    
    _mm_store_ss(&x[i], xmm0); // Store result back into x[i]
    
    for(j=(N/8)*8; j<N; j++){
    	x[i] += A[j][i] * y[j] + beta;
    }
    
    
    
  }
     
     
// x[i] += 3.22f * z[i];
  for (i = 0; i < ((N/8)*8); i+=8){
  
  	num0 = _mm256_load_ps(&x[i]);
  	num1 = _mm256_load_ps(&z[i]);
  	
  	num2 = _mm256_mul_ps(THREE, num1); // Multiply 3.22 by z[i]
  	num2 = _mm256_add_ps(num2, num0); // Add the result to x[i]
  	
  	_mm256_store_ps(&x[i], num2);
  }
	
  for(i=(N/8)*8; i<N; i++){
     x[i] += 3.22f * z[i];
  }



//w[i] += alpha * A[i][j] * x[j] + beta;
  for (i = 0; i < N; i++){
  
    num3 = _mm256_setzero_ps();
    
    for (j = 0; j < ((N/8)*8); j+=8){
      
      num0 = _mm256_load_ps(&A[i][j]);
      num1 = _mm256_load_ps(&x[j]);
      num4 = _mm256_mul_ps(num0, num1);
      num5 = _mm256_mul_ps(num4, ALPHA);
      num3 = _mm256_add_ps(num3, num5);
      num3 = _mm256_add_ps(num3, BETA);

    }
    
    ymm0 = _mm256_permute2f128_ps(num3, num3, 1);
    num3 = _mm256_add_ps(num3, ymm0);
    num3 = _mm256_hadd_ps(num3, num3);
    num3 = _mm256_hadd_ps(num3, num3);
    xmm0 = _mm256_extractf128_ps(num3, 0);
    
    _mm_store_ss(&w[i], xmm0);
    
    for(j; j<N; j++){
    	w[i] += alpha * A[i][j] * x[j] + beta;
    }
  }	
}


unsigned short int Compare(float alpha, float beta) {

unsigned int i,j;

initialize_again();


  for (i = 0; i < N; i++)
    for (j = 0; j < N; j++)
      A[i][j] += alpha * u1[i] * v1[j] + u2[i] * v2[j];


  for (i = 0; i < N; i++)
    for (j = 0; j < N; j++)
      x[i] += A[j][i] * y[j] + beta;

  for (i = 0; i < N; i++)
    x[i] += 3.22f * z[i];


  for (i = 0; i < N; i++)
    for (j = 0; j < N; j++)
      test[i] += alpha * A[i][j] * x[j] + beta;


    for (j = 0; j < N; j++){
	if (equal(w[j],test[j]) == 1){
	  printf("\n %f %f",test[j], w[j]);
		return -1;
		}
		}

	return 0;
}






unsigned short int equal(float const a, float const b) {
	
	if (fabs(a-b)/fabs(a) < EPSILON)
		return 0; //success
	else
		return 1;
}





