#include<stdio.h>
#include<stdlib.h>
#include<string.h> // function to determine length of string 
#include <time.h>


int main(int argc, char *argv[]){
    srand(time(NULL));
    int passLength;
    char char_symbols[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-=+`~[{]}\\|:;,./?";
    printf("\n================================ PASSWORD GENERATOR ================================\n");
    printf("\nEnter password length: ");
    scanf("%d", &passLength);
    /* length of password */
    char password[passLength -1];

    /*----for loop----*/
    printf("\n");
    for(int i = 0; i < passLength; i++){
        password[i] = char_symbols[rand()% strlen(char_symbols)];
        printf("%c", password[i]);
    }
    return 0;

}