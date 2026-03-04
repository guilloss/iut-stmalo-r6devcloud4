# R6.DevCloud.04 – TP Observabilité et pilotage Cloud

**Travaux Pratiques – Observabilité et pilotage de l'application Haddock sur k3s**

| | |
|---|---|
| **Durée** | 9 heures (3 × 3h) |
| **Formation** | BUT R&T – 3ᵉ année – Parcours DevCloud – Semestre 6 |
| **Prérequis** | SAE 5.03 terminée (Haddock déployé sur k3s) |
| **Outils** | Logiciels libres uniquement |

## Contexte

Lors de la SAE 5.03, vous avez déployé l'application **Citations du capitaine Haddock** sur un cluster k3s : 3 microservices (users, quotes, search) avec Redis, Traefik en reverse proxy, et deux namespaces (qualification, production).

Ce TP prolonge ce travail en ajoutant les dimensions de **pilotage** vues en cours : observabilité (métriques, logs, traces), alerting, gestion des ressources, et initiation au FinOps.

## Architecture cible

À la fin du TP, votre cluster contiendra en plus de l'application Haddock :

- Un namespace `monitoring` avec Prometheus + Grafana + Loki + Promtail + Tempo
- Des dashboards Grafana (métriques système et applicatives)
- La centralisation des logs de tous les pods
- Le tracing distribué via OpenTelemetry + Grafana Tempo
- Des alertes fonctionnelles (Prometheus AlertManager)
- Des ResourceQuotas et LimitRanges sur les namespaces
- Un CronJob d'extinction de la plateforme de qualification

## Structure du repository

```
.
├── README.md                    # Ce fichier
├── app/
│   ├── quotes/                  # Sources du microservice quotes
│   ├── search/                  # Sources du microservice search
│   ├── seed/                    # Sources du microservice seed
│   └── users/                   # Sources du microservice users
├── docs/
│   ├── OBSERVABILITY.md         # L5 – Synthèse + réponses Q1–Q10
│   ├── postmortem.md            # L1 – Post-mortem blameless
│   └── resilience.md            # L3 – Rapport résilience
├── k8s/
│   ├── monitoring/              # Fichiers values Helm + manifestes monitoring
│   └── pilotage/                # L2 – Quotas, LimitRanges, CronJobs, PDB, RBAC
├── grafana/
│   └── dashboards/              # L4 – Exports JSON des dashboards
└── quotes-otel/                 # L6 – Instrumentation OpenTelemetry
```

## Livrables et évaluation

| Livrable | Contenu | Points |
|----------|---------|--------|
| L1 – `docs/postmortem.md` | Post-mortem blameless de l'incident simulé (Partie 4) | /2 |
| L2 – `k8s/pilotage/` | Manifestes YAML : alertes, quotas, limitranges, CronJobs, PDB, RBAC | /3 |
| L3 – `docs/resilience.md` | Rapport des scénarios de résilience (Partie 7) | /2 |
| L4 – `grafana/dashboards/` | Export JSON des dashboards Grafana | /2 |
| L5 – `docs/OBSERVABILITY.md` | Synthèse : architecture, choix techniques, limites mono-nœud, Q1–Q10 | /3 |
| L6 – `quotes-otel/` | Dockerfile modifié, manifestes Tempo/OTel Collector, screenshots traces | /4 |
| Questions Q1–Q10 | Réponses dans `docs/OBSERVABILITY.md` | /4 |

**Total : /20**

## Ressources

- [Prometheus](https://prometheus.io/docs/)
- [Grafana](https://grafana.com/docs/grafana/latest/)
- [Loki / LogQL](https://grafana.com/docs/loki/latest/)
- [Tempo](https://grafana.com/docs/tempo/latest/)
- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)
- [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts)
