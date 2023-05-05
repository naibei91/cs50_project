#include <stdio.h>
#include <cs50.h>
int main (void)
{
    //the sum of two numbers
    long a = get_long("Enter your first value:"); //first input from user
    long b=get_long("Enter your second value:"); //second input from user
    printf("sum of %li and %li is %li \n",a,b,a+b); //output from summation of user input
}