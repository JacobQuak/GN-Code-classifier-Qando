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

Je moet initieel een dataset uploaden waarin bestaande productomschrijvingen en GN-codes zijn opgeslagen als tekst. Volg deze stappen:

### 1. Maak een `documents` tabel aan met minimaal deze kolommen:

| Kolomnaam     | Type        | Opmerking                               |
|---------------|-------------|-----------------------------------------|
| `id`          | UUID        | Primaire sleutel (automatisch)          |
| `content`     | TEXT        | Productomschrijving                     |
| `metadata`    | JSONB       | (optioneel) bevat bv. GN-code info      |
| `embedding`   | VECTOR(1536)| Wordt later gevuld met embeddings       |

> ⚠️ Zorg dat je `embedding` kolom het juiste vectorformaat gebruikt (bijv. 1536 voor `text-embedding-ada-002`).

---

### 2. Upload data via SQL of Supabase UI

Voorbeeld-SQL:

```sql
INSERT INTO documents (content, metadata)
VALUES
  (
    'Industriële ventilator met metalen behuizing voor wandmontage',
    '{"gn_code": "8414.59.20"}'
  );
```

Je kunt ook handmatig rijen invoeren via de Supabase Table Editor.

---

### 3. Genereer en voeg embeddings toe

Gebruik een n8n-workflow of een script (bijv. Python) dat:

- De `content`-kolom ophaalt
- Deze doorstuurt naar OpenAI voor vectorisatie
- De verkregen embedding opslaat in de `embedding` kolom van dezelfde rij

**n8n setup**:

1. Gebruik node `Supabase Select` om records op te halen zonder `embedding`.
2. Gebruik `OpenAI Embeddings` node op de `content` veldwaarde.
3. Update embedding in Supabase met `Supabase Update`.

---

## 📥 Voorbeeld: GN-codes importeren vanuit Excel

Je kunt een Excel-bestand met GN-codes en omschrijvingen uploaden naar Supabase via een n8n-workflow.

### 📄 Structuur van het Excel-bestand

Het Excel-bestand bevat bijvoorbeeld de volgende kolommen:

| CN2022 (GN-code) | Symbool | Omschrijving |
|------------------|---------|--------------|
| 1012100          | p/st    | Fokpaarden van zuiver ras |
| 1012910          | p/st    | Slachtpaarden             |
| ...              | ...     | ...                       |

### 🔁 Workflowstappen

1. **Lees het Excel-bestand in n8n** met een `Read Binary File` of `Microsoft Outlook Trigger`.
2. **Gebruik een `Spreadsheet File` node** om de rijen te extraheren.
3. **Maak JSON-records aan** waarbij je `Omschrijving` als `content` gebruikt, en `CN2022` en `Symbool` als `metadata`:

```json
{
  "content": "Fokpaarden van zuiver ras",
  "metadata": {
    "gn
