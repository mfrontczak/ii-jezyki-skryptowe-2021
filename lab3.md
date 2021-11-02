# Języki Skryptowe - Lab 3

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

## Tworzenie modułów
W Pythonie istnieje wiele standardowych gotowych do użycia modułów. Listę wszystkich modułów można znaleść [tutaj](https://docs.python.org/3.9/py-modindex.html).

Modułem nazywamy plik python'a (z rozszerzeniem `.py`) który zawiera definicję funkcji, klas lub zmiennych. Najczęściej w module przechowuje się funkcjonalność zgodną z jego przeznaczeniem, na przykład wbudowany moduł `random` przechowuje funkcje związane z losowaniem.

Aby skorzystać udostęnionego kodu przez moduł wykorzystujemy słowo kluczowe `import`, przykład:

Zawartość pliku `my_physics.py`:
```python
def force(mass, acceleration):
    return mass * acceleration


def acceleration(force, mass):
    return force / mass


def mass(force, acceleration):
    return force / acceleration

```

zawartość pliku `calculate_force.py`:
```python
import my_physics  # tutaj informujemy interpreter python'a że chcemy uzyskać dostęp do zawartości pliku my_physics.py (modułu).


if __name__ == "__main__":
    mass = float(input('Podaj masę obiektu: '))
    acce = float(input('Podaj przyśpieszenie: '))
    f = my_physics.force(mass, acce)  # tutaj wywołujemy funkcję force znajdującą się w module my_physics.
    print(f"{mass:.2f} * {acce:.2f} = {f:.2f}")

```

Istnieje również inny sposób na zaimportowanie określonych zmiennych, funkcji lub klas z modułu. W tym celu należy użyć konstrukcji `from ... import ...`, na przykład `from sys import path`.

Przykład 1:

Alternatywna zawartość pliku `calculate_force.py`:
```python
from my_physics import force  # tutaj informujemy interpreter python'a że chcemy uzyskać dostęp do określonej zawartości pliku my_physics.py (modułu).


if __name__ == "__main__":
    mass = float(input('Podaj masę obiektu: '))
    acce = float(input('Podaj przyśpieszenie: '))
    f = force(mass, acce)  # tutaj wywołujemy funkcję force
    print(f"{mass:.2f} * {acce:.2f} = {f:.2f}")
```

Przykład 2:

Alternatywna zawartość pliku `calculate_force.py`:
```python
from my_physics import force, mass


if __name__ == "__main__":
    mass = float(input('Podaj masę obiektu: '))
    acce = float(input('Podaj przyśpieszenie: '))
    f = force(mass, acce)  # tutaj wywołujemy funkcję force
    print(f"{mass:.2f} * {acce:.2f} = {f:.2f}")
    
    # UPS! tutaj dostaniemy błąd, funkcja mass z modułu my_physics zostanie
    # przysłonięta przez zmienną mass (konflikt nazw).
    m = mass(f, acce)  
    print(f"{m:.2f} * {acce:.2f} = {f:.2f}")
```

📖 Proszę przeczytać https://docs.python.org/3.9/reference/import.html, aby dowiedzieć się więcej.


✏️ Stwórz moduł który udostępni funkcje liczącą średnią artmetyczną i średnią geometryczną.

✏️ Napisz skrypt który wykorzysta obie funkcje. Użytkownik powinien móc wprowadzić dane z klawiatury.

✏️ Z modułu `random` zaimportuj funkcję `randint`, następnie użyj jej do wylosowanie trzech wartości z zakresu od 2 do 5.


### Zakresy zmiennych
Widoczność zmiennej (funkcji lub klasy) zależy od miejsca w którym jest zdeklarowana. 

Aby zmienna była widoczna funkcji należy użyć słowa kluczowego `global` a następnie podać nazwę zmiennej do której chcemy mieć dostęp w obrębie naszej funkcji.

Przykład:
```python
zmienna_globalna = 10


def funkcja():
    global zmienna_globalna
    print(f"Zmienna globalna w funkcji: {zmienna_globalna}")
    zmienna_globalna = 20
    print(f"Zmienna globalna w funkcji po przypisaniu nowej wartości: {zmienna_globalna}")


print(f"Zmienna globalna PRZED wywołaniem funkcji: {zmienna_globalna}")
print("-" * 50)
funkcja()
print("-" * 50)
print(f"Zmienna globalna PO wywołaniem funkcji: {zmienna_globalna}")  
```


## Wyrażenia regularne 
