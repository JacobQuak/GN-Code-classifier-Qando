# 🧠 AI Agents: Beschrijvingagent & GN agent

Deze file beschrijft de werking van twee cruciale AI-agents in de workflow: de `Beschrijvingagent` en de `GN agent`.

---

## 📌 Beschrijvingagent

**Doel:** Genereert een technische, zakelijke productomschrijving (max. 2 regels) op basis van input en webbronnen.

**Promptkenmerken:**
- Zoek naar technische specificaties via een externe workflow (“Internet Agent”).
- Gebruik alleen betrouwbare bronnen: datasheets, fabrikantensites.
- Vermijd marketingtaal of merknamen.
- Output is een korte beschrijving met nadruk op technische kenmerken zoals materiaal, werking, afmetingen of capaciteit.

**Voorbeeldoutput:**
> Elektrisch aangedreven industriële ventilator met metalen behuizing, geschikt voor wandmontage. Luchtverplaatsing tot 3000 m³/h bij 230V.

---

## 🧮 GN Agent

**Doel:** Classificeert een productomschrijving in een correcte GN-code met omschrijving, gebruikmakend van RAG + vector store.

**Promptkenmerken:**
- Gebruik Supabase vector store om gelijkaardige productomschrijvingen te vinden.
- Selecteer de meest geschikte GN-code op basis van technische details.
- Verwacht JSON-only output:
```json
{"gn_code": "...", "gn_omschrijving": "...", "product_omschrijving": "..."}
```

**Foutafhandeling:** Alleen correcte JSON-output wordt geparsed. Anders wordt een foutmelding getoond of het proces overgeslagen.
