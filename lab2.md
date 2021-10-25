# Języki Skryptowe - Lab 2

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

### Wyrażenia listowe i generatorowe

### Filtrowanie

### Transformacja danych

### Sortowanie danych

```python
arr = [1, 4, 5, 6, 1, 3, 4, 7, 8]
sorted(arr)
```

### Funkcje anonimowe (lambda)

```python
lambda x: x**2
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



