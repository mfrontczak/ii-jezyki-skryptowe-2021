# Laboratorium 1

## Wprowadzenie
**Python** - Język skryptowy (język programowania wysokiego poziomu) ogólnego przeznaczenia. Do jego głównych cech zalicza się wysoką czytelność kodu źródłowego. Wspiera [programowanie wielo-paradygmatowe](https://pl.wikipedia.org/wiki/Paradygmat_programowania).

### Zmienna

Zmienną (variable) nazwany obszar w pamięci komputera pod którym można przechowywać dane. 
>Inaczej można sobie wyobrazić ją jako podpisane pudełko do którego możemy umieścić.

Nazwa zmiennej jest dowolna, jednak sugerowane jest nazywanie jest zgodnie z przeznaczeniem lub informacją którą ma przechowywać.
```python
imie = 'Michał'             # zmienna przechowująca łańcuch znakowy Michał (typ str)
liczba_calkowita = 5        # zmienna przechowująca wartość liczbową 5 (typ int)
liczba_rzeczywista = 3.44   # zmienna przechowująca liczbę rzeczywistą 3.44 (typ float)
prawda = True               # zmienna przechowująca wartość logiczną (typ bool)
```

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


### Zadania

Zapoznaj się z dokumentacją opisującą następujące wbudowane funkcje:

* [help](https://docs.python.org/3/library/functions.html#help)
* [print](https://docs.python.org/3/library/functions.html#print)
* [input](https://docs.python.org/3/library/functions.html#input)
* [len](https://docs.python.org/3/library/functions.html#len)
* [type](https://docs.python.org/3/library/functions.html#type)
* [dir](https://docs.python.org/3/library/functions.html#dir)


Korzystając z funkcji `help()` dowiedz się coś na temat:

* int
* float
* str
* print
* input
* len
