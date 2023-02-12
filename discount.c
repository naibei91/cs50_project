#include <cs50.h>
#include <stdio.h>
float discount (float price,int percentage);

int main (void)
{
    float regular = get_float("What is the regular price?");
    int percent_off = get_int("What percentage do you want to take of?");
    float sale = discount(regular,percent_off);
    printf("Current price : %.2f\n",sale);
}


float discount(float price,int percentage)
{
    return price * (100-percentage)/100;
}