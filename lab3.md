# Języki Skryptowe - Lab 3

**Legenda**

📖 - proszę przeczytać

📝 - warte zapamiętania / zanotowania

⚠️ - zwróć uwagę

✏️ - zadanie do wykonania

🔍 - poszukaj w internecie

## Tworzenie modułów
Modułem nazywamy plik python'a (z rozszerzeniem `.py`) który zawiera definicję funkcji, klas lub zmiennych. Aby skorzystać udostęnionego kodu przez moduł wykorzystujemy słowo kluczowe `import`, przykład:

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

