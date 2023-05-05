#include <stdio.h>
#include <cs50.h>
int length(string name1);
int print(int x);

int main(void)
{
    string name=get_string("what is your name?");
    int n =length(name);
    print(n);
}
int length(string name1)
    {
    int number=0;
    for (int i = 0;name1[i]!='\0';i++)
    {
        number++;
    }
    return number;
    }

int print(int x)
    {
    printf("%i\n", x);
    return 0;
    }