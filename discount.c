#include <cs50.h>
#include <stdio.h>
float discount (float price);

int main (void)
{
    float regular = get_float("What is the regular price?");
    int percent =
    float sale = discount(regular);
    printf("Current price : %.2f\n",sale);
}


float discount(float price)
{
    return price * .85;
}