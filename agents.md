# 🤖 AI Agents Workflow

Deze workflow bestaat uit drie op elkaar afgestemde AI-agents die samen zorgen voor een accurate technische productomschrijving en bijbehorende GN-code. Elk onderdeel heeft een duidelijke functie binnen de pipeline.

---

## 🔍 Zoektermagent (Search Query Enricher)

### 🎯 Doel
Genereert een slimme zoekterm gebaseerd op de productomschrijving en het fabrikaat. Deze zoekterm wordt later gebruikt om technische gegevens van het internet op te halen.

### ⚙️ Werking
- Neemt als input: productomschrijving + fabrikant.
- Vormt een verrijkte zoekprompt met relevante technische zoekwoorden.
- Deze prompt wordt doorgestuurd naar de **Internetagent**, die hiermee online zoekt naar betrouwbare informatie.

### 📈 Gebruik in workflow
- Vormt de brug tussen ruwe inputdata en web scraping.
- **Output:** geoptimaliseerde zoekterm voor externe datascraping.

---

## 🌐 Internetagent (Scraper + Interpreter)

### 🎯 Doel
Voert een gerichte online zoekactie uit op basis van de zoekterm die afkomstig is van de Zoektermagent.

### ⚙️ Werking
- Maakt gebruik van een scraper gebaseerd op **Serper.dev (Google)**.
- Bezoekt enkel betrouwbare bronnen zoals datasheets en fabrikantensites.
- Filtert de zoekresultaten en genereert een technische samenvatting van het gevonden materiaal.

### 🧾 Output
Een gestructureerde technische weergave van de online gevonden informatie (nog geen finale productomschrijving).

---

## 🧾 Beschrijvingsagent

### 🎯 Doel
Genereert een zakelijke, technische productomschrijving (max. 2 regels) op basis van de output van de Internetagent.

### 📌 Kenmerken
- Focus op feiten: geen marketingtaal of merknamen.
- Alleen technische kenmerken zoals werking, materiaal, afmetingen, spanning, capaciteit, enz.
- Leunt op externe technische bronnen (gevalideerd via de internetagent).

### 💬 Voorbeeldoutput
> Elektrisch aangedreven industriële ventilator met metalen behuizing, geschikt voor wandmontage. Luchtverplaatsing tot 3000 m³/h bij 230V.

---

## 🧮 GN Agent

### 🎯 Doel
Classificeert het product in een correcte **GN-code (Gecombineerde Nomenclatuur)** inclusief omschrijving, op basis van de technische productomschrijving.

### ⚙️ Werking
- Gebruikt een **Supabase vector store** waarin duizenden GN-codevoorbeelden zitten.
- Door middel van **Retrieval-Augmented Generation (RAG)** wordt de meest passende GN-code gezocht.
- Output wordt **strikt in JSON-formaat** gegenereerd.

### 📤 Outputformaat (vereist)
```json
{
  "gn_code": "84145915",
  "gn_omschrijving": "Industrieventilatoren met elektrische aandrijving",
  "product_omschrijving": "Industriële ventilator met metalen behuizing, luchtverplaatsing tot 3000 m³/h bij 230V"
}

