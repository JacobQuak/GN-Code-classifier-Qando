# 🧩 Supabase Vector Store & Embeddings

Deze file beschrijft het RAG-component van de workflow op basis van een Supabase vector store in combinatie met OpenAI embeddings.

---

## 🔍 Wat doet deze component?

- Zet productomschrijvingen om in vectorrepresentaties met `OpenAI Embeddings`.
- Zoekt de meest relevante bestaande omschrijving in de vector store `documents`.
- Retourneert de top 10 dichtstbijzijnde resultaten (`topK: 10`).

---

## 🧠 Embeddings node

- **Gebruikt model**: `text-embedding-ada-002` (via GPT-4o-mini).
- **Doel**: converteert vrije tekst naar een vector die semantische betekenis bevat.

---

## 📚 Vector Store (Supabase)

- **Tabelnaam**: `documents`
- **Zoekmethode**: cosine similarity
- **Aantal resultaten**: `topK: 10`
- **Gebruik**: wordt geraadpleegd door de GN Agent via Retrieval-Augmented Generation (RAG).

---

## 🧾 Hoe voeg je data toe aan Supabase?

Je kunt op twee manieren data toevoegen aan Supabase:

---

### 🔧 1. Via SQL of Supabase UI (handmatig)

#### 📄 Tabelstructuur

| Kolomnaam     | Type        | Opmerking                               |
|---------------|-------------|-----------------------------------------|
| `id`          | UUID        | Primaire sleutel (automatisch)          |
| `content`     | TEXT        | Productomschrijving                     |
| `metadata`    | JSONB       | (optioneel) bevat bv. GN-code info      |
| `embedding`   | VECTOR(1536)| Wordt later gevuld met embeddings       |

> ⚠️ Zorg dat je `embedding` kolom het juiste vectorformaat gebruikt (bijv. 1536 voor `text-embedding-ada-002`).

#### 📥 SQL Voorbeeld

```sql
INSERT INTO documents (content, metadata)
VALUES
  (
    'Industriële ventilator met metalen behuizing voor wandmontage',
    '{"gn_code": "8414.59.20"}'
  );
```

#### 🧠 Embeddings toevoegen

Gebruik n8n of een script (zoals Python) om de `content` te vectoriseren en op te slaan in de `embedding` kolom.

---

### ⚙️ 2. Via n8n: Add Documents to Vector Store node

Dit is de aanbevolen en meest geautomatiseerde methode.

#### 📄 Voorbeeld Excel

| CN2022 | Symbool | Omschrijving                         |
|--------|---------|--------------------------------------|
| 1012100| p/st    | Fokpaarden van zuiver ras            |
| 1012910| p/st    | Slachtpaarden                        |

#### 🔁 Workflow in n8n

1. **Lees het Excel-bestand in**, bijvoorbeeld via:
   - `Microsoft Outlook Trigger` + bijlage
   - `Read Binary File` + `Spreadsheet File` node

2. **Transformeer naar JSON** met deze structuur:

```json
{
  "content": "Fokpaarden van zuiver ras",
  "metadata": {
    "gn_code": "1012100",
    "symbool": "p/st"
  }
}
```

3. **Gebruik `Add Documents to Vector Store` node**:
   - Kies de Supabase Vector Store
   - Geef het veld `content` op voor vectorisatie
   - Voeg metadata toe indien nodig

De node:
- Genereert automatisch de embedding via OpenAI
- Slaat het op in de `documents` tabel in Supabase

---

## ✅ Best practices

- Upload alleen relevante en technisch correcte omschrijvingen
- Gebruik consistente stijl en terminologie
- Bewaar GN-code en eenheid in `metadata` voor later gebruik
- Herstructureer of her-embed bij grote updates
