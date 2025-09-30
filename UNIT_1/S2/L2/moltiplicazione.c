#include <stdio.h>

int main () {

    float num1, num2;
    float risultato;

    printf("inserisci primo numero: ");
    scanf("%f", &num1);

    printf("inserisci secondo numero: ");
    scanf("%f", &num2);

    risultato = num1*num2;

    printf ("la moltiplicazione tra %f e %f è: %f", num1, num2, risultato); 

    return 0;
}