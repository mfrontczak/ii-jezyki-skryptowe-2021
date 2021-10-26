# Języki Skryptowe - Lab 2

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

### Wyrażenia listowe i generatorowe

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


### Transformacja danych


### Funkcje anonimowe (lambda)
Przy pomocy słowa kluczowego `lambda` definiujemy jedno-wierszową funkcję z kodem. 
Funkcje anonimowe mają zastosowanie w momencie kiedy chcemy przekazać proste wyrażenie jako parametr do innej funkcji np. `sorted`.

Przykład:
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


### Sortowanie danych

```python
arr = [1, 4, 5, 6, 1, 3, 4, 7, 8]
sorted(arr)
```

### Obsługa plików
```python
f = open('plik.txt')
f.read()
f.readline()
for line in f:
  print(line)
f.close()
```

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

f = open('guido_data.json', 'w')
f.write(jsonized)
f.close()
```
:book: Proszę przeczytać https://docs.python.org/3/library/json.html, aby dowiedzieć się więcej.
#### CSV
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

:book: Proszę przeczytać https://docs.python.org/3/library/csv.html, aby dowiedzieć się więcej.



