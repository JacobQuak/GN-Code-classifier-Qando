# 🧪 GN-code Classifier Benchmarking

Deze module voert een nauwkeurigheidsmeting uit op een GN-code classifier. De classifier probeert automatisch producten te koppelen aan de juiste **GN-code** (Gecombineerde Nomenclatuur, 8-cijferige code), gebaseerd op een referentieomschrijving.

---

## ⚙️ Werking van de Benchmark

Het Python-script vergelijkt voor elk geclassificeerd product de **voorgestelde GN-code** van het model met de **referentiecode** uit een Excel-document. De evaluatie is gebaseerd op het aantal overeenkomende cijfers van links naar rechts:

| Overeenkomende cijfers | Score (%) |
|------------------------|-----------|
| 2 cijfers              | 25%       |
| 4 cijfers              | 50%       |
| 6 cijfers              | 75%       |
| 8 cijfers (volledig)   | 100%      |

Voorbeeld:
- Referentiecode: `84145915`
- Voorspelde code: `84140000` → 4 cijfers matchen → **50% score**

De gemiddelde score over alle producten wordt berekend als **de nauwkeurigheid van de classifier**.

---

## 📁 Vereisten

1. **Python-script:**  
   Zorg dat het evaluatiescript (`benchmark_gn_classifier.py`) beschikbaar is in je projectdirectory.

2. **Excel-bestand met referentiegegevens:**  
   Het script verwacht een Excel-bestand met:
   - Minstens één kolom met de **referentie GN-codes**
   - Een tweede kolom met de **geclassificeerde GN-codes**
   - De **exacte naam** van het bestand en kolommen moeten overeenkomen met wat in het script is gedefinieerd

3. **Kolomnamen:**  
   Pas de kolomnamen aan in het script als jouw Excel andere headers gebruikt.

---

## 🧠 Hoe te gebruiken

1. Zorg dat je Excel-bestand op je machine staat met de juiste naam (bijv. `gn_classification_results.xlsx`)
2. Controleer of de kolomnamen kloppen met het script:
   ```python
   REF_COL = "referentiecode"
   PRED_COL = "geclassificeerde_code"
