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
│   ├── Day-01-MindMap.png
│   ├── Day-01-Build-Lifecycle.png
│   ├── Day-01-Repositories.png
│   └── Day-02-POM-and-Lifecycle.md
│
├── 📂 gradle/         ← All Gradle notes
│   ├── Day-01-Gradle-Introduction.md
│   ├── Day-01-MindMap.png
│   ├── Day-01-Gradle-vs-Maven.png
│   ├── Day-01-Groovy-vs-Kotlin.png
│   └── Day-01-Structure-and-Wrapper.png
│
└── 📂 junit5/         ← All JUnit 5 testing notes
    ├── Day-01-JUnit5-Testing.md
    ├── Day-01-MindMap.png
    ├── Day-01-Architecture.png
    ├── Day-01-JUnit4-vs-JUnit5.png
    ├── Day-01-Manual-vs-Unit-Testing.png
    ├── Day-01-Assertions-CheatSheet.png
    └── Day-01-Lifecycle-Annotations.png
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

### 🧪 JUnit 5
| Day | Date | Topics |
|-----|------|--------|
| Day 1 | 01-Jul-2026 | Manual vs Unit Testing, Architecture (Platform/Jupiter/Vintage), @Test, Assertions, Lifecycle, JUnit 4 vs JUnit 5 |

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
