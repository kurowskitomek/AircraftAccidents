import glob
from nbclient import NotebookClient
from nbformat import read, write
from pathlib import Path

possible_files = glob.glob("Airplane_Crashes_and_Fatalities_Since_1908*.csv") + glob.glob("airplane-crashes-since-1908*.csv")
if not possible_files:
    raise FileNotFoundError(
        "Nie znaleziono pliku CSV z danymi. Umieść go w katalogu projektu."
    )
print("Znaleziono plik danych:", possible_files[0])

path = Path('AircraftAccidents.ipynb')
with path.open('r', encoding='utf-8') as f:
    nb = read(f, as_version=4)

client = NotebookClient(nb, timeout=600, kernel_name='python3')
client.execute()

out_path = path.parent / 'AircraftAccidents_executed.ipynb'
with out_path.open('w', encoding='utf-8') as f:
    write(nb, f)

print('Execution complete')
