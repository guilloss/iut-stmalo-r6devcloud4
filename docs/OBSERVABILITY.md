# Synthèse – Observabilité et pilotage Cloud

> **Livrable L5** – Document de synthèse
> Auteur(s) :
> Date :

## 1. Architecture d'observabilité déployée

<!-- Décrivez l'architecture de la stack d'observabilité que vous avez mise en place.
Incluez un schéma (ASCII ou image) montrant les composants et leurs interactions. -->

### Composants déployés

| Composant | Rôle | Namespace | Ressources allouées |
|-----------|------|-----------|---------------------|
| Prometheus | | monitoring | |
| Grafana | | monitoring | |
| Loki | | monitoring | |
| Promtail | | monitoring | |
| Tempo | | monitoring | |
| OTel Collector | | monitoring | |
| AlertManager | | monitoring | |

### Flux de données

<!-- Décrivez le chemin des métriques, logs et traces depuis l'application jusqu'à Grafana. -->

## 2. Choix techniques et justifications

<!-- Pourquoi ces outils ? Quelles alternatives existent ? Quels compromis avez-vous faits ? -->

## 3. Limites du mono-nœud

<!-- Quelles limitations avez-vous rencontrées ? Que feriez-vous différemment en production multi-nœuds ? -->

---

## Réponses aux questions

### Q1 – Rétention et mémoire Prometheus

> Pourquoi a-t-on limité la rétention à 24h et la mémoire de Prometheus à 512Mi ? Que feriez-vous en production multi-nœuds ?

**Réponse :**

### Q2 – Promtail en DaemonSet

> Pourquoi utilise-t-on Promtail en DaemonSet plutôt qu'un side-car dans chaque pod ? Quel avantage en mono-nœud ? Quel inconvénient en multi-nœuds ?

**Réponse :**

### Q3 – Déploiement GitOps des dashboards

> Dans une approche GitOps, comment déploieriez-vous automatiquement ce dashboard dans Grafana à chaque modification du JSON dans Git ?

**Réponse :**

### Q4 – Logs structurés et tracing

> Pourquoi les logs applicatifs doivent-ils être en JSON structuré ? Quel champ ajouteriez-vous pour le tracing distribué ?

**Réponse :**

### Q5 – Symptômes vs causes

> Expliquez la différence entre alerter sur les symptômes vs les causes. Pourquoi HaddockHighErrorRate est-elle préférable à « CPU > 90% » ?

**Réponse :**

### Q6 – Économie FinOps

> Calculez l'économie théorique en % de ressources en éteignant la qualification de 19h à 8h + week-end.

**Réponse :**

### Q7 – PDB et mono-nœud

> Que se passe-t-il avec minAvailable: 1 et un seul réplica lors d'un kubectl drain ? Pourquoi est-ce problématique en mono-nœud ?

**Réponse :**

### Q8 – Stratégie DR

> Quelle stratégie de DR (Backup & Restore, Pilot Light, Warm Standby, Active-Active) est applicable en mono-nœud ? Que faire avec un second nœud ?

**Réponse :**

### Q9 – Collecteur OTel

> Pourquoi déployer un collecteur OTel plutôt qu'envoyer les traces directement de l'application vers Tempo ?

**Réponse :**

### Q10 – Workflow d'investigation 3 piliers

> Décrivez le workflow d'investigation complet : une alerte Prometheus se déclenche (taux d'erreur élevé) → comment utilisez-vous les métriques, les traces, puis les logs pour identifier la cause racine ?

**Réponse :**
