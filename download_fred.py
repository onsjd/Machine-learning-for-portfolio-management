"""Optional refresh; modifies data snapshots. Re-run notebook 03 after downloading."""
from pathlib import Path
from urllib.request import urlopen
root=Path(__file__).resolve().parent/'data/raw/fred'
root.mkdir(parents=True,exist_ok=True)
for sid in ['VIXCLS','DTWEXBGS','DGS10','DGS2']:
    url=f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd=1999-01-01&coed=2025-12-31'
    with urlopen(url,timeout=60) as response:
        (root/f'{sid}.csv').write_bytes(response.read())
    print(sid)
