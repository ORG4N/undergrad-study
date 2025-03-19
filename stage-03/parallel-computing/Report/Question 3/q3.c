/*
------------------DR VASILIOS KELEFOURAS-----------------------------------------------------
------------------COMP3001 ------------------------------------------------------------------
------------------PARALLEL PROGAMMING MODULE-------------------------------------------------
------------------UNIVERSITY OF PLYMOUTH, SCHOOL OF ENGINEERING, COMPUTING AND MATHEMATICS---
*/

#include "convolution_layer_2D.h"

#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))


// Initial GFLOPS value: 2
// Final GFLOPS value: 2

int unoptimized_layer_FP(const float * in_FP, const float * filter_FP, const float *bias_array_FP, float * out_to_compare_with_FP){

    unsigned long long int in_subscript, filter_subscript, out_subscript;
    float temp = 0.0f;
    float s,w;
    
    unsigned int t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12;
    

    t1 = Input_Y_dim * Input_X_dim * Input_depth_dim;
    t4 = Input_X_dim * Input_depth_dim;

    for (unsigned int b = 0; b < Input_Output_batch_dim; b++) { //assume batch=1, needs to be fixed
        t1 = b * (Input_Y_dim * Input_X_dim * Input_depth_dim);
        t10 = b * (Output_depth_dim * Output_X_dim * Output_Y_dim);
        
        for(unsigned int m = 0; m < Output_depth_dim; m++){
            t7 = m * Mask_Y_dim*Mask_X_dim*Input_depth_dim;
            
            for (unsigned int od = 0; od < 1; od++) {	//Output Depth , for 3D convolution only
                
                for (unsigned int y = 0; y < Output_Y_dim; y++) {			//Output height
                    t2 = y*Stride_Y_dim;
                    t11 = y * (Output_depth_dim * Output_X_dim);
                    
                    for (unsigned int x = 0; x < Output_X_dim; x++) {			//Output Width
                        t5 = x*Stride_X_dim;
                        t12 = x * Output_depth_dim + m;
                        for (unsigned int off_y = 0; off_y < Mask_Y_dim; off_y++) {
                            t3 = t2 + off_y;
                            t8 = off_y * Mask_X_dim*Input_depth_dim;
                            
                            for (unsigned int off_x = 0; off_x < Mask_X_dim; off_x++) {
                                t6 = (t5 + off_x) * Input_depth_dim;
                                t9 = off_x*Input_depth_dim;
                                
                                for(unsigned int d = 0; d < Input_depth_dim; d+=8) {
                                
                                    in_subscript = t1 + t3 * t4 + t6 + d;
                                    filter_subscript = t7 + t8 + t9 + d;
				     
                                    temp += in_FP[in_subscript] * filter_FP[filter_subscript];
                                    temp += in_FP[in_subscript+1] * filter_FP[filter_subscript+1];
                                    temp += in_FP[in_subscript+2] * filter_FP[filter_subscript+2];
                                    temp += in_FP[in_subscript+3] * filter_FP[filter_subscript+3];    
                                    temp += in_FP[in_subscript+4] * filter_FP[filter_subscript+4];
                                    temp += in_FP[in_subscript+5] * filter_FP[filter_subscript+5]; 
                                    temp += in_FP[in_subscript+6] * filter_FP[filter_subscript+6];
                                    temp += in_FP[in_subscript+7] * filter_FP[filter_subscript+7];                                 
                                }
                            }
                        }


                        out_subscript = t10 + t11 + t12;
                        temp+=bias_array_FP[m];
                        
                        out_to_compare_with_FP[out_subscript] = Relu_float(temp);

                    }
                }
            }
        }
    }

    //printf("\n from unopt %d %d ",out_to_compare_with[0],out_to_compare_with[1]);
    return 0;

}

float Relu_float(const float temp){


    if (temp<0.0f)
        return 0.0f;
    else
        return temp;

}


