#include <stdio.h>
#include <cs50.h>
void multiplication(int z);
void division(float z);
int get_value(void);

int main (void)
{
 int z = get_value();
 multiplication(z);
 division((float)z);
}


void multiplication(int z)
{
    do
    {
    printf("multiplication Table\n");
    for (int i=1;i <=z;i++)
     {
        for (int j=1;j<=z;j++)
        {
            printf("%4i",i*j);
        }
        printf("\n");
     }
    }
    while(z=0);
}

int get_value(void)
{
    int z = get_int("what is the size of the multiplication table? ");
    return z;
}

void division(float z)
{
    printf("division Table\n");
    for (float i=1;i <=z;i++)
     {
        for (float j=1;j<=z;j++)
        {
            printf("%7.2lf",j/i);
        }
        printf("\n");
     }
}