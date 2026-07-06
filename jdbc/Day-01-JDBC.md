# Day 1 - JDBC (Java Database Connectivity)
**Date:** 3 July 2026
**Topic:** JDBC, JDBC Driver, Steps to connect, Statement, PreparedStatement, ResultSet, executeQuery, executeUpdate

---

## What is JDBC?

JDBC stands for **Java Database Connectivity**.

```
Java Application
       |
      JDBC
       |
Java Database Connectivity
       |
     DBMS
  (Database)
```

---

## JDBC Driver

JDBC Driver is a **software component** that allows a Java application to communicate with a database (also called a **specific JAR** into the project).

---

## Steps Involved in Developing a JDBC Application

1. Import the required package (also download & add database specific JAR into the project).
2. Load and register the driver.
3. Establish the connection.
4. Create the statement.
5. Execute the query.
6. Process the result.
7. Close the resources.

---

## Step 1: Import

```java
import java.sql.*;
```

> First right click the project and go to build path, then to libraries configure build path, then to import Java SQL `*`. We need to import it.

---

## Step 2: Load and Register the Driver

```java
Class.forName("com.mysql.cj.jdbc.Driver");
```

> `Class.forName()` is used to dynamically load a class at runtime. It was used to load and register the JDBC driver. It comes with the JDBC API applications. It uses non-selection statements, it was used to load and register statement. `connect.close();`

---

## Step 3: Establish the Connection

```java
Connection connect = DriverManager.getConnection(url, user, password);
```

```java
class LawnB() {
    public static void main(String[] args) {
        Connection connect = null;
        PreparedStatement pstmt = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connect = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/sage-9", "root", "password"
            );
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## Step 4: Create the Statement

```java
Statement st = connect.createStatement();
```

---

## Step 5: Execute the Query

```java
// Execute query
String sq = "select * from table";
ResultSet rs = statement.executeQuery(sq);
```

---

## Step 6: Process the Result

```java
while (rs.next()) {
    System.out.println(rs.getInt(1) + " " + rs.getString(2) + " " + rs.getString(3));
    // also we can give column names
}
```

---

## Step 7: Close the Resources

```java
rs.close();
statement.close();
connect.close();
```

---

## In JDBC: executeQuery and executeUpdate

In JDBC "selection statements" we will use `executeQuery()`, and return type is `ResultSet`.

```java
Statement st = connect.createStatement();
ResultSet rs = st.executeQuery("select * from students");
// return type is ResultSet
```

- For **non-selection statements** we will use `executeUpdate()`.

---

## Non-selection Statements

Non-selection statements are SQL statements that **do not return rows**. Instead, they are used to insert, update, or delete data from a database — they do not retrieve data.

```java
// Example: insert into student values (10, "vishnu");
```

---

## executeUpdate Example

```java
// execute query
String sq = "insert into studentInfo(id, sname, sage, sity)";
int rows = statement.executeUpdate(sq);
if (rows == 0) {
    System.out.println("unable to insert the data");
} else {
    System.out.println("data inserted successfully!");
}
```

---

## PreparedStatement

> In PreparedStatement, if we need to give values (hardcoded), we don't need to perform a delete statement, then we need to create another statement, because here we need to create a query involving the object. And if we need to create another statement invoking the query.

**PreparedStatement** is a child interface of Statement.

```java
PreparedStatement pstmt = null;
String sq = "update studentInfo set sage=? where id=?";
// the values (1, 2, 3, 4, 5) will be stored in DB()
```

**When we use Statement:**
- Statement is parent interface.
- When we use Statement we have a named object and we need to `createStatement()` and it will give us `preparedStatement()` inside it, having query.

**When we use PreparedStatement:**
- In PreparedStatement, we need to invoke `preparedStatement()`. And it will give correct object and we need to `executeQuery()`.

---

## In PreparedStatement

```java
pstmt = connect.prepareStatement("update studentInfo set sage=? where id=?");
```

> In PreparedStatement, we need to give values (hardcoded), so we use `?` as placeholder. The values (1, 2, 3, 4) will be stored in DB.

```java
// Example
public class LawnB {
    public static void main(String[] args) {
        Connection connect = null;
        PreparedStatement pstmt = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String sq = "update studentInfo set sage=?, sname=?, sage=?, sity=?";

            Scanner scan = new Scanner(System.in);
            System.out.println("Please enter your name:");
            String name = scan.nextLine();

            System.out.println("Please enter age:");
            Integer age = scan.nextInt();

            pstmt = connect.prepareStatement(sq);
            pstmt.setString(1, name);
            pstmt.setInt(2, age);

            int rows = pstmt.executeUpdate();
            if (rows == 0) {
                System.out.println("unable to update the data");
            } else {
                System.out.println("data updated successfully!");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## catch (SQLException e)

```java
catch (Exception e) {
    e.printStackTrace();
}
// finally
try {
    log
    // close the resources
}
catch (SQLException e) {
    e.printStackTrace();
}
```

---

## Selection Statement — executeQuery()

```java
// execute query
String sq = "select * from table";
ResultSet rs = statement.executeQuery(sq);
```

> In JDBC, `executeQuery()` is a selection statement, and return type is `ResultSet`.
> `ResultSet vs = st.executeQuery("select * from students");`

---

## ResultSet — Reading Data

```java
String sq = "select * from table";
ResultSet rs = statement.executeQuery(sq);

while (rs.next()) {
    System.out.println(rs.getInt(1) + " " + rs.getString(2) + " " + rs.getString(3));
}
// close the resources
rs.close();
statement.close();
```

---

## boolean status — execute() method

```java
String sq = "select * from table and non-selection statement";
boolean status = statement.execute(sq);
// it will give false for non-selection statements

if (status) {
    // insert, update, delete
    System.out.println("select operation failed");
} else {
    // if rows = statement.getUpdateCount();
    // if rows != 0
    System.out.println("operation successful!");
}
```

---

## Data Selection

```
Selection statement:
    data will be fetched
    -> select

Non-selection statement:
    data will be modified
    -> insert, update, delete, drop etc.
```
