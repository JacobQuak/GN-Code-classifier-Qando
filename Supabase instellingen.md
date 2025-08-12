## 🧭 Supabase gegevens ophalen voor n8n configuratie

Om de **Supabase Node** of een **PostgreSQL-node** correct in te stellen in n8n, heb je specifieke verbindingsgegevens nodig. Je vindt deze eenvoudig via het **Supabase Dashboard**.

---

### 📍 Stap 1: Ga naar je Supabase Project

1. Log in op [https://app.supabase.com](https://app.supabase.com)
2. Klik op je project (bijv. **Qando project**)

---

### 🔢 Stap 2: Vind je Projectgegevens

Ga naar:  
**Project Settings → General**

Hier vind je:
- **Project Name** – zoals `Qando project`
- **Project ID** – bijv. `ucxnrglveqovfwhqqrp`  
  Deze heb je o.a. nodig voor de PostgreSQL-gebruiker en als identifier in API-calls.

---

### 🛠️ Stap 3: Database Connectiegegevens ophalen

Ga in het linker menu naar:  
**Project Settings → Database → Connection Info**

Daar zie je de instellingen voor meerdere verbindingstypes:

#### 🔌 Direct connection

Gebruik deze als je een dedicated verbinding wilt instellen (langdurige sessies):
postgresql://postgres:[YOUR-PASSWORD]@db.ucxnrglveqovfwhqqrp.supabase.co:5432/postgres


#### 🔁 Transaction Pooler

Gebruik deze voor stateless toepassingen zoals serverless of n8n:

**Belangrijke parameters voor het instellen van de Postgres Chat Memory node in n8n:**

| Parameter      | Waarde                                                           |
|----------------|------------------------------------------------------------------|
| **Host**       | `aws-0-eu-central-1.pooler.supabase.com`                         |
| **Port**       | `6543`                                                           |
| **Database**   | `postgres`                                                       |
| **User**       | `postgres.ucxnrglveqovfwhqqrp`                                    |
| **Password**   | Staat **niet zichtbaar** in de UI, maar moet je zelf ingesteld hebben |
| **Pool Mode**  | `transaction`                                                    |

Gebruik deze gegevens in n8n's PostgreSQL-node of Supabase-node via de **Credential Manager**.

> 🔐 Je wachtwoord kun je terugvinden of opnieuw instellen onder de Database settings.

---

### 🗝️ Stap 4: Vind je API Keys

Ga naar:  
**Project Settings → API Keys**

Daar vind je:
- `anon` public API key (lezen)
- `service_role` API key (lezen en schrijven – alleen server-side gebruiken!)
> `service_role_secret` wordt gevraagd om in te stellen in de Supabase Vector Store tool

Gebruik deze API keys in n8n wanneer je met Supabase werkt via REST of GraphQL.

---

## 📌 Samengevat: Waar vind je wat?

| Gegeven                | Waar in de UI                                           |
|------------------------|----------------------------------------------------------|
| Project ID             | `Settings → General`                                     |
| DB host / port / user  | `Settings → Database → Connection Info`                 |
| API key                | `Settings → API Keys`                                    |
| Wachtwoord             | Zelf ingesteld of via `.env` bij project setup          |

---

## ✅ Tip

Zodra je deze gegevens hebt:
- Voeg ze in **n8n's Credential Manager** in bij het aanmaken van een PostgreSQL- of Supabase-verbinding.
- Gebruik `transaction pooler` als je werkt met veel korte verzoeken (zoals in n8n workflows).
- Gebruik de juiste poort (vaak `5432` voor direct, `6543` voor pooler).

