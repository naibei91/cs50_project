#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
contact;

int main (void)
{
    string names = get_string("Type name: ");

    contact[0].name= "Brian";
    contact[0].number="0724846398";

    contact[1].name="Amos";
    contact[1].number="0724846398";

    for(int i=0;i<2;i++)
    {
        if(strcmp(names,contact.name)==0)
        {
        printf("%s:/n%s:/n",contact[i].name,contact[i].number);
        return 0;
        }
        else
        return 1;
    }


}