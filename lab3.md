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

## Dekorator funkcji
Dekoratorem funkcji nazywamy funkcję która jako parametr przyjmuje referencje innej funkcji w celu rozszerzenia jej funkcjonalności.

Przykład:

```python
# funkcja power_of_2 przyjmie jako parametr inną funkcję
# a następnie wykorzysta ją wewnątrz funkcji _wrapper
# która wywoła przekazaną funkcję i zmodyfikuje jej wartość
def power_of_2(func):
    def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result**2
    return _wrapper


def just_a_number_plus_one(a):
    return a + 1

print(just_a_number_plus_one.__name__)

# tutaj dokonujemy "podmiany"
just_a_number_plus_one = power_of_2(just_a_number_plus_one)

print(just_a_number_plus_one.__name__)

print(just_a_number_plus_one(2))
```

Aby użyć funkcji jako dekorator należy użyć konstrukcji `@` + nazwa funkcji.

Przykład:

```python
def power_of_2(func):
    def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result**2
    return _wrapper

@power_of_2
def just_a_number_plus_one(a):
    return a + 1

print(just_a_number_plus_one.__name__)

print(just_a_number_plus_one(2))
```

✏️ Stwórz dekorator dla funkcji (zwracającej liczbę) który będzie sprawdzał czy liczba jest większa od 0, jeżeli tak to ma zwrócić jej pierwiastek (użyj moduł `math` funkcję `sqrt`).

✏️ Stwórz dekorator który dla dowolnej funkcji będzie wyświetlał przed jej wywołaniem wartości argumentów jakie zostały do niej przekazane.

## Zakresy zmiennych
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
    
## Wyjątki
Wyjątkiem nazywamy często zdarzenie w wyniku którego nasz skrypt lub program nie działa prawidłowo. Kiedy skrypt zgłosi wyjątek interpreter przerwie jego wykonanie i poinformuje o błędzie użytkownika. Na szczęście w języku Python jak i wielu innych językach programowania istnieje mechanizm służący przechwytywaniu wyjątku przez programistę i obsługi tego zdarzenia.

W celu przechwycenia wyjątku w naszym skrypcie używamy konstrukcji `try` `except`.

Przykład 1: zwracający wyjątek:
```python
f = open('nie_istniejacy.txt')
```

Przykład 2: zwracający wyjątek:
```python
i = int('pietnaście')
```

Przykład 1: obsługujący wyjątek:
```python
try:
    f = open('nie_istniejacy.txt')
except:
    print("Podany plik nie istnieje lub nie masz uprawnień do odczytu.")
```

Przykład 2: obsługujący wyjątek:
```python
try:
    i = int('pietnaście')
except ValueError as err:
    print(err)
```

Oczywiście użycie konstrukcji `except` bez podania typu wyjątku który chcemy obsłużyć, będzie przechwytywać wszystkie możliwe wyjątki. W wypadku kiedy chcemy przechwycić konkretny wyjątek należy po `except` podać jego nazwę (jak w przykładzie 2). Konstrukcja `except ... as e` pozwala nam na uzyskanie dostępu do informacji o wyjątku zwróconym przez interpreter.

📖 Proszę przeczytać https://docs.python.org/3.9/tutorial/errors.html, aby dowiedzieć się więcej.


✏️ Z listy dostępnych wyjątków wybierz jeden a następnie użyj go wraz z składnią `raise` do wywołania wyjątku. Napisz skrypt który obsłuży wyjątek - w dowolny sposób.

✏️ Napisz skrypt który będzie odpytywał użytkownika o jego wiek, aż do momentu kiedy wprowadzi poprawne dane. (użyj pętli `while True`)

