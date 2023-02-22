#include <stdio.h>
#include <cs50.h>

int get_number(void);
void print (int a);

int main (void)
{
   int numb = get_number();
   print(numb);
}

int get_number(void)
{
    int number = get_int("To what number do you want to count?");
    return number;
}

void print (int a)
{
    for(int i=1;i<=a;i++)
    {
        for(int j=0;j<i;j++)
        {
        int x = a-j;
        printf("%i",i);
        }
        printf("\n");
    }
}