# J臋zyki Skryptowe - Lab 1

**Legenda**

馃摉 - prosz臋 przeczyta膰

馃摑 - warte zapami臋tania / zanotowania

鈿狅笍 - zwr贸膰 uwag臋

鉁忥笍 - zadanie do wykonania

馃攳 - poszukaj w internecie

## Wprowadzenie
**Python** - J臋zyk skryptowy (j臋zyk programowania wysokiego poziomu) og贸lnego przeznaczenia. Do jego g艂贸wnych cech zalicza si臋 wysok膮 czytelno艣膰 kodu 藕r贸d艂owego. Wspiera [programowanie wielo-paradygmatowe](https://pl.wikipedia.org/wiki/Paradygmat_programowania).

---

W przyk艂adach b臋dzie u偶yty :book: [f-string](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting) s艂u偶膮cy do formatowania tekstu.

Wszystkie udost臋pnione fragmentu kodu mo偶na skopiowa膰 i uruchomi膰 w konsoli python'a.

### Przyk艂ady kodu w C i Pythonie

Przyk艂ad 1 - wy艣wietlenie tekstu na ekranie:

**Kod w C**
```C
#include <stdio.h>

int main() {
  printf("Hello World from C\n");
  return 0;
}
```

**Kod w Pythonie**
```python
print("Hello World from Python")
```

Przyk艂ad 2 - obs艂uga p臋tli:

**Kod w C**
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

**Kod w Pythonie**
```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in arr:
    print(i)
```

przyk艂ad 3 - definicja funkcji:

**Kod w C**
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

**Kod w Pythonie**
```python
def oblicz_delte(a, b, c):
    return b*b - 4*a*c


print("delta dla a=1, b=2, c=1 wynosi: {}".format(oblicz_delte(1,2,1)))
```

### Zarz膮dzanie modu艂ami w Pythonie
W Pythonie modu艂em nazywamy plik kt贸re udost臋pnia nam zbi贸r funkcji i/lub klas. 
Modu艂 importujemy przy u偶yciu s艂owa kluczowego `import`, na przyk艂ad:
```python
import os
import sys
import pdb
```

Python domy艣lnie udost臋pnia standardowa biblioteka modu艂贸w pozwalaj膮ca nam od razu rozpocz膮膰 programowanie.

W przypadku kiedy chcemy wykorzysta膰 modu艂 kt贸ry nie znajduje si臋 w standardowej bibliotece, mo偶emy skorzysta膰 z narz臋dzia `pip` do zarz膮dzania modu艂ami.

Wi臋cej o projekcie i dost臋pnych modu艂ach mo偶na znale藕膰 na https://pypi.org/.

#### :memo: Lista przydatnych komend

lista zainstalowanych modu艂贸w:
```bash
pip list
```
lista zainstalowanych modu艂贸w w sk艂adni dla komendy `pip install -r`.
```bash
pip freeze > requirements.txt  # zapisujemy informacj臋 zainstalowanych modu艂ach do pliku requirements.txt
```

instalacja nowego modu艂u:
```bash
pip install [--user] [-U] nazwa_pakietu[==konkretna wersja]
pip install -r requirements.txt   # instalujemy list臋 pakiet贸w kt贸re znajduj膮 si臋 w pliku requirements.txt
```

Usuni臋cie modu艂u z 艣rodowiska:
```bash
pip uninstall nazwa_pakietu
pip uninstall -r requirements.txt  # usunie list臋 pakiet贸w kt贸re znajduj膮 si臋 w pliku requirements.txt
```

**Zadanie**
1. 鉁忥笍 Zainstaluj 艣rodowisko Anaconda/Python 3.8.
2. 鉁忥笍 Zainstaluj modu艂 `ipython`. :mag:
3. 鉁忥笍 Zapoznaj si臋 z dokumentacj膮 opisuj膮c膮 modu艂 `timeit` (https://docs.python.org/3/library/timeit.html).
4. 鉁忥笍 Uruchom `ipython` i wykonaj nast臋puj膮cy kod: 
```python
import this
```

### Zmienna

Nazwa zmiennej jest obarczona pewnymi ograniczeniami - nie mo偶e zaczyna膰 si臋 od cyfry ani zawiera膰 znak贸w specjalnych. Zalecane jest nazewnictwo zgodne z przeznaczeniem lub informacj膮 kt贸r膮 ma przechowywa膰 dana zmienna. 

:warning: W Pythonie typ zmiennej jest okre艣lany w trakcie przypisania warto艣ci i mo偶e si臋 zmieni膰 (jest dynamiczny:dash:). 

```python
zmienna1 = 'Dawid Rybka'    # jest to teraz zmienna typu str (String - 艁a艅cuch znakowy)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 12345      # teraz typ zostanie okre艣lony na int (Integer - liczba ca艂kowita)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 0.4533113  # nowy typ na podstawie przypisania warto艣ci do zmiennej b臋dzie: float (liczba zmienno przecinkowa)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
```

### Standardowe typy danych

#### Proste 
```python
# 艂ancuchy znakowe
str   # string - 艂a艅cuch znakowy

# numeryczne
int      # integer - liczba ca艂kowita
float    # floating point number - liczba zmienno przecinkowa
complex  # complex - liczb zespolona
```

przyk艂ad:
```python
imie = 'Micha艂'             # zmienna przechowuj膮ca 艂a艅cuch znakowy Micha艂 (typ str)
liczba_calkowita = 5        # zmienna przechowuj膮ca warto艣膰 liczbow膮 5 (typ int)
liczba_rzeczywista = 3.44   # zmienna przechowuj膮ca liczb臋 rzeczywist膮 3.44 (typ float)
prawda = True               # zmienna przechowuj膮ca warto艣膰 logiczn膮 (typ bool)
c = 1 + 3j                  # zmienna przechowuj膮ca liczb臋 zespolon膮 (typ complex) 
```

#### Struktury danych
Pr贸cz prostych typ贸w danych, mo偶na jeszcze wyr贸偶ni膰:
```python
list      # tablica gdzie kluczem jest indeks (warto艣膰 ca艂kowita) 
dict      # s艂ownik gdzie kluczem mo偶e by膰 dowolna warto艣膰 - niemodyfikowalna - czyli taka z kt贸rej mo偶na wygenerowa膰 unikalny hash
set       # zbi贸r unikalnych warto艣ci, kluczem jest indeks
tuple     # krotka niemodyfikowalna tablica (lista)
frozenset # zbi贸r, niemodyfikowalny
```

przyk艂ad:
```python
l = [1, 2, 3, 4]  # lista
print(l[3])
l.append(6)
print(l)

d = {     # s艂ownik (mapa klucz-warto艣膰)
  'klucz1': 'ala ma kota',
  'klucz2': 'p艂otek',
  'moja_lista': l,
  5: 'pi臋膰'
}

d['klucz1']
print(d[5])
# ma艂a modyfikacja
d[5] = 'sze艣膰'
print(d[5])

s = set([1, 3, 5, 3, 2, 1, 1, 1])  # zbi贸r unikalnych warto艣ci
print(s)
s.add(10)
print(s)

t = (1, 4, 5, 3, 2, 1)  # tuple - krotka
print(t)
print(t[1])

fs = frozenset([1, 3, 4, 3, 3, 2, 1])  # niemodyfikowany zbi贸r
print(fs)
```

Przyk艂ad 2:
```python
l = [1, 2, 3, 4]
l[0] = '2'
print(l)
```
Przyk艂ad 3 (powinni艣my otrzyma膰 b艂膮d):
```python
t = (1, 4, 5, 3, 2, 1)
t[1] = 10
print(t)
```

Przyk艂ad 4 (te偶 nie dzia艂a):
```python
s = {1, 4, 5, 3, 2, 1}  # alternatywna sk艂adnia do (nie myli膰 z s艂ownikiem): set([1, 4, 5, 3, 2, 1])
s[1] = 10
print(s)
```

**Problem**

鉁忥笍 Jak zmodyfikowa膰 krotk臋 / zbi贸r? 

馃攳 Poszukaj rozwi膮zania w sieci.


**Problem**

鉁忥笍 zapisz elementy krotki/listy/zbioru do osobnych zmiennych. 

馃攳 Poszukaj o rozpakowywaniu sekwencji (unpacking).

```python
t = (5, 'kot', '12,333', 11223)
l = ['2021-10-02', '2021-10-09', '2021-10-16', '2021-10-23', '2021-10-30', '2021-11-06', '2021-11-13', '2021-11-20']
s = {5, 6, 7, 9, 10, 10, 11}

person_info = ['Imi臋', 'Nazwisko', (2001, 9, 11)]
```

**Zadanie** 

鉁忥笍 Sprawd藕 wydajno艣膰 poszczeg贸lnych struktur danych dla r贸偶nych typ贸w danych. (wykorzystaj do tego modu艂 `timeit`)

**Zadanie** 

鉁忥笍 Stw贸rz list臋 w kt贸rej b臋d膮 wyniki du偶ego lotka.

**Zadanie** 

鉁忥笍 Stw贸rz s艂ownik (`dict`) w kt贸rym b臋dziesz przechowywa艂 informacj臋 o ilo艣ci schronisk w danym mie艣cie dla miast (kluczy): Krak贸w, Warszawa, Pozna艅.

**Zadanie** 

鉁忥笍 W Poznaniu i Krakowie wybudowano nowe schronisko, w Warszawie wybudowano a偶 trzy. 
W poprzednio utworzonym s艂owniku (`dict`) zaktualizuj informacj臋 o liczbie schronisk.

**Zadanie** 

鉁忥笍 Do naszego s艂ownika z informacj膮 o schroniskach dodaj nowe miasto Rzesz贸w z liczb膮 schronisk 3.


**Zadanie** 

鉁忥笍 Stw贸rz s艂ownik w kt贸rym kluczami b臋d膮 daty w formacie 'YYYY-MM-DD', a warto艣ciami wyniki du偶ego lotka. 
Wykonaj zadanie dla ostatnich 3 losowa艅 (albo wprowad藕 w艂asne liczby).

**Zadanie** 

鉁忥笍 Korzystaj膮c z funkcji `input()` popro艣 u偶ytkownika o miasto (klucz) dla kt贸rego chce wy艣wietli膰 informacje o liczbie schronisk.


---
馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3/library/stdtypes.html, aby dowiedzie膰 si臋 wi臋cej.


### Sterowanie przebiegiem programu

Instrukcja warunkowa `if`:

przyk艂ad 1:
```python
x = 11
if x > 10:
    print("x jest wi臋ksze ni偶 10")
elif x == 10:
    print("x jest r贸wne 10")
else:
    print("x jest mniejsze ni偶 10")
```

przyk艂ad 2:
```python
x = 255
arr = [11, 255, 555, 100, 421]
if x in arr:
  pos = arr.index(x)
  print(f"x znajduje sie na pozycji {pos} w li艣cie arr")
else:
  print(f"warto艣膰 {x} nie zosta艂a znaleziona w li艣cie")
```

**Problem**

鉁忥笍 W Pythonie nie istnieje instrukcja `switch`. Spr贸buj j膮 zasymulowa膰.

P臋tla `while`:
```python
i = 0
while i < 10:
    print(f"i = {i}")
    i += 1
```

P臋tla `for`:

Przyk艂ad 1:
```python
for i in range(10):
    print(f"i = {i}")
```

Przyk艂ad 2:
```python
for slowo in ['ala', 'ma', 'kota']:
    print(f"{slowo}", end=" ")
```

Przyk艂ad 3:
```python
for conv in (int, float, str):
    print(f"{conv.__name__}(5.59) = {conv(5.59)}")
```

---
:book: Prosz臋 przeczyta膰 https://docs.python.org/3/tutorial/controlflow.html, aby dowiedzie膰 si臋 wi臋cej.


### Funkcje

#### Wbudowane funkcje

:memo: Wybrane wbudowanych funkcje kt贸re warto zna膰:
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

Przyk艂ad 1:
```python
name = input("Jak masz na imi臋? ")
name_len = len(name)
print(f"{name} to wspania艂e imie! Twoje imie ma {name_len} znak贸w.")
```

Przyk艂ad 2:
```python
age = int(input("Ile masz lat? "))
age_cpy = age

print(f"id({age}) = {id(age)}")
print(f"id({age_cpy}) = {id(age_cpy)}")
```

Przyk艂ad 3 (z b艂臋dem - bez rzutowania na int):
```python
age = input("Ile masz lat? ")
age_in_10_years = age + 10
print(f"dzi艣 mam {age} a za 10 lat b臋d臋 mia艂 {age_in_10_years}")
```

---
:book: Prosz臋 przeczyta膰 https://docs.python.org/3/library/functions.html, aby dowiedzie膰 si臋 wi臋cej.

#### definiowanie w艂asnych funkcji
W pythonie funkcje definiujemy przy u偶yciu s艂owa kluczowego `def` i nazwy.

Przyk艂ad 1:
```python
def say_hello():
    pass
    
say_hello()  # wywo艂anie funkcji bez argument贸w
```

Przyk艂ad 2:
```python  
# przyk艂ad funkcji z jednym argumentem
def say_hello_to(name):
    print(f"Hello {name}")


say_hello_to('Johnny')  # wywo艂anie funkcji z jednym argumentem
```

#### Funkcje z wieloma argumentami
Kolejne argumenty umieszczamy po przecinku (argumenty pozycyjne). Je偶eli chcemy by nasza funkcja przyjmowa艂a dowoln膮 ilo艣膰 argument贸w (pozycyjnych) mo偶emy u偶y膰  `*args`.

Przyk艂ad 1:
```python
def sum_numbers(a, b, c, d, e):
    return a + b + c + d + e
```

Przyk艂ad 2:
```python
def sum_numbers(*args):
    result = 0
    for number in args:
        result += number
    return result
```
Istnieje r贸wnie偶 mo偶liwo艣膰 obs艂ugi dowolnej ilo艣ci nazwanych argument贸w, z wykorzystaniem `**kwargs`.

Przyk艂ad:
```python
d = {}
def add_marks(student, **kwargs):
    d[student] = kwargs


add_marks('Kowalski', JezykiSkryptowe=3, JezykiProgramowania=4, WF=5)
add_marks('Nowak', JezykiSkryptowe=2, JezykiProgramowania=3, WF=4)

print(d)
```
#### Funkcje z domy艣ln膮 warto艣ci膮 dla argument贸w
Kiedy chcemy zdefiniowa膰 domy艣ln膮 warto艣膰 argumentu, nale偶y w trakcie definicji funkcji przypisa膰 warto艣膰 domy艣ln膮 dla danego argumentu.

鈿狅笍 Argumenty z domy艣ln膮 warto艣ci膮 musz膮 znajdowa膰 si臋 na ko艅cu.

Przyk艂ad 1:
```python
def foo(a, b, c=0):
    res = 1
    if a > 1:
        res *= a
    if b > 1:
        res *= b
    if c > 1:
        res *= c
    else:
        res *= -1
    return res



bar = foo(3,2,5)  
print(bar)

bar = foo(5,3)  
print(bar)
```

Przyk艂ad 2:
```python
def multiple_x_by(x, multiplier=1):
  return x * multiplier


print(multiple_x_by(5))  # domy艣ln膮 warto艣ci膮 dla multiplier b臋dzie 1
print(multiple_x_by(6, 10)) # w tym przypadku warto艣膰 argumentu multiplier wynosi 10
print(multiple_x_by(7))  # domy艣ln膮 warto艣ci膮 dla multiplier b臋dzie 1
```


**Zadanie** 

鉁忥笍 Napisz funkcj臋 kt贸ra poprosi u偶ytkownika o jego dane osobowe jak imi臋, nazwisko, wiek. Zaproponuj kt贸r膮 z struktur danych do tego u偶y膰.

鉁忥笍 Napisz funkcj臋 kt贸ra przyjmie dwie warto艣ci liczbowe i zwr贸ci wi臋ksz膮 z nich (u偶yj funkcji wbudowanej `max`).

鉁忥笍 Napisz funkcj臋 kt贸ra przyjmie list臋 liczb jako argument i zwr贸ci sum臋 liczb znajduj膮cych si臋 w li艣cie.

鉁忥笍 Napisz funkcj臋 kt贸ra przyjmie dowolnie d艂ug膮 list臋 liczb (u偶yj `*args`) i zwr贸ci warto艣膰 najmniejsz膮 (u偶yj funkcji wbudowanej `min`).

鉁忥笍 Napisz funkcj臋 kt贸ra przyjmie od u偶ytkownika dane: imie (`str`), nazwisko (`str`), grupa (`str`), obecny (`bool`) i zapisze je do globalnej listy student贸w.

---
:book: Prosz臋 przeczyta膰 https://docs.python.org/3/tutorial/controlflow.html#defining-functions, aby dowiedzie膰 si臋 wi臋cej.
