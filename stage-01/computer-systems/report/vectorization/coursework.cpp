#include "coursework.h"

float* V1, * V2, * test;

void initialization() {

	float e = 0.1234f, p = 0.7264f, r = 0.11f;
	int j;

	V1 = (float*)malloc(M * sizeof(float)); // Dynamically allocate memory for V1 using malloc()
	if (V1 == NULL) { // Check if the memory has been successfully allocated by malloc or not 
		printf("\nMemory not allocated.\n");
		exit(0); // stop running program
	}
	printf("\n\nV1 Memory has been allocated.\n");


	V2 = (float*)malloc(M * sizeof(float)); // Dynamically allocate memory for V2 using malloc() 
	if (V2 == NULL) { // Check if the memory has been successfully allocated by malloc or not 
		printf("\nMemory not allocated.\n");
		exit(0); // stop running program
	}
	printf("\n\nV2 Memory has been allocated.\n");


	test = (float*)malloc(M * sizeof(float)); // Dynamically allocate memory for test using malloc() 
	if (test == NULL) { // Check if the memory has been successfully allocated by malloc or not 
		printf("\nMemory not allocated.\n");
		exit(0); // stop running program
	}
	printf("\n\nTest Memory has been allocated.\n");


	for (j = 0; j != M; j++) {
		V1[j] = (j % 17) + p;
		V2[j] = (j % 13) + e;
		test[j] = V1[j];
	}
}


unsigned short int default_routine() {
	int i, j;

	for (j = 0; j < M; j++) {
		V1[j] = V1[j] + V2[j] + 2.12f;
	}


	return 2;
}

unsigned short int SSE() {

	//WRITE YOUR CODE HERE

	__m128 num1, num2, num3, num4, num5;

	num1 = _mm_set_ps(2.12f, 2.12f, 2.12f, 2.12f);
	int j;

	for (j=0; j<(M/4)*4; j+=4)			// the division will return as an int, for example 10/4 = 2
	{
		num2 = _mm_loadu_ps(&V1[j]);	// load 4 elements from V1[], such as: V1[i] and V1[i+1] and V1[i+2] and V1[i+3]
		num3 = _mm_loadu_ps(&V2[j]);	// same as above, but for V2[]
		num4 = _mm_add_ps(num2, num3);	// add the four loaded elements from each array to eachother
		num5 = _mm_add_ps(num4, num1);	// add each of the previous sums to 2.12

		_mm_storeu_ps(&V1[j], num5);	// store the calculated sum back to the array V1[]
	}

	for (; j < M; j++)					// the starting value of this loop will be where the above vectorisation loop ends
	{
		V1[j] = V1[j] + V2[j] + 2.12f; 	// Non-vectorised addition of any remaining elements.
	}


	return 2;
}

unsigned short int Compare() {
	int i, j;

	 for (j = 0; j < M; j++) {
		test[j] = test[j] + V2[j] + 2.12f;
	}


		for (j = 0; j < M; j++)
		 if (equal(V1[j], test[j]) == 1) {
			//printf("\n i,j=%d,%d\n", i,j);
			return 1;
		}
	
	// Deallocate all of the memory that was previously allocated within Initialisation()
	// The memory is deallocated within this function as it is run after default_routine() and SSE()
	free(V1);
	free(V2);
	free(test);
	printf("\n\nMalloc Memory successfully freed.\n");

	
	return 0;
}

unsigned short int equal(float a, float b) {
	float temp = a - b;
	//printf("\n %f  %f", a, b);
	if (fabs(temp) < EPSILON)
		return 0; //success
	else
		return 1; //wrong result
}




