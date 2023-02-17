#include <stdio.h>
#include <cs50.h>

int main (void)

{
    int n = get_int("How many scores do you have ? \n");
    int scores[n];
    for(int i=0;i<n;i++)
    {
    scores[i]=get_int("Score: ");
    }

    printf("Average of your scores : %f\n",(scores[0]+scores[1]+scores[2])/3.0);

}