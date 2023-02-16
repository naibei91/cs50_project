#include <stdio.h>
#include <cs50.h>
int multiplication(int z);

int main (void)
{
 int z = get_int("what is the size of the multiplication table? ");
 multiplication(z);
}

int multiplication(int z)
{
    for (int i=1;i <=z;i++)
     {
        for (int j=1;j<=z;j++)
        {
            printf("%4i",i*j);
        }
        printf("\n");
     }
}