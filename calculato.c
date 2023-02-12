#include <stdio.h>
#include <cs50.h>
int main (void)
{
    int a = get_int("Enter your first value:");
    int b=get_int("Enter your second value:");
    printf("sum of %i and %i is %i \n",a,b,a+b);
}