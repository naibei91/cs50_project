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
   // contact contacts[2];

    contact contacts[0].name= "Brian";
    contact contacts[0].number="0724846398";

    contacts[1].name="Amos";
    contacts[1].number="0724846398";

    for(int i=0;i<2;i++)
    {
        if(strcmp(names,contacts[i].name)==0)
        {
        printf("%s:\n%s:\n",contacts[i].name,contacts[i].number);
        return 0;
        }
        else
        return 1;
    }


}