# Laboratorium 1

## Wprowadzenie
**Python** - Język skryptowy (język programowania wysokiego poziomu) ogólnego przeznaczenia. Do jego głównych cech zalicza się wysoką czytelność kodu źródłowego. Wspiera [programowanie wielo-paradygmatowe](https://pl.wikipedia.org/wiki/Paradygmat_programowania).


### Przykłady kodu w C

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

przykład 3:
```C
#include <stdio.h>
int oblicz_delte(short a, short b, short c) {
  return b*b - 4*a*c;
}

int main() {
  printf("delta dla a=1, b=2, c=1 wynosi: %d\n", delta(1, 2, 1));
  return 0;
}
```  

### Przykłady kodu w Pythonie

Przykład 1:
```python
print("Hello World from Python")
```

Przykład 2:
```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in arr:
    print(i)
```

przykład 3:
```python
def policz_delte(a, b, c):
  return b*b - 4*a*c
 
print("delta dla a=1, b=2, c=1 wynosi: {}".format(policz_delte(1,2,1))
```

### Zmienna

Nazwa zmiennej jest obarczona pewnymi ograniczeniami - nie może zaczynać się od cyfry ani zawierać znaków specjalnych. Zalecane jest nazewnictwo zgodne z przeznaczeniem lub informacją którą ma przechowywać dana zmienna. 

:exclamation: Należy pamiętać, że w Pythonie typ zmiennej jest określany w trakcie przypisania wartości i może się zmienić (jest dynamiczny:dash:). :exclamation:

```
zmienna1 = 'Paweł'    # jest to teraz zmienna typu str (String - Łańcuch znakowy)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 12345      # teraz typ zostanie określony na int (Integer - liczba całkowita)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 0.4533113  # nowy typ na podstawie przypisania wartości do zmiennej będzie: float (liczba zmienno przecinkowa)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
```

#### Podstawowe typy zmiennych
```python
str
int
float
bool
complex
```

przykład:
```python
imie = 'Michał'             # zmienna przechowująca łańcuch znakowy Michał (typ str)
liczba_calkowita = 5        # zmienna przechowująca wartość liczbową 5 (typ int)
liczba_rzeczywista = 3.44   # zmienna przechowująca liczbę rzeczywistą 3.44 (typ float)
prawda = True               # zmienna przechowująca wartość logiczną (typ bool)
c = 1 + 3j                  # zmienna przechowująca liczbę zespoloną (typ complex) 
```

#### Struktury dane
Prócz podstawowych typów danych, można jeszcze wyróżnić:
```python
list      # tablica gdzie kluczem jest indeks (wartość całkowita) 
dict      # słownik gdzie kluczem może być dowolna wartość - niemodyfikowalna - czyli taka z której można wygenerować unikalny hash
set       # zbiór unikalnych wartości, kluczem jest indeks
tuple     # krotka niemodyfikowalna tablica (lista)
frozenset # zbiór, niemodyfikowalny
```

przykład:
```python
l = [1, 2, 3, 4]  # lista

>>> l[3]
4

d = {     # słownik (mapa klucz-wartość)
  'klucz1': 'ala ma kota',
  'klucz2': 'płotek',
  'moja_lista': l,
  5: 'pięć'
}

>>> d['klucz1']
'ala ma kota'
>>> d[5]
'pięć'

s = set([1, 3, 5, 3, 2, 1, 1, 1])
>>> s
{1, 2, 3, 5}
>>> s.add(10)
>>> s
{1, 2, 3, 5, 10}

t = (1, 4, 5, 3, 2, 1)
>>> t
(1, 4, 5, 3, 2, 1)
>>> t[1]
4


fs = frozenset([1, 3, 4, 3, 3, 2, 1])
>>> fs
frozenset({1, 2, 3, 4})

```

**type hinting**
Nowa wersja pythona 3.X wspiera type hinting - programista może wykorzystać go do poinformowania innego programisty (nie jest to wymuszone, a jedynie sugestią) jakiego typu 
dane powinny zostać przekazane do funkcji (lub metody), oraz jakiego typu wartość jest zwracana przez funkcję (lub metode). 
```python
def say_my_name(name: str) -> None:
    print(f"My name is ... {name}")
```
więcej można przeczytać tutaj: https://docs.python.org/3/library/typing.html


### Zadanie
Zainstaluj środowisko Anaconda. 
Dla systemu windows: https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe
alternatywa: https://www.anaconda.com/products/individual


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
