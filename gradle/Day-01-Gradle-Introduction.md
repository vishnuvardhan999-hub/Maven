# ≡ƒôù Day 1 ΓÇö Gradle Build Tool
**Date:** 1 July 2026  
**Topic:** What is Gradle, Gradle vs Maven, Groovy DSL vs Kotlin DSL, Project Structure, Gradle Wrapper

---

## ≡ƒù║∩╕Å Mind Map

```
                         ΓöîΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ
                         Γöé       GRADLE         Γöé
                         Γöé   Build Tool         Γöé
                         ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ
                                    Γöé
       ΓöîΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ
       Γöé              Γöé             Γöé              Γöé              Γöé
 ΓöîΓöÇΓöÇΓöÇΓöÇΓöÇΓû╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ  ΓöîΓöÇΓöÇΓöÇΓöÇΓöÇΓû╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ ΓöîΓöÇΓöÇΓöÇΓöÇΓû╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ ΓöîΓöÇΓöÇΓöÇΓöÇΓû╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ ΓöîΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓû╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ
 Γöé  What is  Γöé  Γöé Gradle vs Γöé Γöé  Groovy  Γöé Γöé Project  Γöé Γöé  Gradle    Γöé
 Γöé  Gradle?  Γöé  Γöé  Maven    Γöé Γöé    vs    Γöé ΓöéStructure Γöé Γöé  Wrapper   Γöé
 ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ  ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ Γöé  Kotlin  Γöé ΓööΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ
       Γöé               Γöé       ΓööΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ      Γöé              Γöé
  Build tool      Faster,      build.gradle   src/main      gradlew.bat
  automates       flexible,    OR              src/test      no install
  your project    Groovy/      build.gradle   build/        needed
                  Kotlin DSL   .kts
```

---

## 1∩╕ÅΓâú What is a Build Tool?

> A **build tool** is software that **automates the process of building your project**.

### "Building" means:

| Step | What happens |
|------|-------------|
| ≡ƒö¿ Compile | Source code (Java) ΓåÆ Bytecode (`.class`) |
| ≡ƒôª Package | Code into JAR / WAR files |
| ≡ƒôÜ Manage Dependencies | Gets external libraries like Hibernate, Spring, etc. |
| ≡ƒº¬ Run Tests | Executes all your test cases |
| ≡ƒÜÇ Deploy | Puts the application on a server |

### Simple Analogy:
> ≡ƒÅù∩╕Å Building a house manually = carrying bricks one by one, mixing cement yourself  
> Using a **build tool** = a construction machine that does it all automatically

When you build your project, the output is packaged into a **JAR or WAR** file that:
- Bundles your code **plus all dependencies**
- Can be **run directly** without extra setup

---

## 2∩╕ÅΓâú What is Gradle?

Gradle is a **free, open-source build automation tool** that:
- Is **more flexible and faster** than Maven
- Uses a **programming language** (Groovy or Kotlin) instead of XML for configuration
- Is the **default build tool for Android** projects
- Supports many languages: **Java, Kotlin, Groovy, Scala, C++, Swift**

> Maven is for **only Java and Spring Boot**, but Gradle supports:
> Java ┬╖ Kotlin ┬╖ Groovy ┬╖ Scala ┬╖ C++ ┬╖ Swift

---

## 3∩╕ÅΓâú Maven vs Gradle ΓÇö Side by Side

```
ΓöîΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ
Γöé                    MAVEN vs GRADLE                              Γöé
Γö£ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöñ
Γöé         MAVEN            Γöé            GRADLE                   Γöé
Γö£ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöñ
Γöé pom.xml (XML config)     Γöé build.gradle (Groovy or Kotlin DSL) Γöé
Γöé Easy to understand       Γöé More programming-oriented            Γöé
Γöé Performance is slower    Γöé Performance is faster ΓÜí             Γöé
Γöé Fixed conventions        Γöé Highly customizable                  Γöé
Γöé Very common in Java      Γöé Very common in Android and           Γöé
Γöé Enterprise projects      Γöé modern projects                      Γöé
ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö┤ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ
```

### Why is Gradle Faster? (Simple Example)

> Imagine there are **1000 files** in your project, and **some of them are different** (changed).

```
MAVEN:
  You change 5 files out of 1000
  Maven re-executes ALL 1000 files  ΓåÉ wasteful!

GRADLE:
  You change 5 files out of 1000
  Gradle rebuilds ONLY those 5 changed files Γ£à ΓåÉ SMART!
```

This is called **Incremental Build** ΓÇö Gradle only rebuilds what changed.  
That's why Gradle is **faster compared to Maven**.

---

## 4∩╕ÅΓâú Build Command Differences

| Task | Maven Command | Gradle Command |
|------|--------------|----------------|
| Clean | `mvn clean` | `gradle clean` |
| Build | `mvn package` | `gradle build` |
| Run Tests | `mvn test` | `gradle test` |
| Run Spring Boot | `mvn spring-boot:run` | `gradle bootRun` |

---

## 5∩╕ÅΓâú Gradle in CMD ΓÇö Basic Commands

```bash
gradle init       # Create a new Gradle project
gradle tasks      # List all available tasks
gradle run        # Run the project
gradle build      # Build the project (compile + test + package)
gradle clean      # Delete the build/ folder
gradle test       # Run unit tests
```

> ΓÜá∩╕Å `gradle run` works only when Gradle is **installed locally**.  
> Use `gradlew.bat` to run **without installing Gradle** (explained below).

---

## 6∩╕ÅΓâú Gradle Project Folder Structure

```
my-project/
Γöé
Γö£ΓöÇΓöÇ build.gradle          ΓåÉ Main Gradle build script (YOUR config file)
Γö£ΓöÇΓöÇ settings.gradle       ΓåÉ Multi-project settings (project name, subprojects)
Γöé
Γö£ΓöÇΓöÇ gradlew               ΓåÉ Gradle wrapper script (Linux / Mac)
Γö£ΓöÇΓöÇ gradlew.bat           ΓåÉ Gradle wrapper script (Windows) Γ£à
Γöé
Γö£ΓöÇΓöÇ gradle/
Γöé   ΓööΓöÇΓöÇ wrapper/          ΓåÉ Wrapper files (keeps Gradle version info)
Γöé
Γö£ΓöÇΓöÇ src/
Γöé   Γö£ΓöÇΓöÇ main/
Γöé   Γöé   Γö£ΓöÇΓöÇ java/         ΓåÉ Your Java source code
Γöé   Γöé   ΓööΓöÇΓöÇ resources/    ΓåÉ Config files, properties, static files
Γöé   Γöé
Γöé   ΓööΓöÇΓöÇ test/
Γöé       Γö£ΓöÇΓöÇ java/         ΓåÉ Unit test code
Γöé       ΓööΓöÇΓöÇ resources/    ΓåÉ Test-related configs/resources
Γöé
ΓööΓöÇΓöÇ build/                ΓåÉ Auto-generated build output (classes, JARs)
```

### Comparison with Maven:
```
Maven                         Gradle
ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ     ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ
pom.xml               ΓåÆ       build.gradle
src/main/java         ΓåÆ       src/main/java  (same!)
src/test/java         ΓåÆ       src/test/java  (same!)
target/               ΓåÆ       build/
```

---

## 7∩╕ÅΓâú Gradle Wrapper

### What is Gradle Wrapper?

> **Gradle Wrapper** = a set of scripts + small JAR files that allow you to **run Gradle without installing Gradle manually** on your system.

### Simple Analogy:
> ≡ƒÄ« Imagine a game that comes with its own launcher.  
> You don't need to install anything ΓÇö just click the launcher and it runs.  
> **Gradle Wrapper = that launcher** for your project.

### Files in the wrapper:
```
gradlew          ΓåÉ Shell script for Linux/Mac
gradlew.bat      ΓåÉ Batch script for Windows Γ£à
gradle/
ΓööΓöÇΓöÇ wrapper/
    Γö£ΓöÇΓöÇ gradle-wrapper.jar        ΓåÉ Downloads the right Gradle version
    ΓööΓöÇΓöÇ gradle-wrapper.properties ΓåÉ Stores which Gradle version to use
```

### How to use it:

```bash
# Windows
gradlew.bat build
gradlew.bat test
gradlew.bat clean

# Linux / Mac
./gradlew build
./gradlew test
./gradlew clean
```

> Γ£à We need to make sure Gradle application is running globally to use `gradlew.bat`  
> But if not installed globally, `gradlew.bat` **downloads the correct Gradle version automatically**!

### Why wrapper is important:
```
WITHOUT wrapper:                  WITH wrapper:
  Developer A: Gradle 7.0   ΓåÆ     Everyone uses the SAME version
  Developer B: Gradle 8.0   ΓåÆ     defined in wrapper.properties Γ£à
  Developer C: Gradle 6.5   ΓåÆ     No version conflicts!
  Result: CONFLICTS! Γ¥î
```

---

## 8∩╕ÅΓâú Groovy DSL vs Kotlin DSL

This is the most important concept that makes Gradle unique!

> **DSL = Domain Specific Language** ΓÇö a mini-language designed for a specific purpose.  
> Gradle lets you write your build script in **two languages**: Groovy or Kotlin.

---

### ≡ƒƒí Groovy DSL ΓÇö `build.gradle`

**Groovy** is a dynamic scripting language that runs on the JVM (Java Virtual Machine).

Think of Groovy like:
> ≡ƒô¥ Writing build instructions in a **relaxed, flexible way** ΓÇö like a rough draft.  
> It's forgiving, short, and quick to write.

#### File name: `build.gradle`

```groovy
// build.gradle (Groovy DSL)

plugins {
    id 'java'                           // Add Java support
    id 'org.springframework.boot' version '3.1.0'
}

group = 'com.vishnu'                    // GroupId
version = '1.0-SNAPSHOT'               // Version

repositories {
    mavenCentral()                      // Download from Maven Central
}

dependencies {
    // Spring Boot Web
    implementation 'org.springframework.boot:spring-boot-starter-web:3.1.0'

    // JUnit for testing
    testImplementation 'junit:junit:4.13.2'

    // Hibernate
    implementation 'org.hibernate:hibernate-core:6.2.0.Final'
}
```

**Groovy Characteristics:**
- Uses **single quotes** `'...'` for strings (mostly)
- **No semicolons** needed
- **Optional parentheses** in some places
- More **flexible/dynamic** ΓÇö less strict
- Older style, widely used in existing projects

---

### ≡ƒö╡ Kotlin DSL ΓÇö `build.gradle.kts`

**Kotlin** is a modern, statically-typed language made by JetBrains (the makers of IntelliJ).

Think of Kotlin DSL like:
> ≡ƒôï Writing build instructions in a **strict, professional way** ΓÇö like a final typed document.  
> Your IDE catches mistakes immediately, everything is precise.

#### File name: `build.gradle.kts` (notice the `.kts` extension!)

```kotlin
// build.gradle.kts (Kotlin DSL)

plugins {
    java                                         // Add Java support
    id("org.springframework.boot") version "3.1.0"
}

group = "com.vishnu"                             // GroupId
version = "1.0-SNAPSHOT"                         // Version

repositories {
    mavenCentral()                               // Download from Maven Central
}

dependencies {
    // Spring Boot Web
    implementation("org.springframework.boot:spring-boot-starter-web:3.1.0")

    // JUnit for testing
    testImplementation("junit:junit:4.13.2")

    // Hibernate
    implementation("org.hibernate:hibernate-core:6.2.0.Final")
}
```

**Kotlin DSL Characteristics:**
- Uses **double quotes** `"..."` for strings
- **Parentheses are required** `("...")`
- **Statically typed** ΓÇö IDE gives you auto-complete and error highlighting
- **More strict** ΓÇö catches errors before you even run
- Modern style, recommended for new projects

---

### ≡ƒåÜ Groovy vs Kotlin DSL ΓÇö Full Comparison

```
ΓöîΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÉ
Γöé              Groovy DSL  vs  Kotlin DSL                             Γöé
Γö£ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö¼ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöñ
Γöé       GROOVY DSL           Γöé         KOTLIN DSL                    Γöé
Γö£ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö╝ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöñ
Γöé File: build.gradle         Γöé File: build.gradle.kts                Γöé
Γöé Language: Groovy           Γöé Language: Kotlin                      Γöé
Γöé Dynamic typing             Γöé Static typing (stricter)              Γöé
Γöé Less IDE support           Γöé Full IDE auto-complete Γ£à              Γöé
Γöé Shorter, flexible syntax   Γöé More explicit, verbose syntax         Γöé
Γöé Older projects use this    Γöé New/modern projects prefer this       Γöé
Γöé 'single quotes' for stringsΓöé "double quotes" for strings           Γöé
Γöé Optional parentheses       Γöé Parentheses required                  Γöé
Γöé Harder to catch typos      Γöé Errors caught at compile time Γ£à       Γöé
Γöé More beginner-friendly     Γöé Better for large teams                Γöé
ΓööΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓö┤ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÿ
```

### Same thing written in both ΓÇö spot the difference:

```groovy
// GROOVY DSL (build.gradle)
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web:3.1.0'
    testImplementation 'junit:junit:4.13.2'
}
```

```kotlin
// KOTLIN DSL (build.gradle.kts)
dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web:3.1.0")
    testImplementation("junit:junit:4.13.2")
}
```

**Key difference:** Groovy uses no parentheses + single quotes. Kotlin uses parentheses + double quotes. That's it!

### Which one should you use?

```
Starting a NEW project?         ΓåÆ Use Kotlin DSL (build.gradle.kts) Γ£à
Working on an EXISTING project? ΓåÆ Stick with whatever it uses
Learning Gradle for the first time? ΓåÆ Groovy DSL is simpler to start
Working in a TEAM?              ΓåÆ Kotlin DSL (better IDE support)
Android project?                ΓåÆ Kotlin DSL (Google recommends it)
```

---

## 9∩╕ÅΓâú Gradle Supports More Languages Than Maven

```
           MAVEN                        GRADLE
     ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ          ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ
          Java Γ£à                     Java Γ£à
       Spring Boot Γ£à                 Kotlin Γ£à
                                      Groovy Γ£à
                                      Scala Γ£à
                                      C++ Γ£à
                                      Swift Γ£à
                                   Spring Boot Γ£à
                                    Android Γ£à
```

---

## ≡ƒöæ Quick Reference Card

| Concept | Groovy DSL | Kotlin DSL |
|---------|-----------|------------|
| File name | `build.gradle` | `build.gradle.kts` |
| Language | Groovy | Kotlin |
| String quotes | `'single'` | `"double"` |
| Function calls | `implementation 'x'` | `implementation("x")` |
| Typing | Dynamic | Static |
| IDE support | Basic | Full auto-complete |
| Best for | Legacy/simple projects | Modern/team projects |

| Command | What it does |
|---------|-------------|
| `gradle init` | Create new project |
| `gradle build` | Compile + test + package |
| `gradle clean` | Delete build/ folder |
| `gradle test` | Run unit tests |
| `gradle tasks` | List all tasks |
| `gradlew.bat build` | Build without Gradle installed (Windows) |
| `./gradlew build` | Build without Gradle installed (Linux/Mac) |

---

*≡ƒôà Tomorrow: More Gradle concepts...*
