# release-link-integrity

## Français

Vérifier les liens relatifs documentaires sur une révision figée.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m release_link_integrity examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Vérifie les cibles réelles de liens Markdown relatifs dans une arborescence figée, sans réseau ni extraction ; détecte chemins manquants et sorties de racine.

### Limites

Sous-ensemble de liens inline ; ancres, liens de référence, HTML et syntaxe imbriquée non vérifiés. Le numéro de ligne est relatif au texte sans blocs de code.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Check relative documentation links against a frozen revision.

Synthetic data; no network access or secret required.

```sh
python -m release_link_integrity examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Checks actual relative Markdown link targets in a frozen tree without network or extraction; detects missing paths and root escapes.

### Limits

Inline-link subset; anchors, reference links, HTML and nested syntax not checked. Line number is relative to text with code blocks removed.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comprobar enlaces documentales relativos en una revisión fija.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m release_link_integrity examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Comprueba destinos reales de enlaces Markdown relativos en árbol fijo sin red ni extracción; detecta rutas ausentes y salidas de raíz.

### Límites

Subconjunto de enlaces inline; sin comprobar anclas, referencias, HTML ni sintaxis anidada. Número de línea relativo a texto sin bloques de código.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks
