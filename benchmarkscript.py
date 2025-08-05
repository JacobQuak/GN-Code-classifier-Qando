
import pandas as pd

def gn_score(true_code, pred_code):
    """Berekent geschaalde nauwkeurigheid voor GN-codes op basis van aantal correcte begin-cijfers."""
    true_code = str(true_code).strip()
    pred_code = str(pred_code).strip()
    
    max_len = min(len(true_code), len(pred_code), 8)
    correct = 0
    for i in range(max_len):
        if true_code[i] == pred_code[i]:
            correct += 1
        else:
            break  # stop bij eerste fout
    
    # Vertaal aantal correcte cijfers naar score
    if correct == 8:
        return 100
    elif correct >= 6:
        return 75
    elif correct >= 4:
        return 50
    elif correct >= 2:
        return 25
    else:
        return 0

# Laad je Excel-bestand
bestandspad = "/Users/jacobquak/Downloads/Qando GPT based Enrichement Articles with GN codes.xlsx"  # ← pas dit aan
df = pd.read_excel(bestandspad)

# Verwijder rijen zonder codes
df_clean = df.dropna(subset=["Goederencode", "Column1"])

# Bereken GN-score per regel
df_clean["GN-score"] = df_clean.apply(lambda row: gn_score(row["Goederencode"], row["Column1"]), axis=1)

# Gemiddelde nauwkeurigheid over alle regels
gemiddelde_score = df_clean["GN-score"].mean()
# Zorg dat alle rijen zichtbaar zijn
import pandas as pd
pd.set_option('display.max_rows', None)

# Toon alleen relevante kolommen met scores
print(df_clean[["Goederencode", "Column1", "GN-score"]])

# Resultaat

print(df_clean[["Goederencode", "Column1", "GN-score"]])
print(f"\nGemiddelde GN-code nauwkeurigheidsscore: {gemiddelde_score:.2f}%")
