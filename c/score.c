#include <stdio.h>
#include <cs50.h>

float average(int length,int array[]);

int main (void)

{
    int n = get_int("How many scores do you have ? \n");
    int scores[n];
    for(int i=0;i<n;i++)
    {
    scores[i]=get_int("Score: ");
    }
    float aver = average(n,scores);
    printf("Average of your scores : %f\n",aver);

}

float average(int length,int array[])
{
    int sum = 0;
    for(int j=0;j<length;j++)
    {
        sum = sum + array[j];
    }
    return sum/(float)length;
}

