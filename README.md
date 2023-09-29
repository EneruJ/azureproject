# Système de Surveillance Environnementale pour Jardins Urbains
Ce projet vise à fournir une solution robuste pour la surveillance environnementale des jardins urbains en utilisant une API.

## Problématique
Les jardins urbains gagnent en popularité, mais leur maintenance requiert une compréhension précise des conditions environnementales. Pour garantir un environnement optimal pour la croissance des plantes et la biodiversité, il est crucial d'avoir accès à des données précises et en temps réel sur différents paramètres environnementaux.

## Solution
Notre solution est une API qui recueille, traite et fournit des données environnementales essentielles pour les jardins urbains. Ces données peuvent être utilisées par les jardiniers, les chercheurs et les décideurs pour optimiser la croissance des plantes, surveiller l'impact environnemental et prendre des décisions éclairées concernant la gestion du jardin.

## Étapes d'Implémentation
### 1. Configuration initiale
a. Environnement Azure : Avant tout développement, un environnement Azure a été configuré pour permettre le déploiement et la mise en œuvre des services.

b. Création de l'App Service : Dans Azure, un App Service a été créé pour héberger notre application Flask. Cela nous a permis de déployer facilement notre API et de la rendre accessible via le web.

### 2. Développement de l'API
a. Choix du Framework : Flask a été choisi pour son caractère léger et sa flexibilité. Cela nous a permis de développer rapidement une API répondant à nos besoins.

b. Points d'accès API : Plusieurs endpoints ont été créés pour permettre aux utilisateurs d'interagir avec l'API. Parmi ces endpoints, nous avons notamment un pour récupérer toutes les données et un autre pour récupérer des données spécifiques.

c. Modèle de Données : Un modèle de données CosmosDB a été conçu pour stocker et organiser les informations environnementales. Cela a facilité le traitement et l'extraction des données.

d. Extraction des Données : Des méthodes ont été mises en place pour extraire des données de diverses sources environnementales, les traiter et les rendre disponibles via l'API.

### 3. Tests de Performance avec Locust
a. Installation et Configuration de Locust : Locust, un outil de test de performance, a été installé et configuré pour simuler différents scénarios de trafic.

b. Création du locustfile.py : Un fichier de configuration spécifique à Locust (locustfile.py) a été créé. Il définit le comportement des utilisateurs simulés et les requêtes qu'ils effectuent sur l'API.

c. Lancement des Tests : Des tests ont été réalisés pour simuler différents volumes de trafic et évaluer la capacité de l'API à gérer de nombreuses requêtes.

d. Analyse des Résultats : Après avoir exécuté les tests, les résultats ont été analysés pour déterminer les limites de performance de l'API et pour identifier les éventuels goulets d'étranglement.

### 4. Déploiement sur Azure
a. Configuration de l'Environnement : Les variables d'environnement et les paramètres nécessaires au déploiement ont été définis dans Azure.

b. Mise en ligne de l'API : L'API a été déployée sur l'App Service d'Azure à l'aide des outils de développement Azure.

c. Vérification de la mise en ligne : Après le déploiement, des tests ont été effectués pour s'assurer que l'API était fonctionnelle et accessible en ligne.

## Dépendances
- Flask: pour le développement de l'API.
- Locust: pour les tests de performance.
- Azure: pour le déploiement et l'hébergement.

## Fonctionnement
Capture d'écran de l'API en action : 
<br>
<img width="789" alt="image" src="https://github.com/EneruJ/azureproject/assets/62664268/400921f4-1ce4-42c5-b607-7b5f8cd56af9"><br>
Lien actif vers l'API : https://azprojweather.azurewebsites.net/
<br>Lien de la documentation : https://azprojdoc.blob.core.windows.net/doc/Documentation.pdf


