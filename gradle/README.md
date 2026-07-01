# ⚡ Gradle Notes

All Gradle-related daily notes are here.

| Day | Date | Topics | File |
|-----|------|--------|------|
| Day 1 | 01-Jul-2026 | What is Gradle, Gradle vs Maven, Groovy DSL vs Kotlin DSL, Project Structure, Gradle Wrapper | [Day-01](./Day-01-Gradle-Introduction.md) · [MindMap](./Day-01-MindMap.html) |

## ⚡ Quick Commands
```bash
gradle init           # Create new project
gradle build          # Compile + test + package
gradle clean          # Delete build/ folder
gradle test           # Run unit tests
gradle tasks          # List all available tasks
gradle bootRun        # Run Spring Boot app

# Without Gradle installed (use wrapper)
gradlew.bat build     # Windows
./gradlew build       # Linux / Mac
```

## 🔑 Groovy vs Kotlin DSL at a glance
| | Groovy DSL | Kotlin DSL |
|-|-----------|------------|
| File | `build.gradle` | `build.gradle.kts` |
| Strings | `'single'` | `"double"` |
| Functions | `implementation 'x'` | `implementation("x")` |
| Typing | Dynamic | Static |
| Best for | Legacy projects | Modern / team projects |
