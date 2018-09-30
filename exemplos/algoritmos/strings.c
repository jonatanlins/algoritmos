#include <stdio.h>


int stringLength (const char *s);
char *stringConcat (char *dest, const char *src);
char *stringCopy (char *dest, const char *src);


int main () {
  char string1[50] = "primeira string ";
  char string2[] = "segunda string";

  printf("A comprimento de '%s' é: %d\n", string1, stringLength(string1));
  printf("A comprimento da '%s' é: %d\n", string2, stringLength(string2));
  
  stringConcat(string1, string2);

  printf("A concatenação das duas é: %s\n", string1);

  stringCopy(string1, string2);

  printf("Copiando a segunda string para a primeira: %s\n", string1);

  return 0;
}


int stringLength (const char *string) {
  int c = 0;
  while (string[c]) {
    c++;
  }
  return c;
}


char *stringConcat (char *dest, const char *src) {
    int i, j;

    for (i = 0; dest[i] != '\0'; i++);

    for (j = 0; src[j] != '\0'; j++) {
      dest[i+j] = src[j];
    }

    dest[i+j] = '\0';
    return dest;
}


char *stringCopy (char *dest, const char *src) {
  int i;
  
  for (i = 0; src[i] != '\0'; i++) {
    dest[i] = src[i];
  }

  dest[i] = '\0';

  return dest;
}
