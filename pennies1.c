#include <stdio.h>
#include <cs50.h>
float division (float a,float b);

int main(void)
{
    int x = get_float("get value of x:");
    int y = get_float("get value of y:");
    float z = division((float)x,(float)y);
    printf("the division of %i and %i is %f",x,y,z);

}

float division (float a,float b)
{
 return a/b;
}