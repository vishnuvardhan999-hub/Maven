# 📘 Maven Notes — Daily Learning Journal

> **Author:** Vishnu Vardhan  
> **Started:** 30 June 2026  
> **Topic:** Apache Maven — Build Automation Tool

---

## 📅 Daily Notes Index

| Date | Topic | File |
|------|-------|------|
| 30-Jun-2026 | Maven Introduction, Lifecycle, Repositories, Terminologies | [Day 1 Notes](./Day-01-Maven-Introduction.md) |

---

## 🗺️ Mind Map Overview

```
                          ┌─────────────┐
                          │    MAVEN    │
                          └──────┬──────┘
           ┌───────────┬─────────┼──────────┬───────────┐
           │           │         │          │           │
    ┌──────▼────┐ ┌────▼────┐ ┌──▼───┐ ┌───▼────┐ ┌────▼──────┐
    │  Build    │ │ Project │ │ Repo │ │  POM   │ │  Goals /  │
    │ Lifecycle │ │Structure│ │Types │ │  File  │ │  Plugins  │
    └──────┬────┘ └────┬────┘ └──┬───┘ └───┬────┘ └────┬──────┘
           │           │         │          │           │
     compile        src/main   Local      GroupId    clean
     test           src/test   Central    ArtifactId compile
     package        pom.xml    Remote     Version    test
     deploy                               Packaging  package
                                                     deploy
```

---

## 🚀 Quick Commands Reference

```bash
mvn archetype:generate          # Create new Maven project
mvn compile                     # Compile source code
mvn test                        # Compile + run tests
mvn package                     # Compile + test + create JAR/WAR
mvn clean package               # Clean then package
mvn install                     # Install to local repo
mvn deploy                      # Deploy to remote repo
```

---

*Notes are updated daily. Each day's learning is in a separate file.*
