# Amélioration d'Images Logo

Ce projet contient des scripts Python pour convertir des images logo en haute résolution (HD, 2K, 4K) en utilisant différentes méthodes.

## Prérequis

Installez les dépendances nécessaires:

```bash
pip install -r requirements.txt
```

> **Note**: Pour la méthode avancée utilisant Real-ESRGAN, vous aurez besoin de plus de dépendances. Si vous n'avez besoin que de la méthode simple, vous pouvez installer uniquement Pillow:
> ```bash
> pip install pillow
> ```

## Scripts disponibles

### 1. Version simple (Pillow uniquement)

Utilise uniquement Pillow pour redimensionner et améliorer légèrement l'image:

```bash
python enhance_logo_simple.py
```

Cette méthode est rapide et ne nécessite que Pillow. Elle génère des versions Full HD (1920x1920), 2K (2560x2560) et 4K (3840x3840) de votre logo.

### 2. Version standard

Utilise Pillow et OpenCV avec super-résolution si disponible:

```bash
python enhance_logo.py
```

### 3. Version avancée avec Real-ESRGAN

Utilise la bibliothèque Real-ESRGAN pour une super-résolution de haute qualité basée sur l'IA:

```bash
python enhance_logo_advanced.py
```

Cette méthode télécharge automatiquement le modèle Real-ESRGAN si nécessaire et produit généralement les meilleurs résultats, mais nécessite plus de dépendances et une machine plus puissante.

## Résultats

Les images améliorées sont enregistrées dans le dossier `enhanced/` créé automatiquement. Chaque script génère des fichiers avec des noms différents pour distinguer les méthodes utilisées.

## Personnalisation

Pour utiliser ces scripts avec vos propres images:

1. Remplacez `logo ok.png` par le chemin de votre image dans chaque script.
2. Modifiez la taille cible dans les scripts si vous souhaitez une résolution différente.

## Avantages de chaque méthode

- **Pillow (simple)**: Rapide, facile à installer, bons résultats pour les logos vectoriels.
- **OpenCV**: Meilleurs résultats pour les images photographiques, plus de ressources nécessaires.
- **Real-ESRGAN**: Résultats de qualité professionnelle, excellents pour les images photographiques, mais plus lent et nécessite plus de ressources. 