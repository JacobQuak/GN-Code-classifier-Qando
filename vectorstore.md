# 🧩 Supabase Vector Store & Embeddings

Deze file beschrijft het RAG-component van de workflow op basis van een Supabase vector store in combinatie met OpenAI embeddings.

---

## 🔍 Wat doet deze component?

- Zet productomschrijvingen om in vectorrepresentaties met `OpenAI Embeddings`.
- Zoekt de meest relevante bestaande omschrijving in de vector store `documents`.
- Retourneert de top 10 dichtstbijzijnde resultaten (`topK: 10`).

---

## 🧠 Embeddings node

- Gebruikt: `text-embedding-ada-002` (via GPT-4o-mini).
- Doel: converteert vrije tekst naar een vector die semantische betekenis bevat.

---

## 📚 Vector Store (Supabase)

- Tabellen: `documents`
- Zoekmethode: cosine similarity
- Aantal resultaten: `topK: 10`
- Gebruikt als input voor `GN Agent` in RAG-mode

---

## 🛠 Tips

- Zorg dat je Supabase API key correct is ingesteld in n8n.
- Upload enkel relevante, gestandaardiseerde productomschrijvingen als vector store content.
