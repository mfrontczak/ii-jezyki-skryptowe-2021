# J臋zyki Skryptowe - Lab 2

**Legenda**

馃摉 - prosz臋 przeczyta膰

馃摑 - warte zapami臋tania / zanotowania

鈿狅笍 - zwr贸膰 uwag臋

鉁忥笍 - zadanie do wykonania

馃攳 - poszukaj w internecie

### Wyra偶enia listowe i generatorowe
#### Generator
Generator pozwala nam na u偶ycie wyra偶e艅 ktore zachowuj膮 si臋 jak 馃摉 [iterator](https://pl.wikipedia.org/wiki/Iterator). Funkcja generatora pami臋ta sw贸j stan jaki posiada艂a w poprzednim wywo艂aniu. Generatory s膮 cz臋sto wykorzystywane w momencie kiedy przetwarzamy sekwencje kt贸re s膮 bardzo d艂ugie, a w danym momencie nie interesuje nas jako ca艂o艣膰, a jedynie jej elementy. Do obs艂ugi generator贸w u偶ywamy funkcji wbudowanej `next`.

:book: Prosz臋 przeczyta膰 https://docs.python.org/3.9/library/functions.html#next, aby dowiedzie膰 si臋 wi臋cej.

Przyk艂ad 1:
```python
import random
genr = ( (i, random.randint(1, 100)) for i in range(100) )
type(genr)

print(next(genr))
print(next(genr))
print(next(genr))
```

Przyk艂ad 2:
```python
import random
genr = ( (i, random.randint(1, 100)) for i in range(100) )
type(genr)

for (i, r) in genr:
    print(f"{i}-te wywo艂anie generatora, zwr贸ci艂o losow膮 warto艣膰 {r}")
    
```

鉁忥笍 Stw贸rz generator kt贸ry b臋dzie zwraca艂 kolejne litery alfabetu.

鉁忥笍 Zapoznaj si臋 z modu艂em [random](https://docs.python.org/3.9/library/random.html), Korzystaj膮c z funkcji `random.choice`, napisz generator kt贸ry b臋dzie zwraca艂 losowe alfa-numeryczne znaki.

鉁忥笍 Spytaj u偶ytkownika o to jak d艂ugie powinno by膰 wygenerowane has艂o, a nast臋pnie wykorzystaj wcze艣niej utworzony generator do wygenerowania losowego has艂a dla u偶ytkownika. 


#### Generator listy

Przyk艂ad:
```python
arr = []
for x in range(10):
    arr.append(x % 3)
print(arr)
```
Powy偶szy kod, mo偶na zast膮pi膰 przez generator wyra偶enia listowego:
```python
arr = [x % 3 for x in range(10)]
print(arr)
```

### Filtrowanie

Funkcja wbudowana `filter(func, iter)` zwraca iterator element贸w dla kt贸rych `func` zwr贸ci `True`. 

Przyk艂ad z wykorzystaniem funkcji `filter`:
```python
def only_even(value):
    return value % 2 == 0
    
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

print(f"Nasza lista przed zastosowaniem filtra: {arr}")

filtered_arr = list( filter(only_even, arr) )

print(f"Nasza lista po zastosowaniu filtra:{filtered_arr}")
```

Przyk艂ad filtrowania danych z wykorzystaniem p臋tli for:
```python
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

print(f"Nasza lista przed zastosowaniem filtra: {arr}")

filtered_arr = []
for value in arr:
    if value % 2 == 0:  # if only_even(value):
        filtered_arr.append(value)
        
print(f"Nasza lista po zastosowaniu filtra:{filtered_arr}") 
```

Bardziej eleganckim i zgodnym z Pythonem sposobem filtrowanie listy, jest wykorzystanie generatora wyra偶e艅 listowych.

Przyk艂ad:
```python
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

print(f"Nasza lista przed zastosowaniem filtra: {arr}")

filtered_arr = [value for value in arr if value % 2 == 0]

print(f"Nasza lista po zastosowaniu filtra:{filtered_arr}")
```

鉁忥笍 Wykorzystuj膮c generator wyra偶enia listowego utw贸rz [Sito Eratostenesa](https://pl.wikipedia.org/wiki/Sito_Eratostenesa).

馃く Najpierw spr贸buj zaimplementowa膰 Sito Eratostenesa bez generatora, a dopiero p贸藕niej przekszta艂膰 sw贸j kod.

<!-- 
### Transformacja danych

```python
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

powered_arr = [x**2 for x in arr] 
-->

### Funkcje anonimowe (lambda)
Przy pomocy s艂owa kluczowego `lambda` definiujemy jedno-wierszow膮 funkcj臋 z kodem. 
Funkcje anonimowe maj膮 zastosowanie w momencie kiedy chcemy przekaza膰 proste wyra偶enie jako parametr do innej funkcji np. `sorted`.

Przyk艂ad 1:
```python
# takiej funkcji nie da si臋 wywo艂a膰 poprzez nazw臋
lambda x: x**2
# Spos贸b jednorazowego wywo艂ania
(lambda x: x**2)(10)
```
Przyk艂ad 2:
```python
# niby-anonimowa, bo nazwana
pow = lambda x: x**2
print(pow(2))
```

Przyk艂ad 3:
```python
d = {
    'klucz1': 2,
    'klucz2': 4,
    'klucz3': 3,
    'klucz4': 1
}
print(sorted(d))
print(sorted(d.items()))

print(sorted(d.items(), key=lambda item: item[0]))
```

### Sortowanie danych

Przyk艂ad 1:
```python
arr = [1, 4, 5, 6, 1, 3, 4, 7, 8]
print(sorted(arr))
print(sorted(arr, reverse=True))
```

Przyk艂ad 2:
```python
words = ["ala", "ma", "kota", "i", "psa"]
print(sorted(words))
print(sorted(words, reverse=True))
```

:book: Prosz臋 przeczyta膰 https://docs.python.org/3.9/library/functions.html#sorted, aby dowiedzie膰 si臋 wi臋cej.

### Obs艂uga plik贸w
Do obs艂ugi plik贸w otwarcia(r)/zapisu(w)/nadpisania(a) s艂u偶y funkcja `open`. Funkcja `open` dzia艂a r贸wnie偶 z wyra偶eniem `with`. 

Przyk艂ad:
```python
f = open('plik.txt')
# data = f.read()
# lines = f.readline()
for line in f:
  print(line)
f.close()
```

Przyk艂ad z `with`:

```python
with open('plik.txt') as f:
    # data = f.read()
    # lines = f.readline()
    for line in f:
      print(line)
```

鉁忥笍 Utw贸rz plik tekstowy a nast臋pnie wczytaj go do swojego programu przy u偶yciu r贸偶nych metod.

:book: Prosz臋 przeczyta膰 https://docs.python.org/3.9/library/functions.html#open, aby dowiedzie膰 si臋 wi臋cej.

### Serializacja obiekt贸w
Serializacja to proces polegaj膮cy na przekszta艂ceniu obiekt贸w na format danych pozwalaj膮cych nam na zapisanie i p贸藕niejsze odtworzenie danych z pliku, bazy danych lub pami臋ci komputera.

鈿狅笍 Pliki do przyk艂ad贸w znajduj膮 si臋 w katalogu [materia艂y/lab2](materia艂y/lab2).

#### JSON
Wczytywanie danych z pliku o formacie JSON.

przyk艂ad:
```python
import json

# Wczytywanie pliku w formacie JSON do pythona
f = open('uczelnie.json', encoding='utf-8')
content = f.read()
uczelnie = json.loads(content)
# Otrzymujemy struktur臋 danych zgodn膮 z python'em
print(uczelnie)
f.close()
```

Zapisywanie danych do pliku o formacie JSON.

przyk艂ad:
```python
import json

data = {
  'name': 'Guido van Rossum',
  'age': 65,
  'faviourite_movies': [
    '呕ywot Briana',
    'Monty Python i 艢wi臋ty Graal',
    'Monty Python: Prawie prawda'
  ]
}

jsonized = json.dumps(data)

f = open('guido_data.json', mode='w', encoding='utf-8')
f.write(jsonized)
f.close()
```

鉁忥笍 Stw贸rz bibliotek臋 film贸w. Napisz skrypt w kt贸rym u偶ytkownik b臋dzie m贸g艂 dodawa膰 filmy do pliku w formacie json. U偶ytkownik powinien m贸c wprowadza膰 nazwy film贸w wraz z ich 艣redni膮 ocen膮 (z dowolnego serwisu) i rokiem wydawania, a偶 do momentu nie wprowadzenia tytu艂u filmu przez u偶ytkownika.

:book: Prosz臋 przeczyta膰 https://docs.python.org/3/library/json.html, aby dowiedzie膰 si臋 wi臋cej.

#### CSV

Wczytywanie danych z pliku CSV.

Przyk艂ad:
```python
import csv

# Wczytywanie danych z pliku CSV
f = open('ciasta.csv', encoding='utf-8')
reader = csv.reader(f, delimiter=';')
for row in reader:
    name, prep_time = row
    print(f"Ciasto *{name}* przygotowuje si臋 *{prep_time}* minut.")
f.close()
```

Zapisywanie danych do pliku CSV.
```python
import csv

# Zapisywanie danych do pliku CSV
f = open('miasta.csv', mode='w', encoding='utf-8')
writer = csv.writer(f, delimiter=';')
writer.writerow(['Krak贸w', 766000])
writer.writerow(['Wroc艂aw', 638000])
writer.writerow(['Warszawa', 1765000])
f.close()
```
鉁忥笍 Napisz skrypt w kt贸rym u偶ytkownik b臋dzie m贸g艂 dodawa膰 student贸w do pliku w formacie csv. Skrypt powinien spyta膰 u偶ytkownika ilu student贸w chce doda膰 a nast臋pnie w petli poprosi膰 u偶ytkownika o numer albumu i ocene ko艅cow膮.

:book: Prosz臋 przeczyta膰 https://docs.python.org/3/library/csv.html, aby dowiedzie膰 si臋 wi臋cej.
