# GN Code Classifier - n8n Workflow

Deze repository bevat een geavanceerde [n8n](https://n8n.io/) workflow voor het classificeren van producten op basis van hun omschrijving in combinatie met webdata en een vectorstore. De output is een correcte GN-code (Goederencode), inclusief technische omschrijving.

## ⚙️ Functionaliteiten

- 📩 **Microsoft Outlook Trigger**: Start automatisch bij nieuwe inkomende e-mails met bijlagen (Excel-bestanden).
- 📂 **Excel Extractie**: Haalt data uit Excel-bestanden.
- 🧼 **Dataopschoning**: Lege waarden worden aangevuld met `"onbekend"`.
- 🧠 **Beschrijvinggenerator**: Genereert een technische, uniforme productomschrijving via een AI-agent en gebruikt hiervoor het taalmodel GPT5-5.
- 📡 **Internet agent tool**: Haalt technische specificaties van het web.
- 📊 **Vector Store Search**: Zoekt in een Supabase vector store naar de juiste GN-code (via RAG).
- 💬 **AI Classificatie**: GPT-4o-mini wordt gebruikt om GN-code te genereren op basis van omschrijving en vectorinformatie.
- 📤 **Export naar Excel**: Resultaten worden teruggeschreven naar een gekoppeld Excel-bestand in Microsoft 365.

## 🔧 Vereisten

- Een werkende n8n-installatie (cloud).
- Microsoft Outlook- en Excel 365-accounts gekoppeld aan n8n.
- OpenAI API Key.
- Supabase instance met vector store (`documents`).

## 🚀 Installatie

1. Clone de repo:
   ```bash
   git clone https://github.com/<your-org-or-username>/gn-code-classifier-n8n.git
   cd gn-code-classifier-n8n
