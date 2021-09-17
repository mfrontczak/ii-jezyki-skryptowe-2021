# Laboratorium 1

## Wprowadzenie
**Python** - Język skryptowy (język programowania wysokiego poziomu) ogólnego przeznaczenia. Do jego głównych cech zalicza się wysoką czytelność kodu źródłowego. Wspiera [programowanie wielo-paradygmatowe](https://pl.wikipedia.org/wiki/Paradygmat_programowania).

### Przykład kodu w C

Przykład 1:
```C
#include <stdio.h>

int main() {
  printf("Hello World from C\n");
  return 0;
}
```

Przykład 2:
```C
#include <stdio.h>

int main() {
  int array[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  for(int i = 0; i < 10; i++) {
    printf("%d\n", array[i]);
  }
  return 0;
}
```

### Przykład kodu w Pythonie

Przykład 1
```python
print("Hello World from Python")
```

Przykład 2
```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in arr:
    print(i)
```
