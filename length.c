#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name=get_string("what is your name?");
    int number=0;


    for (int i = 0;name[i]!='\0';i++)
    {
        number++;
    }
    printf("%i\n", number);


}