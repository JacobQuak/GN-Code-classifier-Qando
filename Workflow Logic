# 🔄 Workflow Logica: Loops, Batches & Triggers

In deze file leggen we uit hoe de workflow items verwerkt in batches, en hoe timing en herhaling geregeld worden.

---

## ⏰ Microsoft Outlook Trigger

- Trigger: bij elke nieuwe e-mail met bijlage
- Polling mode: `everyMinute`

---

## 🔁 Batchverwerking

### Loop Over Items & SplitInBatches

- `Loop Over Items1` – verwerkt alle Excel-rijen met 1 item per batch.
- `Loop Over Items` – tweede iteratie met bewerking van geclassificeerde resultaten.
- `batchSize`: 10 (voor performance en API limieten)

---

## ⏳ Wait nodes

- `Wait` tussen loop en verwerking om throttling of race conditions te vermijden.
- `Wait2` aan einde van flow als buffer voor outputverwerking.

---

## 📌 Waarom deze structuur?

- Beperkt foutkansen door async calls (zoals AI of internet lookup).
- Biedt schaalbaarheid voor grotere Excel-bestanden.
- Houdt het proces stabiel binnen API limieten van Microsoft & OpenAI.
