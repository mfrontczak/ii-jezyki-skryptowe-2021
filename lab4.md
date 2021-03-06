# J臋zyki Skryptowe - Lab 4

**Legenda**

馃摉 - prosz臋 przeczyta膰

馃摑 - warte zapami臋tania / zanotowania

鈿狅笍 - zwr贸膰 uwag臋

鉁忥笍 - zadanie do wykonania

馃攳 - poszukaj w internecie


## Wyra偶enia regularne 
Wyra偶enia regularne s膮 mini j臋zykiem programowania kt贸ry pozwala nam na tworzenie wzorc贸w dopasowania. 
Modu艂em odpowiedzialny za udost臋nienie funkcjonalno艣ci dla wyra偶e艅 regularnych jest `re`.

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3/library/re.html.

馃摉 Prosz臋 przeczyta膰 https://pl.wikipedia.org/wiki/Wyra偶enie_regularne.

### meta-znaki 
Meta-znaki posiadaj膮 specjalne przeznaczenie w wyra偶eniach regularnych. 

| token/meta-znak  | Przeznaczenie | Przyk艂ad |
| ------------- | ------------- | ------------- |
| $  | ko艅czy si臋 ...  |  "python$" |
| ^  | zaczyna si臋 od ...   | "^Programowanie" |
| .  | dowolny znak | ".ot" |
| \*  | dopasowanie zach艂anne | "\*" |
| + | wyra偶enie wyst臋puje 1 lub wi臋cej razy | "\[a-z\]+" |
| ? | wyra偶enie wyst臋puje 0 lub 1 raz | "kot?" |
| {m} | wyra偶enie musi by膰 dok艂adnie `m` razy dopasowane | "\[abc\]{5}" |
| {n,m} | wyra偶enie musi by膰 dopasowane od `n` do `m` razy | "\a{3,5}" |
| {n,} | wyra偶enie musi by膰 dopasowane `n` lub wi臋cej razy | "\a{3,}" |
| \d | dopasowuje liczby | "\d?" |
| \D | dopasowuje wszystko pr贸cz liczb | "\D+" |
| \s | dopasowuje bia艂e znaki | "\s+" |
| \S | dopasowuje nie-bia艂e znaki | "\S+ \S+" |
| \w | dopasowuje dowolne s艂owo | "\w" |
| \W | dopasowuje wszystko pr贸cz s艂贸w | "\W+" |
| [] | kt贸ry艣 z znak贸w opisanych w nawiasach kwadratowych | "\[abc\]" |
| \[a-z\] | zakres znak贸w od a-z | "\[a-z\]+" |
| (...) | przechwy膰 wszystko co jest zawarte w nawiasach | "(\d)+" |
| a\|b  | dopasowuje `a` lub `b` | "(kot\|pies)" |

### Flagi
| Flaga         | Opis
| ------------- | ------------------------- |
| re.IGNORECASE | ignoruje wielko艣膰 znak贸w. |
| re.MULTILINE | Wyszukanie w wielu liniach. |
| re.ASCII | Tylko znaki ASCII, znaki UNICODE s膮 ignorowane. |
| re.DOTALL | Dopasowuje dowolny znak, nawet je偶eli jest to znak nowej linii. |

馃摉 Prosz臋 przeczyta膰 https://pl.wikipedia.org/wiki/Wyra%C5%BCenie_regularne#Wyra%C5%BCenia_zach%C5%82anne.

### Funkcja search
Funkcja `re.search(pattern, string, flags=0)` zwraca pierwszy zgodny z wzorcem 艂a艅cuch znakowy. 
Funkcja zwraca obiekt `re.Match` lub `None`.

Przyk艂ad 1:
```python
import re
p = '[a-z\.]+'
s = '-!!michal.frontczak(at)up.krakow.pl% %lub% %michal.frontczak@up.krakow.pl!!-'
r = re.search(p, s)
print(result.group()) # michal.frontczak
```

Przyk艂ad 2:
```python
import re
p = '.ome.'
s = 'domek'
r = re.search(p, s)
print(r.group())


s = 'Tomek'
r = re.search(p, s)
print(r.group())

s = 'Kometa'
r = re.search(p, s)
print(r.group())
```

Przyk艂ad 3:
```python
import re
p = 'kot? kot'
s = 'kotek kot'
r = re.search(p, s)
if r:
    print(r.group())
else:
    print("brak wynik贸w")
```

Przyk艂ad 4:
```python
import re
p = '(\S+) (\S+)'
s = 'Peter Snake'
r = re.search(p, s)
print(r.groups()) # zwr贸膰 uwag臋 na groups
```

### Funkcja findall
Funkcja `re.findall(pattern, string, flags=0)` zwraca list臋 dopasowa艅.

Przyk艂ad 1:
```python
import re
p = '[abc]{3}'
s = 'abc a-a-a ccc bb5b ddd aaa'
print(re.findall(p, s))
```
Przyk艂ad 2:
```python
import re
p = 'a{3,5}'
s = 'a aa aaa aaaa aaaaa aaaaaa aaaaaaa'
print(re.findall(p, s))
```

Przyk艂ad 3:
```python
import re
p = '(kot.|pies)'
s = 'kot pies tok siep kotopies'
print(re.findall(p, s))
```

### Kompilowanie wzorca
Kiedy pracujemy na bardzo du偶ej ilo艣ci danych warto skorzysta膰 z `re.compile(pattern, flags=0)`. 

Przyk艂ad 1:

```python
import re

p = re.compile('kot*')

print(p.match("kotek"))
print(p.match("piesek"))
print(p.match("kot"))

r = p.match("koteczek")

print(r.group())
```

Przyk艂ad 2:
```python
import re
p = re.compile(r'\d+')
r = p.findall("Dopasuj cyfry 12, 13, 14 z tekstu")
if m:
    print('Znalezione: ', r)
else:
    print('Brak')
```

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3.9/howto/regex.html aby dowiedzie膰 si臋 wi臋cej.

### Zadania

鉁忥笍 Napisz regu艂臋 pozwalaj膮c膮 na dopasowanie adresu e-mail.

鉁忥笍 Napisz regu艂臋 pozwalaj膮c膮 na dopasowanie numeru telefonu.

鉁忥笍 Napisz skrypt kt贸ry z wykorzystaniem wyra偶e艅 regularnych znajdzie wszystkie funkcje i klasy w pliku `.py`.

鉁忥笍 Napisz regu艂臋 pozwalaj膮c膮 na dopasowanie wydobycie protoko艂u, domeny, i adresu z linku do strony www. np. https://ii.up.krakow.pl/aktualnosci/ -> ('https', 'ii.up.krakow.pl' , '/aktualnosci/')

鉁忥笍 Napisz regul臋 pozwalaj膮c膮 na wyci膮gni臋cie wszystkich odmian Polska z 
`'Witaj Polsko, Polska to pi臋kny kraj. W Polsce 偶yje bardzo du偶o ludzi. "Hello" oznacza "Cze艣膰" po polsku.'`.

鉁忥笍 Wczytaj plik `maile.html` z [materia艂y/lab4](materia艂y/lab4) . Przygotuj regu艂臋 dopasowania pozwalaj膮c膮 na znalezienie wszystkich adres贸w email w pliku HTML.
  
