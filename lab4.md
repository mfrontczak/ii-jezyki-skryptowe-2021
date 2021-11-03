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
  
