#include <stdio.h>
#include <cs50.h>
#include <string.h>

datatype struct
{
    string name;
    string number;
}
contact;

int main void
{
    string names = get_strng("Type name: ");

    contact.name[0]= "Brian";
    contact.number[0]="0724846398";

    contact.name[1]="Amos";
    contact.number[1]="0724846398";

    for(int i=0;i<2;i++)
    {
        if(strcmp(names,contact.name)==0)
        {
        printf("%s:/n%s:/n",contact.name[i],contact.number[i]);
        return 0;
        }
        else
        return 1;
    }


}