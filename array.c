#include <stdio.h>
#include <cs50.h>

int number(void);
float average(int a,int array[]);
int print(int c);

int main (void)
{

    int n = number();
    int scores
    int a = average(n,scores);
    int b = print(a);

}

int number(void)
{
    int x=get_int("How many number do you want to find the average for? ");
    return x;
}

float average(int a,int array[])

{
    for (int j=0;j<a;j++)
    {
       int array[j]=get_int("score: ");
    }
    for (int i=0;i<a;i++)
    {
        int sum;
        sum  = sum + array[i];
    }
    return (float)sum/a;
}

void print(int c)
{
    printf ("The average is %f\n",c);
}