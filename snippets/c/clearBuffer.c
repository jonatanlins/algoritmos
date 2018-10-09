#include <stdio.h>


int main() {
    char text[100];
    
    // A expressão %[^\n]%*c serve para coletar todos os caracteres digitados,
    // ignorando o código do enter
    scanf("%[^\n]%*c", text);
    printf("%s\n", text);

    return 0;
}