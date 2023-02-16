#include <stdio.h>
int multiplication(void);

int main (void)
{
 int z = get_int("what is the size of the multiplication table? ");
 int multiplication(int z);
}

int multiplication(void)
{
    for (int i=1;i <=10;i++)
     {
        for (int j=1;j<=10;j++)
        {
            printf("%4i",i*j);
        }
        printf("\n");
     }
}