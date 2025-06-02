# 🎓 Student Score Prediction

Projet de régression supervisée visant à prédire le score en mathématiques des élèves à partir de données démographiques et scolaires.

---

## 📌 Objectif du Projet

Prédire les résultats en mathématiques d'étudiants à l’aide d’informations telles que :
- le sexe,
- le niveau d’éducation des parents,
- le type de déjeuner,
- la participation à un cours de préparation,
- etc.

---

## 📁 Source des Données

- **Titre** : [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Origine** : Kaggle
- **Tâche** : Régression
- **Taille** : 1000 lignes × 8 colonnes

---

## 🧠 Pourquoi ce projet ?

Ce projet m’a intéressé car il allie **data science** et **éducation**, un domaine où les données peuvent être utilisées pour améliorer les résultats scolaires. C’est aussi une très bonne opportunité de :
- pratiquer le **prétraitement de données réelles**,
- appliquer des modèles de **régression**,
- et évaluer leur performance.

---

## 🔧 Étapes du projet

### 1. Prétraitement
- Nettoyage du dataset
- Encodage des variables catégorielles (LabelEncoder, OneHotEncoder)
- Normalisation si nécessaire

### 2. Visualisation
- Matrice de corrélation
- Graphiques exploratoires (barres, boxplots)

### 3. Ingénierie des Caractéristiques
- Transformation de variables
- Sélection de variables pertinentes

### 4. Modélisation
- Modèle : Régression Linéaire (et comparaison avec d'autres modèles)
- Séparation train/test : 80/20
- Entraînement du modèle avec `scikit-learn`

### 5. Évaluation
- Métriques utilisées : `R²`, `MAE`, `RMSE`
- Courbe de régression / résidus

---

## 🧪 Résultats

- **R² Score** :  0.18
- **MAE** : 5.1
- Le **niveau d’éducation des parents** et la **préparation au test** sont des facteurs importants.

---

## 🚧 Défis rencontrés

- Traitement des variables catégorielles multiples
- Visualisation efficace pour explorer les données
- Choix du bon modèle avec les bonnes hypothèses

---

## 💻 Technologies utilisées

- Python 3.10
- Scikit-Learn
- Pandas
- Seaborn / Matplotlib
- Jupyter Notebook / PyCharm

---

## 📦 Structure du projet

student_score_prediction/
│
# Données sources
│ └── StudentsPerformance.csv
│ 
src/# Scripts Python
│ ├── preprocessing.py
│ ├── feature_engineering.py
│ └── model_training.py
│
├── requirements.txt # Librairies Python utilisées
├── README.md # Présentation du projet
└── main.py # Script principal (optionnel)



---

## 🔗 Lien du projet

🔍 [Voir le dépôt GitHub](https://github.com/axel-yarell/student_score_prediction)

---

## 📬 Contact

Axel Yarell  
[GitHub](https://github.com/axel-yarell)
