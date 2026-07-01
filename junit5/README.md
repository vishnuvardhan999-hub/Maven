# 🧪 JUnit 5 Testing Notes

All JUnit 5 testing notes are here.

| Day | Date | Topics | File |
|-----|------|--------|------|
| Day 1 | 01-Jul-2026 | Manual vs Unit Testing, JUnit5 Architecture, @Test, Assertions, Lifecycle, JUnit4 vs JUnit5 | [Notes](./Day-01-JUnit5-Testing.md) |

## 🖼️ Visual Images (Day 1)
| Image | Description |
|-------|-------------|
| `Day-01-MindMap.png` | Full JUnit 5 mind map |
| `Day-01-Architecture.png` | Platform + Jupiter + Vintage architecture |
| `Day-01-JUnit4-vs-JUnit5.png` | Complete 14-point comparison table |
| `Day-01-Manual-vs-Unit-Testing.png` | Code comparison side by side |
| `Day-01-Assertions-CheatSheet.png` | All 8 assertion methods with examples |
| `Day-01-Lifecycle-Annotations.png` | @BeforeAll → @BeforeEach → @Test → @AfterEach → @AfterAll flow |

## 🔑 Quick Reference
```java
// Maven dependency
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.0</version>
    <scope>test</scope>
</dependency>

// JUnit 4 → JUnit 5 annotation mapping
@Before      → @BeforeEach
@After       → @AfterEach
@BeforeClass → @BeforeAll
@AfterClass  → @AfterAll
@Ignore      → @Disabled
@RunWith     → @ExtendWith
```
