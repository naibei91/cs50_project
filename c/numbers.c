#include <stdio.h>
#include <cs50.h>
void count (int a);

int main(void)
{
    for (int a=1;a<11;a++)
    {
        count(a);
    }
}

void count (int a)
    {
     printf("%i\n",a);
     a++;
    }