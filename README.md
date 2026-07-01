# 📘 Build Tools — Daily Learning Journal

> **Author:** Vishnu Vardhan  
> **Started:** 30 June 2026  
> **Topics:** Apache Maven · Gradle · Groovy DSL · Kotlin DSL

---

## 📁 Folder Structure

```
📦 Root
├── 📂 maven/          ← All Maven notes
│   ├── Day-01-Maven-Introduction.md
│   ├── Day-01-MindMap.html
│   └── Day-02-POM-and-Lifecycle.md
│
└── 📂 gradle/         ← All Gradle notes
    ├── Day-01-Gradle-Introduction.md
    └── Day-01-MindMap.html
```

---

## 📅 Learning Index

### 📦 Maven
| Day | Date | Topics |
|-----|------|--------|
| Day 1 | 30-Jun-2026 | Introduction, Build Lifecycle, Repositories, Terminologies, Dependency vs Plugin |
| Day 2 | 01-Jul-2026 | pom.xml, Effective POM, Maven Build Lifecycle |

### ⚡ Gradle
| Day | Date | Topics |
|-----|------|--------|
| Day 1 | 01-Jul-2026 | What is Gradle, Gradle vs Maven, Groovy DSL vs Kotlin DSL, Project Structure, Gradle Wrapper |

---

## 🚀 Quick Commands

### Maven
```bash
mvn archetype:generate    # Create new project
mvn clean package         # Clean + build
mvn test                  # Run tests
mvn install               # Copy to local ~/.m2
mvn help:effective-pom    # View final merged POM
```

### Gradle
```bash
gradle init               # Create new project
gradle build              # Compile + test + package
gradle clean              # Delete build/ folder
gradle test               # Run tests
gradlew.bat build         # Run without Gradle installed (Windows)
./gradlew build           # Run without Gradle installed (Linux/Mac)
```

---

*Notes updated daily. Each day = a new file in the relevant folder.*
