# Języki Skryptowe - Lab 2

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

### Wyrażenia listowe i generatorowe
#### Generator
Generator pozwala nam na użycie wyrażeń ktore zachowują się jak 📖 [iterator](https://pl.wikipedia.org/wiki/Iterator). Funkcja generatora pamięta swój stan jaki posiadała w poprzednim wywołaniu. Generatory są często wykorzystywane w momencie kiedy przetwarzamy sekwencje które są bardzo długie, a w danym momencie nie interesuje nas jako całość, a jedynie jej elementy. Do obsługi generatorów używamy funkcji wbudowanej `next`.

:book: Proszę przeczytać https://docs.python.org/3.9/library/functions.html#next, aby dowiedzieć się więcej.

Przykład 1:
```python
import random
genr = ( (i, random.randint(1, 100)) for i in range(100) )
type(genr)

print(next(genr))
print(next(genr))
print(next(genr))
```

Przykład 2:
```python
import random
genr = ( (i, random.randint(1, 100)) for i in range(100) )
type(genr)

for (i, r) in genr:
    print(f"{i}-te wywołanie generatora, zwróciło losową wartość {r}")
    
```

✏️ Stwórz generator który będzie zwracał kolejne liczby alfabetu.

✏️ Zapoznaj się z modułem [random](https://docs.python.org/3.9/library/random.html), Korzystając z funkcji `random.choice`, napisz generator który będzie zwracał losowe alfa-numeryczne znaki.

✏️ Spytaj użytkownika o to jak długie powinno być wygenerowane hasło, a następnie wykorzystaj wcześniej utworzony generator do wygenerowania losowego hasła dla użytkownika. 


#### Generator listy

Przykład:
```python
arr = []
for x in range(10):
    arr.append(x % 3)
print(arr)
```
Powyższy kod, można zastąpić przez generator wyrażenia listowego:
```python
arr = [x % 3 for x in range(10)]
print(arr)
```

### Filtrowanie

Funkcja wbudowana `filter(func, iter)` zwraca iterator elementów dla których `func` zwróci `True`. 

Przykład z wykorzystaniem funkcji `filter`:
```python
def only_even(value):
    return value % 2 == 0
    
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

print(f"Nasza lista przed zastosowaniem filtra: {arr}")

filtered_arr = list( filter(only_even, arr) )

print(f"Nasza lista po zastosowaniu filtra:{filtered_arr}")
```

Przykład filtrowania danych z wykorzystaniem pętli for:
```python
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

print(f"Nasza lista przed zastosowaniem filtra: {arr}")

filtered_arr = []
for value in arr:
    if value % 2 == 0:  # if only_even(value):
        filtered_arr.append(value)
        
print(f"Nasza lista po zastosowaniu filtra:{filtered_arr}") 
```

Bardziej eleganckim i zgodnym z Pythonem sposobem filtrowanie listy, jest wykorzystanie generatora wyrażeń listowych.

Przykład:
```python
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

print(f"Nasza lista przed zastosowaniem filtra: {arr}")

filtered_arr = [value for value in arr if value % 2 == 0]

print(f"Nasza lista po zastosowaniu filtra:{filtered_arr}")
```

✏️ Wykorzystując generator wyrażenia listowego utwórz [Sito Eratostenesa](https://pl.wikipedia.org/wiki/Sito_Eratostenesa).

🤯 Najpierw spróbuj zaimplementować Sito Eratostenesa bez generatora, a dopiero później przekształć swój kod.

<!-- 
### Transformacja danych

```python
arr = [1, 5, 3, 4, 2, 7, 8, 9, 10, 12, 11, 16, 14]

powered_arr = [x**2 for x in arr] 
-->

### Funkcje anonimowe (lambda)
Przy pomocy słowa kluczowego `lambda` definiujemy jedno-wierszową funkcję z kodem. 
Funkcje anonimowe mają zastosowanie w momencie kiedy chcemy przekazać proste wyrażenie jako parametr do innej funkcji np. `sorted`.

Przykład 1:
```python
# takiej funkcji nie da się wywołać poprzez nazwę
lambda x: x**2
# Sposób jednorazowego wywołania
(lambda x: x**2)(10)
```
Przykład 2:
```python
# niby-anonimowa, bo nazwana
pow = lambda x: x**2
print(pow(2))
```

Przykład 3:
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

Przykład 1:
```python
arr = [1, 4, 5, 6, 1, 3, 4, 7, 8]
print(sorted(arr))
print(sorted(arr, reverse=True))
```

Przykład 2:
```python
words = ["ala", "ma", "kota", "i", "psa"]
print(sorted(words))
print(sorted(words, reverse=True))
```

:book: Proszę przeczytać https://docs.python.org/3.9/library/functions.html#sorted, aby dowiedzieć się więcej.

### Obsługa plików
Do obsługi plików otwarcia(r)/zapisu(w)/nadpisania(a) służy funkcja `open`. Funkcja `open` działa również z wyrażeniem `with`. 

Przykład:
```python
f = open('plik.txt')
# data = f.read()
# lines = f.readline()
for line in f:
  print(line)
f.close()
```

Przykład z `with`:

```python
with open('plik.txt') as f:
    # data = f.read()
    # lines = f.readline()
    for line in f:
      print(line)
```

✏️ Utwórz plik tekstowy a następnie wczytaj go do swojego programu przy użyciu różnych metod.

:book: Proszę przeczytać https://docs.python.org/3.9/library/functions.html#open, aby dowiedzieć się więcej.

### Serializacja obietków
Serializacja to proces polegający na przekształceniu obiektów na format danych pozwalających nam na zapisanie i późniejsze odtworzenie danych z pliku, bazy danych lub pamięci komputera.

⚠️ Pliki do przykładów znajdują się w katalogu [materiały/lab2](materiały/lab2).

#### JSON
Wczytywanie danych z pliku o formacie JSON.

przykład:
```python
import json

# Wczytywanie pliku w formacie JSON do pythona
f = open('uczelnie.json', encoding='utf-8')
content = f.read()
uczelnie = json.loads(content)
# Otrzymujemy strukturę danych zgodną z python'em
print(uczelnie)
f.close()
```

Zapisywanie danych do pliku o formacie JSON.

przykład:
```python
import json

data = {
  'name': 'Guido van Rossum',
  'age': 65,
  'faviourite_movies': [
    'Żywot Briana',
    'Monty Python i Święty Graal',
    'Monty Python: Prawie prawda'
  ]
}

jsonized = json.dumps(data)

f = open('guido_data.json', mode='w', encoding='utf-8')
f.write(jsonized)
f.close()
```

✏️ Stwórz bibliotekę filmów. Napisz skrypt w którym użytkownik będzie mógł dodawać filmy do pliku w formacie json. Użytkownik powinien móc wprowadzać nazwy filmów wraz z ich średnią oceną (z dowolnego serwisu) i rokiem wydawania, aż do momentu nie wprowadzenia tytułu filmu przez użytkownika.

:book: Proszę przeczytać https://docs.python.org/3/library/json.html, aby dowiedzieć się więcej.

#### CSV

Wczytywanie danych z pliku CSV.

Przykład:
```python
import csv

# Wczytywanie danych z pliku CSV
f = open('ciasta.csv', encoding='utf-8')
reader = csv.reader(f, delimiter=';')
for row in reader:
    name, prep_time = row
    print(f"Ciasto *{name}* przygotowuje się *{prep_time}* minut.")
f.close()
```

Zapisywanie danych do pliku CSV.
```python
import csv

# Zapisywanie danych do pliku CSV
f = open('miasta.csv', mode='w', encoding='utf-8')
writer = csv.writer(f, delimiter=';')
writer.writerow(['Kraków', 766000])
writer.writerow(['Wrocław', 638000])
writer.writerow(['Warszawa', 1765000])
f.close()
```
✏️ Napisz skrypt w którym użytkownik będzie mógł dodawać studentów do pliku w formacie csv. Skrypt powinien spytać użytkownika ilu studentów chce dodać a następnie w petli poprosić użytkownika o numer albumu i ocene końcową.

:book: Proszę przeczytać https://docs.python.org/3/library/csv.html, aby dowiedzieć się więcej.
