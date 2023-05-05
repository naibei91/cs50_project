#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int n;

    do
    {
    n = get_int("size?");
    }
    while (n<1);
    //for row
    for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)   //for column
            {
                printf("#");
            }
        //MOVE TO NEXT ROW
        printf("\n");
    }

}