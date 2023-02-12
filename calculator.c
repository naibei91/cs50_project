#include <stdio.h>
#include <cs50.h>

int main (void)
{
    float x = get_float("Enter fitrst value:");
    float y = get_float("Enter second value:");
    float a = x+y;
    float b = x*y;
    float c = x-y;
    float d = x/y;
    float e = x%y;

    printf("Sum of %f and %f is %f",x,y,a);
    printf("Multiplication of %f and %f is %f",x,y,a);
    printf("Substraction of %f and %f is %f",x,y,a);
    printf("Division of %f and %f is %f",x,y,a);
    printf("Remaindr of %f and %f is %f",x,y,a);
}