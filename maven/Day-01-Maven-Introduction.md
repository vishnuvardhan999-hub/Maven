# 📗 Day 1 — Maven Introduction
**Date:** 30 June 2026  
**Topic:** Maven Basics, Build Lifecycle, Project Structure, Repositories, Terminologies

---

## 🗺️ Mind Map — Day 1

```
                              ┌──────────────────────┐
                              │  APACHE MAVEN        │
                              │  Build Automation    │
                              │  Tool (Apache)       │
                              └──────────┬───────────┘
                                         │
         ┌───────────────┬───────────────┼───────────────┬───────────────┐
         │               │               │               │               │
  ┌──────▼──────┐  ┌─────▼──────┐  ┌────▼─────┐  ┌──────▼──────┐  ┌────▼──────┐
  │   BUILD     │  │  PROJECT   │  │   POM    │  │REPOSITORIES │  │TERMINOLO- │
  │  LIFECYCLE  │  │ STRUCTURE  │  │   FILE   │  │             │  │   GIES    │
  └──────┬──────┘  └─────┬──────┘  └────┬─────┘  └──────┬──────┘  └────┬──────┘
         │               │               │               │               │
  Source→Compile    src/main/java   GroupId         Local Repo      Archetype
  Bytecode→Test     src/test/java   ArtifactId      Central Repo    GroupID
  Package→JAR/WAR   pom.xml         Version         Remote Repo     ArtifactID
                                    Packaging                       Version
                                    Dependencies                    Packaging
                                    Plugins
```

---

## 1️⃣ What is Maven?

Maven is a **free and open-source build automation tool** developed by the **Apache Software Foundation**.

It simplifies the entire build process — from compiling code to deploying applications.

### 🔄 Build Lifecycle Flow

```
┌────────────┐     ┌───────────┐     ┌───────────┐     ┌──────────┐     ┌──────────────┐
│   Source   │────▶│  Compile  │────▶│   Test    │────▶│ Package  │────▶│  JAR / WAR   │
│    Code    │     │ Bytecode  │     │  (JUnit)  │     │          │     │    Build     │
│  (.java)   │     │  (.class) │     │           │     │          │     │              │
└────────────┘     └───────────┘     └───────────┘     └──────────┘     └──────────────┘
```

---

## 2️⃣ What Maven Can Do

| # | Capability | Description |
|---|-----------|-------------|
| 1 | 📁 Project Structure | Creates the standard project folder structure automatically |
| 2 | 📦 Dependency Management | Downloads and manages required dependencies/libraries automatically |
| 3 | 🧪 Unit Testing | Executes unit test cases using testing frameworks like JUnit |
| 4 | ⚙️ Compile | Compiles the project's source code |
| 5 | 🚀 Package | Packages the project into deployable formats such as JAR or WAR |

### 💡 Example
Without Maven, you would manually:
- Download `junit-5.jar`, `spring-core.jar`, `hibernate.jar` etc.
- Add them to classpath
- Write scripts to compile and test

**With Maven**, just declare in `pom.xml`:
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
</dependency>
```
Maven handles the rest automatically! ✅

---

## 3️⃣ Creating a Maven Project

### Command
```bash
mvn archetype:generate
```
This command **creates a Maven project automatically**.

### Parameters you define:

| Parameter | Example Value | Description |
|-----------|--------------|-------------|
| `-DgroupId` | `com.telusko` | Organization/company name (domain name reversed) |
| `-DartifactId` | `telusko-app` | Project/module name |
| `-DarchetypeArtifactId` | `maven-archetype-quickstart` | Template type |
| `-DarchetypeVersion` | `1.0` | Version of the archetype |
| `-DinteractiveMode` | `false` | Run without prompts |

### Full Command Example
```bash
mvn archetype:generate \
  -DgroupId=com.telusko \
  -DartifactId=telusko-app \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DarchetypeVersion=1.0 \
  -DinteractiveMode=false
```

### For a Web Application (WAR)
```bash
mvn archetype:generate \
  -DgroupId=com.telusko \
  -DartifactId=telusko-webapp \
  -DarchetypeArtifactId=maven-archetype-webapp \
  -DinteractiveMode=false
```

---

## 4️⃣ Maven Project Structure

After running `mvn archetype:generate`, Maven creates this folder structure:

```
vishnu-app/
├── .mvn/
│   └── maven-config
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/
│   │           └── vishnu/
│   │               └── App.java          ← Your main application code
│   └── test/
│       └── java/
│           └── com/
│               └── vishnu/
│                   └── AppTest.java      ← Your unit tests
└── pom.xml                               ← Maven configuration file (heart of Maven)
```

### 📌 Key Points
- `src/main/java` → Production source code
- `src/test/java` → Test source code
- `pom.xml` → **Project Object Model** — the Maven configuration file

---

## 5️⃣ Maven Terminologies

### 1) Archetype
> A **template** that defines the structure of a Maven project.

| Archetype | Purpose |
|-----------|---------|
| `maven-archetype-quickstart` | Java standalone application |
| `maven-archetype-webapp` | Java web application |

```bash
# Example: Create a standalone Java app
mvn archetype:generate -DarchetypeArtifactId=maven-archetype-quickstart

# Example: Create a Java web app
mvn archetype:generate -DarchetypeArtifactId=maven-archetype-webapp
```

---

### 2) GroupId
> Represents the **organization or company name** (written as a reversed domain name).

```xml
<groupId>com.telusko</groupId>   <!-- company: telusko.com -->
<groupId>com.ibm</groupId>       <!-- company: ibm.com -->
<groupId>com.telusko</groupId>   <!-- company: telusko.com -->
```

**Real-world examples:**
- `com.google` → Google
- `org.springframework` → Spring Framework
- `org.apache.maven` → Apache Maven

---

### 3) ArtifactId
> Represents the **name of the project or module**.

```xml
<artifactId>vishnu-app</artifactId>
<artifactId>telusko-app</artifactId>
<artifactId>spring-core</artifactId>
```

---

### 4) Version
> Specifies the **version of the project**.

```xml
<version>0.0.1-SNAPSHOT</version>   <!-- Under development -->
<version>1.0-RELEASE</version>      <!-- Final version delivered to client -->
<version>2.3.5</version>            <!-- Stable release -->
```

| Version Type | Meaning |
|-------------|---------|
| `SNAPSHOT` | Under active development — changes frequently |
| `RELEASE` | Final stable version — delivered to the client |

**Example:**
```xml
<!-- In pom.xml -->
<groupId>com.vishnu</groupId>
<artifactId>vishnu-app</artifactId>
<version>1.0-RELEASE</version>
```

---

### 5) Packaging Type
> Defines the **packaging format** of the project.

```xml
<packaging>jar</packaging>   <!-- Default — Java application -->
<packaging>war</packaging>   <!-- Web application -->
<packaging>pom</packaging>   <!-- Parent/multi-module project -->
```

> ⚠️ **Default packaging is `jar`** if not specified.

| Type | Use Case |
|------|----------|
| `jar` | Standalone Java application |
| `war` | Web application deployed on a server (Tomcat, etc.) |

---

### 6) Maven Dependencies
> Libraries or external modules required for project development.

```xml
<dependencies>
    <!-- Spring Boot Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <version>3.1.0</version>
    </dependency>

    <!-- Hibernate ORM -->
    <dependency>
        <groupId>org.hibernate</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>6.2.0.Final</version>
    </dependency>

    <!-- JUnit Testing -->
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13.2</version>
        <scope>test</scope>
    </dependency>

    <!-- Apache Kafka -->
    <dependency>
        <groupId>org.apache.kafka</groupId>
        <artifactId>kafka-clients</artifactId>
        <version>3.4.0</version>
    </dependency>

    <!-- Redis -->
    <dependency>
        <groupId>redis.clients</groupId>
        <artifactId>jedis</artifactId>
        <version>4.3.1</version>
    </dependency>
</dependencies>
```

**Popular dependencies:** Spring, Hibernate, JUnit, Kafka, Redis

---

### 7) Maven Goals
> Commands used to **perform specific steps in the Maven build lifecycle**.

```bash
mvn clean      # Delete the target/ folder (compiled output)
mvn compile    # Compile source code → .class files
mvn test       # Compile + run all test cases
mvn package    # Compile + test + create JAR/WAR file
mvn install    # Package + copy to local repository (~/.m2)
mvn deploy     # Install + upload to remote repository
```

### 🔄 Build Lifecycle Visualization

```
clean → validate → compile → test → package → verify → install → deploy
  │                   │         │       │          │        │        │
Delete            .java→     JUnit   JAR/WAR    Checks   ~/.m2   Remote
target/           .class    Tests    file     quality    repo     repo
```

---

### 8) Maven Repositories
> **Storage locations** for Maven dependencies (artifacts/libraries).

```
                    ┌─────────────────────┐
                    │    Maven App        │
                    │    (pom.xml)        │
                    └──────────┬──────────┘
                               │ needs dependency
                               ▼
                    ┌─────────────────────┐
                    │   Local Repository  │
                    │   (~/.m2/repository)│
                    └──────────┬──────────┘
                    Found? ◄───┤───► Not Found?
                       │       │           │
                  Use it ✅     │    ┌──────▼──────────┐
                               │    │ Maven Central   │
                               │    │ Repository      │
                               │    │ (repo1.maven.org)│
                               │    └──────┬──────────┘
                               │           │ download & cache
                               │           ▼
                               │    ┌─────────────────┐
                               │    │  Local Repo     │
                               │    │  (now cached)   │
                               │    └─────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  Remote Repository  │
                    │ (Company/Private)   │
                    └─────────────────────┘
```

---

## 6️⃣ Types of Maven Repositories (Detailed)

### 1) Local Repository (on your machine)

- Located at: `~/.m2/repository` folder on your computer
- Maven **stores downloaded dependencies** here so it doesn't re-download them every time
- If a dependency is already in local repo, Maven uses it **directly** (no internet needed)

```
C:\Users\vishnu\.m2\repository\
├── org\springframework\
├── junit\junit\4.13.2\
├── org\hibernate\
└── ...
```

**Example:** First time you add Spring Boot dependency → Maven downloads it from Central. Second time → uses from `~/.m2` directly ⚡

---

### 2) Central Repository (Official Online Repo)

- Maven's **official public repository** hosted online at [https://repo1.maven.org/maven2](https://repo1.maven.org/maven2)
- Contains **millions of open-source libraries**
- If something is **not in your local repo**, Maven looks here next
- No configuration needed — works out of the box

---

### 3) Remote Repository (Company or Third-Party Server)

- Additional repositories defined in `pom.xml` or `settings.xml`
- Often used by **companies or private teams** to host internal JARs
- Maven checks these **before or after Central**, depending on configuration

```xml
<!-- Adding a remote repository in pom.xml -->
<repositories>
    <repository>
        <id>company-repo</id>
        <url>https://repo.mycompany.com/maven2</url>
    </repository>
</repositories>
```

**Use case:** Your company built an internal library `payment-sdk-2.0.jar` — it's stored in the company's remote repo, not on Maven Central.

---

## 7️⃣ Dependency vs Plugin

| Feature | Dependency | Plugin |
|---------|-----------|--------|
| **Purpose** | Application code use | Build/lifecycle tasks |
| **Import in code?** | ✅ Yes | ✅ Yes (Maven uses it) |
| **Function** | Adds new functionalities to app | Performs build process actions |
| **POM Section** | `<dependencies>` | `<build><plugins>` |

### Dependency Example
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-core</artifactId>
        <version>6.0.9</version>
    </dependency>
</dependencies>
```

### Plugin Example
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>17</source>
                <target>17</target>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---

## 8️⃣ Key Maven Commands

```bash
# Clean and repackage
mvn clean package

# Generate a web app (if you need to generate a Maven web app)
mvn archetype:generate -DarchetypeArtifactId=maven-archetype-webapp

# mvn test = mvn compile + test execution
mvn test

# mvn package = compile + execute test cases + generate JAR/WAR file
mvn package
```

### Repository Flow (First-time vs Subsequent)

```
FIRST TIME:
  Maven App (pom.xml)
       │
       ▼ dependency not in local repo
  Maven Central Repo
       │
       ▼ downloads and stores
  Local Repo (~/.m2)

NEXT TIME:
  Maven App (pom.xml)
       │
       ▼ dependency already exists
  Local Repo (~/.m2) ← directly comes from here ⚡
```

---

## 📝 Complete pom.xml Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <!-- Project Coordinates -->
    <groupId>com.vishnu</groupId>          <!-- Organization name -->
    <artifactId>vishnu-app</artifactId>    <!-- Project name -->
    <version>1.0-SNAPSHOT</version>        <!-- Version -->
    <packaging>jar</packaging>             <!-- Output format -->

    <!-- Dependencies Section -->
    <dependencies>

        <!-- JUnit for testing -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>

        <!-- Spring Boot Starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
            <version>3.1.0</version>
        </dependency>

    </dependencies>

    <!-- Plugins Section -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

---

## 🔑 Quick Reference Card

| Concept | Definition | Example |
|---------|-----------|---------|
| **Maven** | Free open-source build automation tool by Apache | `mvn package` |
| **Archetype** | Template that defines project structure | `maven-archetype-quickstart` |
| **GroupId** | Organization/company name (reversed domain) | `com.telusko` |
| **ArtifactId** | Project/module name | `vishnu-app` |
| **Version** | Project version | `1.0-SNAPSHOT` |
| **SNAPSHOT** | Under development | `0.0.1-SNAPSHOT` |
| **RELEASE** | Final version for client | `1.0-RELEASE` |
| **Packaging** | Output format (jar/war) | `<packaging>jar</packaging>` |
| **Dependency** | External library needed by app | Spring, Hibernate, JUnit |
| **Plugin** | Tool that performs build tasks | `maven-compiler-plugin` |
| **Local Repo** | `~/.m2/repository` on your machine | Cached dependencies |
| **Central Repo** | Official Maven online repository | `repo1.maven.org` |
| **Remote Repo** | Company/private repository | Internal JARs |
| **Goal** | Specific Maven task | `clean`, `compile`, `test`, `package` |

---

*📅 Next session: Continue with more Maven concepts...*
