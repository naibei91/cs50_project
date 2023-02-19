#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main (void)
{
    string name = get_string("what is your name:");
    int length = strlen(name);
    printf("%i\n",length);
}