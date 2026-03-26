# Analýza dat – projde student zkouškou (logistická regrese)

## Čištění dat

Dataset obsahoval několik typů chyb:

* chybějící hodnoty (např. prázdné buňky, NaN)
* neplatné hodnoty (např. "?", "invalid")
* nesprávné datové typy (text místo čísla)

### Postup čištění:

* všechny sloupce byly převedeny na číselné hodnoty pomocí `pd.to_numeric(errors="coerce")`
* neplatné hodnoty se změnily na `NaN`
* řádky s chybějícími hodnotami byly odstraněny (`dropna()`)
* dataset byl zkontrolován na duplicity

Po vyčištění zůstaly pouze validní záznamy.

---

## Vytvoření klasifikační proměnné

Byl vytvořen nový sloupec:

```id="u3c6m2"
passed = final_score >= 75
```

* 1 = student prošel
* 0 = student neprošel

### Proč klasifikace?

Nepředpovídáme přesné skóre, ale rozhodnutí (projde / neprojde), což je v praxi užitečnější.

---

## Explorace dat

Byly porovnány skupiny studentů:

### Studenti, kteří prošli:

* více studují (vyšší `study_hours`)
* mají vyšší docházku (`attendance`)

### Studenti, kteří neprošli:

* mají méně hodin studia
* nižší docházku

Hlavní rozdíl je v množství studia.

---

## Model – logistická regrese

Byl použit model:

```id="3h3n3d"
LogisticRegression()
```

Vstupní proměnné:

* study_hours
* sleep_hours
* attendance
* coffee_cups

Výstup:

* passed (0 nebo 1)

Model odhaduje pravděpodobnost, že student projde.

---

## Vyhodnocení modelu

Model byl testován na části dat.

* přesnost (accuracy) se pohybuje přibližně mezi 70–100 % (kvůli malému datasetu)
* model funguje dobře na jednoduchých případech
* hůře funguje na extrémních nebo neobvyklých datech

Dataset je malý, takže model není obecně spolehlivý.

---

## Pravděpodobnost

Model vrací pravděpodobnosti ve formátu:

```id="m3k9rz"
[0.2, 0.8]
```

* 0.2 = pravděpodobnost, že student neprojde
* 0.8 = pravděpodobnost, že student projde

Např. 0.8 znamená 80% šanci na úspěch.

---

## Threshold (rozhodovací hranice)

Standardně se používá:

```id="q3b1xt"
0.5
```

* pokud pravděpodobnost > 0.5 → student projde
* pokud < 0.5 → neprojde

Threshold lze upravit (např. 0.6 pro přísnější hodnocení).

---

## Interpretace modelu

Z koeficientů modelu vyplývá:

### Faktory, které zvyšují šanci na úspěch:

* více hodin studia (`study_hours`)
* vyšší docházka (`attendance`)

### Faktory s menším vlivem:

* káva (`coffee_cups`)
* spánek má menší, ale pozitivní vliv

Výsledky dávají smysl a odpovídají realitě.

---

## Rozhodování v praxi

Navržené pravidlo:

* pokud pravděpodobnost < 0.4 → student je rizikový

Škola by mohla:

* studenta včas upozornit
* nabídnout doučování nebo podporu

---

## Vlastní analýza

Byla vytvořena nová proměnná:

```id="q9v2sl"
effort = study_hours + attendance / 10
```

Výsledek:

* vyšší kombinované úsilí → vyšší šance projít

Kombinace více faktorů lépe vysvětluje výkon než jeden faktor.

---

## Shrnutí

* nejdůležitější faktor je studium
* docházka má také významný vliv
* model dokáže odhadnout pravděpodobnost úspěchu
* výsledky dávají smysl, ale dataset je malý

---
