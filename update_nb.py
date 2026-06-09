import json
from pathlib import Path
path = Path('AircraftAccidents.ipynb')
with path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

found = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and any('possible_files' in line for line in cell['source']):
        cell['source'] = [
            'possible_files = [\n',
            '    "Airplane_Crashes_and_Fatalities_Since_1908.csv",\n',
            '    "airplane-crashes-since-1908.csv"\n',
            ']\n',
            'df = None\n',
            'for filename in possible_files:\n',
            '    if os.path.exists(filename):\n',
            '        df = pd.read_csv(filename, low_memory=False, encoding="utf-8")\n',
            '        break\n',
            'if df is None:\n',
            '    raise FileNotFoundError("Dataset nie został znaleziony lokalnie. Umieść plik CSV w katalogu roboczym.")\n',
            'print("Wczytano wierszy:", len(df))\n',
            'df.head()\n'
        ]
        found = True
        break

if not found:
    raise ValueError('Nie znaleziono komórki ze zmienną possible_files.')

extra_cells = [
    {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '## Dodatkowe wykresy i wyjaśnienia\n',
            'Poniżej znajdują się dodatkowe wizualizacje obrazujące rozkład ofiar oraz zależności między typem samolotu, przyczyną i śmiertelnością.\n'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [
            'plt.figure(figsize=(12,6))\n',
            'sns.countplot(data=df, y="CauseCategory", order=df["CauseCategory"].value_counts().index, palette="viridis")\n',
            'plt.title("Liczność kategorii przyczyn katastrof")\n',
            'plt.xlabel("Liczba zdarzeń")\n',
            'plt.ylabel("CauseCategory")\n',
            'plt.tight_layout()\n',
            'plt.show()\n'
        ]
    },
    {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            'Ten wykres pokazuje, które kategorie przyczyn występują najczęściej w analizowanym zbiorze.\n'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [
            'top_models = df["AC Type"].value_counts().head(10).index\n',
            'plt.figure(figsize=(12,6))\n',
            'sns.boxplot(data=df[df["AC Type"].isin(top_models)], x="AC Type", y="FatalityRate")\n',
            'plt.xticks(rotation=45, ha="right")\n',
            'plt.title("Rozkład FatalityRate dla 10 najczęściej występujących modeli")\n',
            'plt.ylabel("FatalityRate")\n',
            'plt.xlabel("AC Type")\n',
            'plt.tight_layout()\n',
            'plt.show()\n'
        ]
    },
    {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            'Boxplot przedstawia rozkład współczynnika śmiertelności dla najpopularniejszych modeli, co pomaga zidentyfikować modele o najwyższej zmienności i największych wartości.\n'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [
            'plt.figure(figsize=(10,6))\n',
            'sns.scatterplot(data=df, x="Aboard", y="FatalityRate", hue="CauseCategory", alpha=0.7)\n',
            'plt.title("Związek między liczbą osób na pokładzie a wskaźnikiem śmiertelności")\n',
            'plt.xlabel("Aboard")\n',
            'plt.ylabel("FatalityRate")\n',
            'plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")\n',
            'plt.tight_layout()\n',
            'plt.show()\n'
        ]
    },
    {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            'Ten wykres pozwala ocenić, czy większe wypadki mają tendencję do wyższej śmiertelności oraz jak kategorie przyczyn rozkładają się w zależności od liczby osób na pokładzie.\n'
        ]
    },
    {
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [
            'plt.figure(figsize=(12,6))\n',
            'sns.lineplot(data=df.groupby("Year")["FatalityRate"].mean().reset_index(), x="Year", y="FatalityRate")\n',
            'plt.title("Średni FatalityRate w kolejnych latach")\n',
            'plt.ylabel("FatalityRate")\n',
            'plt.xlabel("Year")\n',
            'plt.tight_layout()\n',
            'plt.show()\n'
        ]
    },
    {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            'Analiza trendów rocznych pomaga zrozumieć, jak zmieniał się poziom śmiertelności w sporcie lotniczym na przestrzeni czasu.\n'
        ]
    },
    {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '## Uwagi\n',
            'Aby notebook mógł się uruchomić, należy umieścić plik CSV z danymi w katalogu projektu lub dostarczyć odpowiedni mechanizm pobierania danych.\n'
        ]
    }
]

nb['cells'].extend(extra_cells)
with path.open('w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
print('Notebook zaktualizowany o dodatkowe wykresy i wyjaśnienia')
