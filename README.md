# 📚 Django REST API - Gestion des Livres avec Authentification JWT et Permissions

![Django](https://img.shields.io/badge/Django-4.x-brightgreen) ![DRF](https://img.shields.io/badge/DRF-3.x-red) ![JWT](https://img.shields.io/badge/JWT-Authentication-orange) ![Python](https://img.shields.io/badge/Python-3.x-blue)

Ce projet est une API RESTful développée avec Django et Django Rest Framework (DRF), conçue pour gérer une bibliothèque en ligne. Il inclut un système d'authentification **JWT** et un contrôle d'accès basé sur les rôles et permissions.

Les utilisateurs **administrateurs** ont un accès complet à toutes les API (**GET**, **POST**, **PUT**, **DELETE**), tandis que les utilisateurs normaux peuvent uniquement accéder aux requêtes **GET** (lecture seule).

## 🚀 Fonctionnalités

- **Système d'authentification JWT** : Utilisation de tokens JWT pour sécuriser les endpoints de l'API.
- **Gestion des rôles** :
  - **Admin** : Accès complet (GET, POST, PUT, DELETE).
  - **User** : Accès limité à la lecture seule (GET).
- **Gestion des permissions** : Les utilisateurs normaux peuvent seulement lire les données tandis que les administrateurs peuvent créer, modifier, et supprimer des enregistrements.
- **Filtrage et tri** : Utilisation de Django Filter pour filtrer et trier les données.
- **Permissions au niveau des objets** : Avec **django-guardian**, les utilisateurs ne peuvent modifier que leurs propres objets (livres, commentaires, etc.).
- **Blacklist des tokens JWT** : Les tokens peuvent être mis en blacklist après leur utilisation.

## 📦 Installation

### Prérequis

- **Python 3.x**
- **Django 4.x**
- **Django Rest Framework**
- **SimpleJWT** pour l'authentification par token
- **Django Guardian** pour la gestion des permissions au niveau des objets

## Requirement 

- **asgiref==3.8.1**
- **Django==5.1.2**
- **django-filter==24.3**
- **django-guardian==2.4.0**
- **djangorestframework==3.15.2**
- **djangorestframework-simplejwt==5.3.1**
- **drf-yasg==1.21.7**
- **inflection==0.5.1**
- **packaging==24.1**
- **pillow==10.4.0**
- **PyJWT==2.9.0**
- **pytz==2024.2**
- **PyYAML==6.0.2**
- **setuptools==75.1.0**
- **sqlparse==0.5.1**
- **tzdata==2024.2**
- **uritemplate==4.1.1**
