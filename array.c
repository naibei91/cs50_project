#include <stdio.h>
#include <cs50.h>

int number(void);
int average(int a,array[]);
int print(int c);

int main (void)
{
    int n = number();
    int a = average(n);
    int b = print(a);
}

int number(void)
{
    int x=get_int("How many number do you want to find the average for? ");
    return x;
}

int average(int a)

{
    for (int i=0;i<a;i++)
    {
        int score[i];
        int sum;
        sum  = sum + score[i];
    }
    return sum/a;
}

void print(int c)
{
    printf ("The average is %f\n",b);
}