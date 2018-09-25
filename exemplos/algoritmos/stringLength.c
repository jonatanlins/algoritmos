#include <stdio.h>
#include <stddef.h> /* para size_t */

size_t stringLength(const char *s);

void main () {
  char string[] = "string de comprimento 24";

  printf("o comprimento da string é: %d\n", stringLength(string));
}

size_t stringLength(const char *string) {
    const char *pointer = string;
    while (*string) string++;
    return string - pointer;
}
