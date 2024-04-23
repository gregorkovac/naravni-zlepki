# Naravni zlepki

### 1. domača naloga pri predmetu Numerična matematika

Gregor Kovač \

## Opis naloge

Danih je $n$ interpolacijskih točk $(x_i, f(x_i)), i = 1,...,n$. _Naravni interpolacijski kubični zlepek_ $S$ je funkcija, za katero velja:

- $S(x_i) = f_i$,
- $S$ je polinom stopnje 3 ali manj na intervalih $[x_i, x_{i+1}]$,
- $S$ je dvakrat zvezno odvedljiva funkcija na intervalu $[x_i, x_{i+1}]$,
- $S''(x_1) = S''(x_n) = 0$.

Cilj te naloge je izračunati zlepek iz podanih točk $(x_i, f(x_i))$.

## Struktura projekta

- [zlepek.py](zlepek.py) - Python skripta s kodo projekta.
- [test_zlepek.py](test_zlepek.py) - Python skripta s testi.
- [report.pdf](report.pdf) - poročilo projekta.
- [report.ipynb](report.ipynb) - Jupyter Notebook skripta za dinamično generiranje poročila.

## Potrebne Python knjižnice

- Numpy
- MatPlotLib
- Jupyter

## Uporaba projekta

V ukazni vrstici se postavimo v mapo projekta in zaženemo `python zlepek.py`.

V funkciji `main()` je definiran primer uporabe, za ustvarjanje lastnega primera pa lahko uporabimo naslednje smernice:

- Ustvarimo `numpy` seznama `x = np.array([...])`, `y = np.array([...])`, ki vsebujeta interpolacijske točke $(x_i, f(x_i))$.
- Uporabimo funkcijo `interpoliraj`, ki ustvari zlepek: `z = interpoliraj(x, y)`.
- Uporabimo funkcijo `plot`, ki izriše zlepek in interpolacijske točke: `plot(z, f)`. Argument `f` je opcijski in predstavlja funkcijo, s katero so bili podatki generirani. Če je podana, se izriše s črtkano črto poleg zlepka.

## Uporaba testov

Če želimo pognati teste za projekt, v ukazno vrstico napišemo `python test_zlepek.py`, ali pa uporabimo vgrajeno funkcijo za testiranje v našem razvojnem okolju.

## Ustvarjanje poročila

Za (ponovno) ustvarjanje odpremo datoteko [report.ipynb](report.ipynb).
To lahko storimo v svojem razvojnem okolju, ali pa v ukazni vrstici napišemo `jupyter notebook`. Nato v seznamu poiščemo pravo datoteko, jo odpremo, po želji spremenimo in poženemo vse celice, nato pa v orodni vrstici izberemo `File > Save and Export Notebook As > PDF`.
