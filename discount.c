#include <cs50.h>
#include <stdio.h>

int main (void)
{
    float regular = get_float("What is the regular price?");
    float sale = regular * .85;
    printf("Current price : %.2f\n",sale);
}