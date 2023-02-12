#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //user to agree
    char x = get_char("Do you agree?");
    if (x == 'y'||x=='Y')
    {
        printf("Agreed\n");
    }
    else if (x == 'N'||x== 'n')
    {
        printf("Dis-agreed\n");
    }
    else
    {
        printf("Kindly type y to agree or n to disagree.\n");
    }
}