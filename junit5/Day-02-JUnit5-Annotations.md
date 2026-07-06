# Day 2 - JUnit 5 Annotations
**Date:** 1 July 2026 / 2 July 2026
**Topic:** @BeforeEach, @AfterEach, @AfterAll, @TestInstance, TDD, assertArrayEquals, assertThrows, assertTimeout

---

## @BeforeEach

Before each test case, these methods need to be executed.

```java
// Example
class CalculatorTest {

    Calculator c;

    @BeforeEach
    void setUp() {
        c = new Calculator();
    }

    @Test
    void testAddition() {
        assertEquals(5, c.add(2, 3));
    }

    @Test
    void testSubtraction() {
        assertEquals(1, c.subtract(3, 2));
    }
}
```

---

## @AfterEach

For clean up (to close the resources) — runs after every test case.

```java
class CalculatorTest {

    Calculator c;

    @BeforeEach
    void setUp() {
        c = new Calculator();
        System.out.println("Before each");
    }

    @Test
    void testAddition() {
        assertEquals(5, c.add(2, 3));
        System.out.println("middle of test");
    }

    @Test
    void testSubtraction() {
        assertEquals(1, c.subtract(3, 2));
        System.out.println("middle of test");
    }

    @AfterEach
    void init() {
        System.out.println("After clean up");
    }
}
```

---

## @AfterAll

Will execute after testing all test cases, and also only once. We need to use `static`.

```java
@AfterAll
static void afterAll() {
    System.out.println("test all test cases");
}
```

> How many test cases are there, that many instances are created. To avoid that we have an annotation:
>
> `@TestInstance(TestInstance.Lifecycle.PER_METHOD)` — default
> `@TestInstance(TestInstance.Lifecycle.PER_CLASS)`

---

## @TestInstance

```java
class TestBeforeAllAfterAll {

    TestBeforeAllAfterAll() {
        System.out.println("Test obj is created before test method");
    }

    @BeforeAll
    void beforeAll() {
        System.out.println("Before all test");
    }

    @AfterAll
    void afterAll() {
        System.out.println("test all test cases");
    }

    @BeforeEach
    void setup() {
        c = new AutoShape();
        System.out.println("Before each");
    }
}
```

---

## @BeforeAll

Need to apply this annotation to only static methods, else we will get exceptions.

```java
@BeforeAll
static void beforeAll() {
    System.out.println("Before all test");
}
```

> It will get executed only once before all the test cases.

```java
// Example
class DemoTest {

    @BeforeAll
    static void beforeAll() {
        System.out.println("Before test");
    }

    @Test
    void testAdd() {
        System.out.println("Test 1");
    }

    @Test
    void test2() {
        System.out.println("Test 2");
    }
}
```

**Output:**
```
Before test
Test 1
Test 2
```

> Why static? Because before even creating the object, we are executing the `@BeforeAll`. So without creating object, and to call method, we can do it by using `static`.

---

## PER_METHOD vs PER_CLASS

> In the above example we are not using static for `@BeforeAll` and `@AfterAll` because we changed the instance of the class. Like before it was creating object (as) instances for every test case, but after changing the class by annotation `@TestInstance` now it will need to create only once.

- **PER_METHOD (default)** — one test = one object
- **PER_CLASS** — all tests share the only one object

```
PER_METHOD (default)         PER_CLASS
   object 1                    object 1
      |                           |
    test 1                      test 1
                                   |
   object 2                      test 2
      |
    test 2
```

> PER_METHOD → "one test = one object" (default and most commonly used)
> PER_CLASS  → "one class = one object" (all tests share the same object)

---

## Test Driven Development (TDD)

> First test, then code. We will be writing only a method, not actual real code, and then we will do the test.

- `maven-surefire-plugin` can be used for testing independently as a plugin.

---

## assertNotEquals

`assertNotEquals()` is the opposite of `assertEquals()`.

---

## assertTrue and assertFalse

- `assertTrue()` will check the value is `true` or `false`.
- `assertFalse()` is opposite to `assertTrue()`.

---

## assertArrayEquals

```
1) Actual and expected arrays are equal
2) Elements of an array are equal
3) Order of elements in an array
```

---

## assertThrows

```java
assertThrows(NullPointerException.class, () -> sortingArray(unsorted));
```

> If it generates `null` only then it will pass the test case. If it generates other than `null`, then it will fail the test case.

---

## assertTimeout

```java
assertTimeout(Duration.ofMillis(10), supplier);
assertTimeout(Duration.ofMillis(100), () -> sortingArray(unsorted));
```

> These are not available in JUnit 4. Instead it has:
> `@Test(timeout = 100)` — initially only we need to specify.
