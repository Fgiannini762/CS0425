#include <stdio.h>

int main (){

    float num1, num2;
    float media;

    printf("inserisci il primo numero: ");
    scanf("%f", &num1);

    printf ("inserisci il secondo numero: ");
    scanf("%f", &num2);

    media = (num1+num2) /2;

    printf("la media tra %f e %f è: %f", num1, num2, media);

    return 0;
}