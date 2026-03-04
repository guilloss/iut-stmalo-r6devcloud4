# Rapport de résilience – Mini Game Day

> **Livrable L3** – Résultats des scénarios de résilience
> Auteur(s) :
> Date :

## Scénario A – Kill d'un pod

**Action réalisée** :

<!-- Quelle commande avez-vous utilisée ? Quel pod a été supprimé ? -->

**Observations** :

- Le service est-il resté disponible pendant la suppression ?
- Quelle alerte s'est déclenchée (le cas échéant) ?
- Temps de récupération observé :

**Données dashboards** :

<!-- Captures d'écran ou description des métriques observées pendant le test. -->

**Améliorations possibles** :

---

## Scénario B – Saturation mémoire

**Action réalisée** :

<!-- Décrivez le pod stress déployé et ses paramètres. -->

**Observations** :

- Le pod stress a-t-il été accepté par les quotas ?
- Impact observé sur les autres pods :
- Alerte HaddockHighMemory déclenchée : oui / non

**Données dashboards** :

<!-- Captures d'écran ou description des métriques observées. -->

**Améliorations possibles** :

---

## Scénario C – Perte de la base de données

**Action réalisée** :

<!-- Comment avez-vous stoppé Redis ? -->

**Observations** :

- Comportement des microservices (logs dans Loki) :
- Temps avant déclenchement de la première alerte :
- Quelles alertes se sont déclenchées ?

**Données dashboards** :

<!-- Captures d'écran ou description des métriques et logs observés. -->

**Améliorations possibles** :

---

## Synthèse

| Scénario | Temps de détection | Temps de récupération | Alerte déclenchée |
|----------|-------------------|----------------------|-------------------|
| A – Kill pod | | | |
| B – Stress mémoire | | | |
| C – Perte Redis | | | |

<!-- Conclusion : quels scénarios ont été les plus impactants ? Quelles améliorations prioritaires recommandez-vous ? -->
