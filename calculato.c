#include <stdio.h>
#include <cs50.h>
int main (void)
{
    //the sum of two numbers
    int a = get_int("Enter your first value:"); //first input from user
    int b=get_int("Enter your second value:"); //second input from user
    printf("sum of %i and %i is %i \n",a,b,a+b); //output from summation of user input
}