# J臋zyki Skryptowe - Lab 3

**Legenda**

馃摉 - prosz臋 przeczyta膰

馃摑 - warte zapami臋tania / zanotowania

鈿狅笍 - zwr贸膰 uwag臋

鉁忥笍 - zadanie do wykonania

馃攳 - poszukaj w internecie

## Tworzenie modu艂贸w
W Pythonie istnieje wiele standardowych gotowych do u偶ycia modu艂贸w. List臋 wszystkich modu艂贸w mo偶na znale藕膰 [tutaj](https://docs.python.org/3.9/py-modindex.html).

Modu艂em nazywamy plik python'a (z rozszerzeniem `.py`) kt贸ry zawiera definicj臋 funkcji, klas lub zmiennych. Najcz臋艣ciej w module przechowuje si臋 funkcjonalno艣膰 zgodn膮 z jego przeznaczeniem, na przyk艂ad wbudowany modu艂 `random` przechowuje funkcje zwi膮zane z losowaniem.

Aby skorzysta膰 udost臋nionego kodu przez modu艂 wykorzystujemy s艂owo kluczowe `import`, przyk艂ad:

Zawarto艣膰 pliku `my_physics.py`:
```python
def force(mass, acceleration):
    return mass * acceleration


def acceleration(force, mass):
    return force / mass


def mass(force, acceleration):
    return force / acceleration

```

zawarto艣膰 pliku `calculate_force.py`:
```python
import my_physics  # tutaj informujemy interpreter python'a 偶e chcemy uzyska膰 dost臋p do zawarto艣ci pliku my_physics.py (modu艂u).


if __name__ == "__main__":
    mass = float(input('Podaj mas臋 obiektu: '))
    acce = float(input('Podaj przy艣pieszenie: '))
    f = my_physics.force(mass, acce)  # tutaj wywo艂ujemy funkcj臋 force znajduj膮c膮 si臋 w module my_physics.
    print(f"{mass:.2f} * {acce:.2f} = {f:.2f}")

```

Istnieje r贸wnie偶 inny spos贸b na zaimportowanie okre艣lonych zmiennych, funkcji lub klas z modu艂u. W tym celu nale偶y u偶y膰 konstrukcji `from ... import ...`, na przyk艂ad `from sys import path`.

Przyk艂ad 1:

Alternatywna zawarto艣膰 pliku `calculate_force.py`:
```python
from my_physics import force  # tutaj informujemy interpreter python'a 偶e chcemy uzyska膰 dost臋p do okre艣lonej zawarto艣ci pliku my_physics.py (modu艂u).


if __name__ == "__main__":
    mass = float(input('Podaj mas臋 obiektu: '))
    acce = float(input('Podaj przy艣pieszenie: '))
    f = force(mass, acce)  # tutaj wywo艂ujemy funkcj臋 force
    print(f"{mass:.2f} * {acce:.2f} = {f:.2f}")
```

Przyk艂ad 2:

Alternatywna zawarto艣膰 pliku `calculate_force.py`:
```python
from my_physics import force, mass


if __name__ == "__main__":
    mass = float(input('Podaj mas臋 obiektu: '))
    acce = float(input('Podaj przy艣pieszenie: '))
    f = force(mass, acce)  # tutaj wywo艂ujemy funkcj臋 force
    print(f"{mass:.2f} * {acce:.2f} = {f:.2f}")
    
    # UPS! tutaj dostaniemy b艂膮d, funkcja mass z modu艂u my_physics zostanie
    # przys艂oni臋ta przez zmienn膮 mass (konflikt nazw).
    m = mass(f, acce)  
    print(f"{m:.2f} * {acce:.2f} = {f:.2f}")
```

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3.9/reference/import.html, aby dowiedzie膰 si臋 wi臋cej.


鉁忥笍 Stw贸rz modu艂 kt贸ry udost臋pni funkcje licz膮c膮 艣redni膮 artmetyczn膮 i 艣redni膮 geometryczn膮.

鉁忥笍 Stw贸rz kolejny modu艂 w kt贸rym znajd膮 si臋 funkcj臋 do liczenia odchylenia standardowego. 

鉁忥笍 Napisz skrypt kt贸ry wykorzysta funkcje z poprzednio utworzonych modu艂贸w. U偶ytkownik powinien m贸c wprowadzi膰 dane z klawiatury.


## Dekorator funkcji
Dekoratorem funkcji nazywamy funkcj臋 kt贸ra jako parametr przyjmuje referencje innej funkcji w celu rozszerzenia jej funkcjonalno艣ci.

Przyk艂ad:

```python
# funkcja power_of_2 przyjmie jako parametr inn膮 funkcj臋
# a nast臋pnie wykorzysta j膮 wewn膮trz funkcji _wrapper
# kt贸ra wywo艂a przekazan膮 funkcj臋 i zmodyfikuje jej warto艣膰
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

Aby u偶y膰 funkcji jako dekorator nale偶y u偶y膰 konstrukcji `@` + nazwa funkcji.

Przyk艂ad:
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

Dektorator mo偶e r贸wnie偶 dzia艂a膰 jak funkcja i przyjmowa膰 parametry.

Przyk艂ad:
```python
def multiply(by):
    def _wrapper(func):
        def _inner(*args, **kwargs):
            return func(*args, **kwargs) * by
        return _inner
    return _wrapper


@multiply(2)
def add_two_numbers(a, b):
    return a + b
    
    
@multiply(3)
def add_three_numbers(a, b, c):
    return a + b

print(add_two_numbers(3, 2)) 
print(add_three_numbers(1, 2, 3))
```

鉁忥笍 Stw贸rz dekorator dla funkcji (zwracaj膮cej liczb臋) kt贸ry b臋dzie sprawdza艂 czy liczba jest wi臋ksza od 0, je偶eli tak to ma zwr贸ci膰 jej pierwiastek (u偶yj modu艂 `math` funkcj臋 `sqrt`).

鉁忥笍 Stw贸rz dekorator kt贸ry dla dowolnej funkcji b臋dzie wy艣wietla艂 przed jej wywo艂aniem warto艣ci argument贸w jakie zosta艂y do niej przekazane.

鉁忥笍 Napisz dekorator kt贸ry zrzutuje argumenty funkcji na wskazane typy.

## Zakresy zmiennych
Widoczno艣膰 zmiennej (funkcji lub klasy) zale偶y od miejsca w kt贸rym jest zdeklarowana. 

Aby zmienna by艂a widoczna funkcji nale偶y u偶y膰 s艂owa kluczowego `global` a nast臋pnie poda膰 nazw臋 zmiennej do kt贸rej chcemy mie膰 dost臋p w obr臋bie naszej funkcji.

Przyk艂ad:
```python
zmienna_globalna = 10


def funkcja():
    global zmienna_globalna
    print(f"Zmienna globalna w funkcji: {zmienna_globalna}")
    zmienna_globalna = 20
    print(f"Zmienna globalna w funkcji po przypisaniu nowej warto艣ci: {zmienna_globalna}")


print(f"Zmienna globalna PRZED wywo艂aniem funkcji: {zmienna_globalna}")
print("-" * 50)
funkcja()
print("-" * 50)
print(f"Zmienna globalna PO wywo艂aniem funkcji: {zmienna_globalna}")  
```
    
## Wyj膮tki
Wyj膮tkiem nazywamy cz臋sto zdarzenie w wyniku kt贸rego nasz skrypt lub program nie dzia艂a prawid艂owo. Kiedy skrypt zg艂osi wyj膮tek interpreter przerwie jego wykonanie i poinformuje o b艂臋dzie u偶ytkownika. Na szcz臋艣cie w j臋zyku Python jak i wielu innych j臋zykach programowania istnieje mechanizm s艂u偶膮cy przechwytywaniu wyj膮tku przez programist臋 i obs艂ugi tego zdarzenia.

W celu przechwycenia wyj膮tku w naszym skrypcie u偶ywamy konstrukcji `try` `except`.

Przyk艂ad 1: zwracaj膮cy wyj膮tek:
```python
f = open('nie_istniejacy.txt')
```

Przyk艂ad 2: zwracaj膮cy wyj膮tek:
```python
i = int('pietna艣cie')
```

Przyk艂ad 1: obs艂uguj膮cy wyj膮tek:
```python
try:
    f = open('nie_istniejacy.txt')
except:   # przechwytujemy wszystkie wyj膮tki.
    print("Podany plik nie istnieje lub nie masz uprawnie艅 do odczytu.")
```

Przyk艂ad 2: obs艂uguj膮cy wyj膮tek:
```python
try:
    i = int('pietna艣cie')
except ValueError as err:
    print(err)
```

Oczywi艣cie u偶ycie konstrukcji `except` bez podania typu wyj膮tku kt贸ry chcemy obs艂u偶y膰, b臋dzie przechwytywa膰 wszystkie mo偶liwe wyj膮tki. W wypadku kiedy chcemy przechwyci膰 konkretny wyj膮tek nale偶y po `except` poda膰 jego nazw臋 (jak w przyk艂adzie 2). 

Konstrukcja `except ... as e` pozwala nam na uzyskanie dost臋pu do informacji o wyj膮tku zwr贸conym przez interpreter.

### Przechwytywanie wielu wyj膮tk贸w
Python umo偶liwia nam zdefiniowanie w jednym wierszu `except` wielu wyj膮tk贸w jakie chcemy obs艂u偶y膰.

Przyk艂ad:
```python
try:
    import foobar
    foobar.value
except (ModuleNotFoundError, ImportError) as e:
    # jaka艣 obs艂uga b艂臋du ModuleNotFoundError lub ImportError
except (FileNotFoundError, IOError, OSError) as e:
    # jaka艣 obs艂uga b艂臋du FileNotFoundError lub IOError lub OSError
```

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3.9/library/exceptions.html, aby dowiedzie膰 si臋 wi臋cej.

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3.9/library/exceptions.html#exception-hierarchy, aby dowiedzie膰 si臋 wi臋cej.

馃摉 Prosz臋 przeczyta膰 https://docs.python.org/3.9/tutorial/errors.html, aby dowiedzie膰 si臋 wi臋cej.

鉁忥笍 Z listy dost臋pnych wyj膮tk贸w wybierz jeden a nast臋pnie u偶yj go wraz z sk艂adni膮 `raise` do wywo艂ania wyj膮tku. Napisz skrypt kt贸ry obs艂u偶y wyj膮tek - w dowolny spos贸b.

鉁忥笍 Napisz skrypt kt贸ry b臋dzie odpytywa艂 u偶ytkownika o jego wiek, a偶 do momentu kiedy wprowadzi poprawne dane. (u偶yj p臋tli `while True`)

