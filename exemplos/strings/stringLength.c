#include <stdio.h>

int stringLength(const char *s);

void main () {
  char string[] = "string de comprimento 24";

  printf("o comprimento da string é: %d\n", stringLength(string));
}

int stringLength(const char *string) {
  int c = 0;
  while (string[c]) {
    c++;
  }
  return c;
}
