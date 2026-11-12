# Commodity market regimes and dynamic portfolio allocation

**Notebook à rendre : `Final_Research_Notebook.ipynb`.** Il regroupe l'ensemble du projet (régimes K-Means/GMM, FRED, sentiment des news, portefeuilles) en deux expériences chronologiques (juil. 2016–déc. 2018 et mars 2021–déc. 2025). Il est autonome : il lit les données du dépôt si elles sont présentes, sinon il les télécharge depuis des révisions figées, avec vérification SHA-256 (connexion internet nécessaire pour les news). Les notebooks 01–05 ci-dessous restent disponibles comme historique de travail.

Données réelles World Bank et notebook exécuté, sans news ni sentiment.

## Démarrage
1. Cloner ce dépôt : `git clone https://github.com/onsjd/Machine-learning-for-portfolio-management.git`.
2. Ouvrir un terminal à la racine du dépôt.
3. Facultatif : créer un environnement `python -m venv .venv`, puis l’activer.
4. Installer : `pip install -r requirements.txt`.
5. Lancer : `jupyter lab 01_market_regimes.ipynb`, puis Run All.

Aucune clé API et aucun téléchargement requis pour exécuter le notebook.
Les graphiques et tableaux sont déjà enregistrés dans les cellules.

## Contenu
- `data/raw/world_bank_monthly.xlsx` : fichier original téléchargé.
- `data/sources.json` : liens, unités, date et empreinte SHA-256.
- `data/processed/prices_full_history.csv` : historique disponible des cinq séries.
- `data/processed/prices_2000_2025.csv` : échantillon étudié.
- `data/processed/features.csv` : variables calculées par le notebook.
- `01_market_regimes.ipynb` : exploration, K-Means, GMM, validation temporelle, interprétation.
- `results/` : graphiques et résultats CSV.

## Méthodologie
Train : jusqu'à fin 2015. Validation : 2016–2020. Test : 2021–2025.
Les variables contiennent un historique glissant de 12 mois, d'où une période de chauffe.
Standardisation apprise sur train seulement pour la sélection, puis réapprise sur train + validation pour le test.
Le nombre de groupes K-Means est choisi par silhouette en validation ; celui du GMM par BIC sur train.
Modèles figés pendant le test. Pas d’optimisation de portefeuille dans cette première partie.

## Limites
Prix moyens mensuels physiques, non rendements investissables. Le fichier est un snapshot révisé et non une base de données disponible en temps réel à chaque date.
Ne pas interpréter les diagnostics de prix comme une performance de futures/ETF. La date de publication doit être prise en compte avant toute stratégie.
Les modèles de régimes ne garantissent pas de prévisibilité. Aucun résultat n'a été fabriqué.

## Partie 2 : comparaison de portefeuilles
Ouvrir `02_portfolio_comparison.ipynb`, indépendant du premier notebook.
Quatre stratégies : équipondération, Markowitz classique, Markowitz avec K-Means et Markowitz avec GMM.
Test commun mars 2021–décembre 2025 ; modèles figés fin 2020 ; signaux et historique décalés de deux mois.
Fenêtre 120 mois ; long only ; somme des poids 1 ; plafond 60% ; gamma 5 ; régularisation des moyennes et covariances.
Coûts 10 bp sur la somme des transactions absolues, poids pré-trade corrigés de leur dérive. Sensibilité 0/10/25 bp.
Graphiques, poids, rendements, métriques, audit temporel et bootstrap apparié disponibles dans `results/portfolios/`.
Ces comparaisons sont illustratives sur prix moyens World Bank : aucune performance investissable n'est revendiquée.

## Partie 3 : World Bank + FRED (version mise à jour)
Commencer par `03_fred_regimes_portfolios.ipynb` pour la comparaison complète avec FRED. Il est indépendant et déjà exécuté.
FRED : VIXCLS, DTWEXBGS, DGS10, DGS2. CSV quotidiens réels inclus dans `data/raw/fred/`. Agrégation mensuelle et sources documentées.
Six stratégies sur les mêmes dates, avec/sans FRED pour chaque algorithme ; indicateurs explicatifs seulement, les actifs restent les cinq commodities.
Le dollar commence en 2006 : les modèles avec/sans FRED sont entraînés sur une période commune réduite pour isoler l’apport des indicateurs.
Les deux anciens notebooks et leurs résultats restent disponibles. Les comparaisons correspondantes diffèrent parce que l’historique de clustering est différent.
Le test déjà inspecté rend cette nouvelle comparaison exploratoire. Aucune conclusion d’investissement ne doit être tirée de ces prix moyens mensuels.
Résultats, comparaisons appariées et coûts dans `results/fred_extension/`. Aucune news.

## Projet de cours
Équipe : Ons Jdey et Senghak Rou.
Sujet : détection des régimes de marché et sentiment des news pour l’allocation dynamique en matières premières.
Référence du cours : https://github.com/schampon/skfin/tree/master/nbs

## État du projet
Les trois notebooks, données sources et résultats existants sont inclus.
La partie news/sentiment et son évaluation incrémentale restent à développer.
Le HMM et la comparaison risk parity ne sont pas implémentés dans cette version.

## Reproduire les calculs sans Jupyter
`python run_notebooks.py` exécute les cellules Python des trois notebooks dans l’ordre, avec leurs assertions.
Les résultats et graphiques sont régénérés dans `results/`. Les sorties des notebooks restent celles du snapshot original ; utiliser Jupyter Run All pour les actualiser.
