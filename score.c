#include <stdio.h>
#include <cs50.h>

int average(int length,int array[]);

int main (void)

{
    int n = get_int("How many scores do you have ? \n");
    int scores[n];
    for(int i=0;i<n;i++)
    {
    scores[i]=get_int("Score: ");
    }
    int aver = int average(int n,int scores[n]);
    printf("Average of your scores : %f\n",aver);

}

int average(int length,int array[])
{
    for(int j=0;j<length;j++)
    {
        sum = sum + array[j];
    }
    return sum/(float)length;
}

