# Języki Skryptowe - Lab 4

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie


## Wyrażenia regularne 
Wyrażenia regularne są mini językiem programowania który pozwala nam na tworzenie wzorców dopasowania. 
Modułem odpowiedzialny za udostęnienie funkcjonalności dla wyrażeń regularnych jest `re`.

📖 Proszę przeczytać https://pl.wikipedia.org/wiki/Wyrażenie_regularne.

### meta-znaki 
Meta-znaki posiadają specjalne przeznaczenie w wyrażeniach regularnych. 

| Meta znak  | Przeznaczenie | Przykład |
| ------------- | ------------- | ------------- |
| $  | kończy się ...  |  "python$" |
| ^  | zaczyna się od ...   | "^Programowanie" |
| .  | dowolny znak | ".ot" |
| \*  | dopasowanie zachłanne | "\*" |
| + | wyrażenie występuje 1 lub więcej razy | "[a-z]+" |
| ? | wyrażenie występuje 0 lub 1 raz | "kot?" |
| [] | zbiór znaków opisany w nawiasach kwadratowych | "[abc]" |

📖 Proszę przeczytać https://pl.wikipedia.org/wiki/Wyra%C5%BCenie_regularne#Wyra%C5%BCenia_zach%C5%82anne.

### Funkcja search
Funkcja `re.search(pattern, string, flags=0)` zwraca pierwszy zgodny z wzorcem łańcuch znakowy. 
Funkcja zwraca obiekt `re.Match` lub `None`.

Przykład 1:
```python
import re
p = '[a-z\.]+'
s = '-!!michal.frontczak(at)up.krakow.pl% %lub% %michal.frontczak@up.krakow.pl!!-'
r = re.search(p, s)
print(result.group()) # michal.frontczak
```

Przykład 2:
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

Przykład 3:
```python
import re
p = 'kot? kot'
s = 'kotek kot'
r = re.search(p, s)
if r:
    print(r.group())
else:
    print("brak wyników")
```

### Kompilowanie wzorca

Przykład 1:

```python
import re

p = re.compile('kot*')

print(p.match("kotek"))
print(p.match("piesek"))
print(p.match("kot"))

r = p.match("koteczek")

print(r.group())
```

Przykład 2:
```python
import re
p = re.compile(r'\d+')
r = p.findall("Dopasuj cyfry 12, 13, 14 z tekstu")
if m:
    print('Znalezione: ', r)
else:
    print('Brak')
```

📖 Proszę przeczytać https://docs.python.org/3.9/howto/regex.html, aby dowiedzieć się więcej.

✏️ Napisz regułę pozwalającą na dopasowanie adresu e-mail.

✏️ Napisz regułę pozwalającą na dopasowanie numeru telefonu.

✏️ Wczytaj plik `maile.html` z [materiały/lab4](materiały/lab4) . Przygotuj regułę dopasowania pozwalającą na znalezienie wszystkich adresów email w tagu \<a href\> w pliku HTML.
  
