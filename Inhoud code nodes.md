# 💻 Code Nodes - Uitleg en Inhoud

Dit document bevat alle aangepaste `Code` nodes uit de GN-code-classificatie workflow. Elke sectie geeft de naam, functionaliteit en de bijbehorende JavaScript code weer.

---

## 1. 🧼 Code Node: `Code`

**Doel:** Schoont elke rij uit het Excel-bestand op door alle `undefined`, `null` of lege waarden te vervangen met `"onbekend"`, en trimt alle kolomnamen.

```js
// Loop over de rijen en vul lege waarden aan
const transformed = items.map(item => {
  const row = item.json;
  const cleanRow = {};

  Object.entries(row).forEach(([label, value]) => {
    cleanRow[label.trim()] = (value === undefined || value === null || value === '')
      ? 'onbekend'
      : value;
  });

  return { json: cleanRow };
});

return transformed;
```

---

## 2. 📦 Code Node: `Code1`

**Doel:** Parseert een string-uitvoer van een LLM (die een JSON-object als string retourneert) naar een echt JSON-object zodat n8n ermee verder kan werken.

```js
// Haal de input op van de vorige node
const input = $json;

// Stap 1: Haal de string op uit het juiste veld
const aiOutput = input.message.content;

// Stap 2: Parse de string naar een bruikbaar object
let parsed;
try {
  parsed = JSON.parse(aiOutput);
} catch (e) {
  throw new Error("Kon de AI-output niet parsen naar JSON: " + e.message);
}

// Stap 3: Geef het als output van de node
return [
  {
    json: parsed
  }
];
```

---

## ✅ Gebruik

Deze code-nodes zijn essentieel voor:

- **Voorbewerking** van onvolledige of ongestructureerde input uit Excel.
- **Validatie** en veilige conversie van AI-uitvoer naar bruikbare JSON in n8n.

Je kunt deze snippets direct hergebruiken of aanpassen voor soortgelijke workflows.
