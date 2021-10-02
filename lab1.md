# Języki Skryptowe - Lab 1

**Legenda:**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

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
def oblicz_delte(a, b, c):
    return b*b - 4*a*c


print("delta dla a=1, b=2, c=1 wynosi: {}".format(oblicz_delte(1,2,1)))
```
**Zadanie**
1. ✏️ Zainstaluj środowisko Anaconda/Python.
2. ✏️ Zainstaluj moduł ipython. :mag:
2. ✏️ Zapoznaj się z dokumentacją opisującą moduł `timeit` (https://docs.python.org/3/library/timeit.html).
3. ✏️ Uruchom ipython i wykonaj następujący kod: 
```python
import this
```

### Zmienna

Nazwa zmiennej jest obarczona pewnymi ograniczeniami - nie może zaczynać się od cyfry ani zawierać znaków specjalnych. Zalecane jest nazewnictwo zgodne z przeznaczeniem lub informacją którą ma przechowywać dana zmienna. 

:warning: W Pythonie typ zmiennej jest określany w trakcie przypisania wartości i może się zmienić (jest dynamiczny:dash:). 

```python
zmienna1 = 'Paweł'    # jest to teraz zmienna typu str (String - Łańcuch znakowy)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 12345      # teraz typ zostanie określony na int (Integer - liczba całkowita)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 0.4533113  # nowy typ na podstawie przypisania wartości do zmiennej będzie: float (liczba zmienno przecinkowa)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
```

### Standardowe typy danych

#### Proste 
```python
# łancuchy znakowe
str   # string - łańcuch znakowy

# numeryczne
int      # integer - liczba całkowita
float    # floating point number - liczba zmienno przecinkowa
complex  # complex - liczb zespolona
```

przykład:
```python
imie = 'Michał'             # zmienna przechowująca łańcuch znakowy Michał (typ str)
liczba_calkowita = 5        # zmienna przechowująca wartość liczbową 5 (typ int)
liczba_rzeczywista = 3.44   # zmienna przechowująca liczbę rzeczywistą 3.44 (typ float)
prawda = True               # zmienna przechowująca wartość logiczną (typ bool)
c = 1 + 3j                  # zmienna przechowująca liczbę zespoloną (typ complex) 
```

#### Struktury danych
Prócz prostych typów danych, można jeszcze wyróżnić:
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
l[3]

d = {     # słownik (mapa klucz-wartość)
  'klucz1': 'ala ma kota',
  'klucz2': 'płotek',
  'moja_lista': l,
  5: 'pięć'
}

d['klucz1']
d[5]

s = set([1, 3, 5, 3, 2, 1, 1, 1])  # zbiór unikalnych wartości
s
s.add(10)
s

t = (1, 4, 5, 3, 2, 1)  # tuple - krotka
t
t[1]

fs = frozenset([1, 3, 4, 3, 3, 2, 1])  # niemodyfikowany zbiór
fs
```

**Problem**

✏️ zapisz elementy krotki/listy/zbioru do osobnych zmiennych. 

🔍 Poszukaj o rozpakowywaniu zmiennych (unpacking).

```python
t = (5, 'kot', '12,333', 11223)
l = ['2021-10-02', '2021-10-09', '2021-10-16', '2021-10-23', '2021-10-30', '2021-11-06', '2021-11-13', '2021-11-20']
s = {5, 6, 7, 9, 10, 10, 11}

person_info = ['Imię', 'Nazwisko', (2001, 9, 11)]
```

**Zadanie** 

✏️ Sprawdź wydajność poszczególnych struktur danych dla różnych danych.


---
:book: Proszę przeczytać https://docs.python.org/3/library/stdtypes.html, aby dowiedzieć się więcej.


### Wbudowane funkcje

:memo: Wybrane wbudowanych funkcje które warto znać:
* [print](https://docs.python.org/3/library/functions.html#print)
* [input](https://docs.python.org/3/library/functions.html#input)
* [range](https://docs.python.org/3/library/functions.html#func-range)
* [len](https://docs.python.org/3/library/functions.html#len)
* [help](https://docs.python.org/3/library/functions.html#help)
* [type](https://docs.python.org/3/library/functions.html#type)
* [dir](https://docs.python.org/3/library/functions.html#dir)
* [globals](https://docs.python.org/3/library/functions.html#globals)
* [locals](https://docs.python.org/3/library/functions.html#locals)
* [id](https://docs.python.org/3/library/functions.html#id)
* [hash](https://docs.python.org/3/library/functions.html#hash)
* [hasattr](https://docs.python.org/3/library/functions.html#hasattr)
* [getattr](https://docs.python.org/3/library/functions.html#getattr)
* [isinstance](https://docs.python.org/3/library/functions.html#isinstance)

---
:book: Proszę przeczytać https://docs.python.org/3/library/functions.html, aby dowiedzieć się więcej.

### Sterowanie przebiegiem programu

Instrukcja warunkowa `if`:

przykład 1:
```python
x = 11
if x > 10:
    print("x jest większe niż 10")
elif x == 10:
    print("x jest równe 10")
else:
    print("x jest mniejsze niż 10")
```

przykład 2:
```python
x = 255
arr = [11, 255, 555, 100, 421]
if x in arr:
  pos = arr.index(x)
  print(f"x znajduje sie na pozycji {pos} w liście arr")
else:
  print(f"wartość {x} nie została znaleziona w liście")
```

Pętla `while`:
```python
i = 0
while i < 10:
    print(f"i = {i}")
    i += 1
```

Pętla `for`:

Przykład 1:
```python
for i in range(10):
    print(f"i = {i}")
```

Przykład 2:
```python
for slowo in ['ala', 'ma', 'kota']:
    print(f"{slowo}", end=" ")
```

Przykład 3:
```python
for conv in (int, float, str):
    print(f"{conv.__name__}(5.59) = {conv(5.59)}")
```

---
:book: Proszę przeczytać https://docs.python.org/3/tutorial/controlflow.html, aby dowiedzieć się więcej.


### Funkcje
W pythonie funkcje definiujemy przy użyciu słowa kluczowego `def` i nazwy.

Przykład 1:
```python
def say_hello():
    pass
    
say_hello()  # wywołanie funkcji bez argumentów
```

Przykład 2:
```python  
# przykład funkcji z jednym argumentem
def say_hello_to(name):
    print(f"Hello {name}")


say_hello_to('Johnny')  # wywołanie funkcji z jednym argumentem
```

#### funkcje z wieloma argumentami
Kolejne argumenty umieszczamy po przecinku.

Przykład 1:
```python
def sum_numbers(a, b, c, d, e):
    return a + b + c + d + e
```

Przykład 2:
```python
def sum_numbers(*args):
  ????
```

#### funkcje z domyślną wartością dla argumentów
Kiedy chcemy zdefinicować domyślną wartość argumentu, należy w trakcie definicji funkcji przypisać wartość domyślną dla danego argumentu.

⚠️ Argumenty z domyślną wartością muszą znajdować się na końcu.

Przykład 1:
```python
def call_math_func(a, b, c, d, e, func=sum):
    return func([a, b, c, d, e])
  

suma = call_math_func(1,2,3,4,5)  # domyślnie dla argumentu func zostanie przypisany adres funkcji sum.
mini = call_math_func(1,2,3,4,5, min)  # argument func przyjmie adres funkcji min.

print(suma)
print(mini)
```

Przykład 2:
```python
def multiple_x_by(x, multiplier=1):
  return x * multiplier


print(multiple_x_by(5))  # domyślną wartością dla multiplier będzie 1
print(multiple_x_by(6, 10)) # w tym przypadku wartość argumentu multiplier wynosi 10
print(multiple_x_by(7))  # domyślną wartością dla multiplier będzie 1
```

---
:book: Proszę przeczytać https://docs.python.org/3/tutorial/controlflow.html#defining-functions, aby dowiedzieć się więcej.

