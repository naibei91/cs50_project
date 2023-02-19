#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name=get_string("what is your name?");



    for (int i = 0;name[i]!='\0';i++)
    {
        printf("%i\n", i);
    }
    
}