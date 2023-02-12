# include <stdio.h>
# include <cs50.h>
void meow (int n);

int main(void)

    {
        int n = get_int("How many meows do you want? ");
        meow(n);
    }

    void meow (n)
{
    for(int i=0;i < n;i++)
    {
    printf("meow\n");
    }
}