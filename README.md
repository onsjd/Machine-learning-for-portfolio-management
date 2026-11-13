# Commodity market regimes and dynamic portfolio allocation

**Notebook à rendre : [Final_Research_Notebook.ipynb](Final_Research_Notebook.ipynb).**

Projet de cours — Ons Jdey et Senghak Rou, ENSAE, novembre 2026.

Le notebook autonome rassemble les prix World Bank, les indicateurs FRED, le sentiment annoté des actualités sur l'or, les régimes K-Means/GMM et les portefeuilles de Markowitz conditionnés. Les cinq actifs sont le Brent, le gaz américain, l'or, l'argent et le cuivre.

## Fichier à rendre et organisation

- **À rendre : `Final_Research_Notebook.ipynb`**, seul notebook à la racine.
- `old_work/` : cinq notebooks intermédiaires conservés pour la traçabilité.
- `data/` : données sources ; à conserver dans le dépôt.
- `results/` : sorties historiques, non nécessaires à l’exécution du notebook final.

## Exécution

Avec Python 3.12, installer `pip install -r requirements.txt`, ouvrir `jupyter lab Final_Research_Notebook.ipynb`, puis redémarrer le noyau et exécuter toutes les cellules. Les versions testées figurent dans la section 7 et `environment_used.json`.

Aucune clé API n'est nécessaire. Les fichiers locaux sont utilisés lorsqu'ils existent ; sinon, les données sont téléchargées depuis des révisions figées et vérifiées par SHA-256. Une connexion internet est nécessaire pour les news lorsqu'elles ne sont pas disponibles localement. Le notebook ne nécessite pas l'exécution des notebooks historiques.

## Protocole et résultats

- Expérience A : entraînement avril 2006–2012, validation 2013–2015, évaluation juillet 2016–décembre 2018 (30 mois), avec sentiment.
- Expérience B : entraînement avril 2006–2015, validation 2016–2020, évaluation mars 2021–décembre 2025 (58 mois), sans sentiment.
- Modèles figés avant évaluation, décalage de deux mois, historique glissant de 120 mois, portefeuilles long-only, plafond initial 60 %, coûts de 10 points de base.
- Les régimes modifient les allocations, mais aucun gain robuste et répété n'est établi. Les conclusions concernent ce protocole et cet indice de sentiment sur l'or.

## Analyses exploratoires supplémentaires — section 5.2

1. Rendements seuls, covariance seule ou les deux : régimes de prix, deux algorithmes et deux périodes.
2. Avec/sans sentiment à nombre de groupes identique : deux algorithmes, avec/sans FRED, k = 2, 3 et 4.
3. Plafonds de concentration de 40 %, 50 % et 60 % : chaque stratégie est comparée à Markowitz sous le même plafond.

Toutes les variantes sont rapportées, sans sélectionner la meilleure après observation des performances. Les intervalles bootstrap sont exploratoires et non corrigés pour comparaisons multiples.

## Limites et historique

Les variations de prix moyens mensuels ne sont pas des rendements directement investissables. Les snapshots révisés, les annotations rétrospectives et l'indice dollar reconstruit empêchent une interprétation entièrement point-in-time. Les deux fenêtres avaient déjà été examinées ; elles ne constituent pas un nouvel échantillon de confirmation.

Les notebooks intermédiaires 01–05 sont regroupés dans [`old_work/`](old_work/README.md). Ils documentent les étapes de recherche et ne sont pas nécessaires pour exécuter ou évaluer le notebook final. Les données et résultats historiques restent disponibles. `run_notebooks.py` exécute seulement les notebooks historiques 01–03 dans `old_work/` ; pour le rendu complet, utiliser le notebook final. HMM et risk parity ne sont pas implémentés.
