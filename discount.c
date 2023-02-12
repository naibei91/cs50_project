#include <cs50.h>
#include <stdio.h>
float discount (float price,percentage);

int main (void)
{
    float regular = get_float("What is the regular price?");
    int percent_off = get_percent("What percentage do you want to take of?");
    float sale = discount(regular,percent_off);
    printf("Current price : %.2f\n",sale);
}


float discount(float price,percentage)
{
    return price * (100-percentge)/100;
}