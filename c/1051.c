// Imposto de Renda
// Problema 1051 do URI Online Judge
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1051

#include <stdio.h>

void main() {
  float value;
  scanf("%f", &value);

  if (value <= 2000) {
    printf("Isento\n");
  } else if (value <= 3000) {
    printf("R$ %.2f\n", (value - 2000) * 0.08);
  } else if (value <= 4500) {
    printf("R$ %.2f\n", (value - 3000) * 0.18 + 1000 * 0.08);
  } else {
    printf("R$ %.2f\n", (value - 4500) * 0.28 + 1000 * 0.08 + 1500 * 0.18);
  }

  return 0;
}
