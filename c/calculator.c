#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int x = get_float("Enter fitrst value:");
    int y = get_float("Enter second value:");
   // float a = x+y;
   // float b = x*y;
    //float c = x-y;
    float d = (float)x/(float)y;
    //int e = x%y;

    //printf("Sum of %.2f and %f is %f\n",x,y,a);
    //printf("Multiplication of %.2f and %f is %f\n",x,y,b);
    //printf("Substraction of %f and %.f is %f\n",x,y,c);
    printf("Division of %i and %i is %.2f\n",x,y,d);
    //printf("Remainder of %f and %f is %f",x,y,e);
}