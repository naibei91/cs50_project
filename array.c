#include <stdio.h>
#include <cs50.h>

int number(void);
float average(int a);
void print(float c);

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

float average(int a)

{
    int array[a];
    int sum=0;
    for (int j=0;j<a;j++)
    {
       array[j]=get_int("score: ");
    }
    for (int i=0;i<a;i++)
    {
        sum  = sum + array[i];
    }
    return sum/(float)a;
}

void print(float c)
{
    printf ("The average is %f\n",c);
}