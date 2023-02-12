#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int a = get_int ("a : ");
    if(a%2==0)
    {
        printf("even\n");
    }
    else
    {
        printf("odd\n");
    }
}