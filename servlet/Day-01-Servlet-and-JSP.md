# Day 1 - Servlet and JSP
**Date:** 4 July 2026
**Topic:** Client-Server Architecture, Web Server, Static vs Dynamic Response, Servlets, Servlet Lifecycle, PrintWriter, Request Dispatching, JSP

---

## Fundamentals of Client-Server Architecture

### Client

The client is a **user or system** that requests a specific resource (or) service from another entity known as the server.

### Internet

Internet is a **global communication system** that links together thousands of individual networks. It allows exchange of information between two or more computers on a network.

---

## Server

A server may be responsible to process **a single request or more than one** request at a time.

---

## Web Server

A software program (or) server computer that is equipped to offer **worldwide web access**.

---

## Static Response (no change in the output for every user)

```
Web Browser  -->  Request  -->  WebApp? / WebServer  -->  search  -->  static files
             <--  Response
             static
```

---

## Dynamic Response (change in the output for every user)

```
Web Browser  -->  Request  -->  WebApp / WebServer  -->  search  -->  static files
             <--  Response
             Dynamic
                   |
             Apache Tomcat
                   |
           Helper application (Java app)
               Contains
                              Dynamic Response:
                              1) Servlet
                              2) JSP
                              3) ASP
                              4) PHP
                              5) CGI
                              6) REST
                              7) Cold Fusion
```

---

## Servlets

```
Web Browser  -->  Request  -->  WebServer  -->  HTTP Request  -->  Servlet Container
             <--  Response                  <--  Response               |
             dynamic                                               Database
```

- **Servlet means a Java class.**
- A **Servlet** is a Java program that runs on a web server (or servlet container) and processes client requests to generate dynamic responses.

---

## Servlet Lifecycle

It contains **3 main stages**:

1. `init()` — used for servlet initialization.
2. `service()` — processes the client requests.
3. `destroy()` — destroys the servlet.

```
Tomcat start
      |
Create servlet object
      |
init()         (only once)
      |
service()      (every request)
      |
Tomcat stop
      |
destroy()      (only once)
```

> One servlet object per servlet.

---

## JSP

> JSP is just like HTML but with additional features. It can take the data from servlet.

---

## PrintWriter

Used for sending response from servlet to user (to `getWriter()`).

```java
// Example
PrintWriter writer = response.getWriter();
writer.println();
writer.close();
```

---

## doGet Method

```java
public void doGet(Request, Response) {
    String name  = request.getParameter("uname");
    String univ  = request.getParameter("univ");
    PrintWriter writes = response.getWriter();
    response.sendRedirect("//austin servletApp/success.jsp");
}
```

---

## Request Dispatching

Sending request from one servlet to another servlet is called **Request Dispatching**.

### Forward

```
client  -->  request  -->  Servlet 1  -->  (forward)  -->  Servlet 2
                           no resp              req / resp
             <--  response
```

```java
reqDispatch.forward(Request, Response);
```

### Include

```
client  -->  request  -->  Servlet 1  -->  (include)  -->  Servlet 2
                           yes req              req / resp
             <--  response
```

```java
reqDispatch.include(Request, Response);
```

```java
// Getting the dispatcher
RequestDispatcher reqDispatch = request.getRequestDispatcher("/secondServlet");
```

---

## Statement vs PreparedStatement

**Statement** is parent interface and **PreparedStatement** is a child interface.

- When we use Statement, we have a named object and we need to `createStatement()`.
- When we use PreparedStatement, we need to invoke `preparedStatement()`, and it will give correct object and we need to `executeQuery()`.

**In PreparedStatement:**
- In PreparedStatement, we need to give values hardcoded.
- We need to invoke `preparedStatement()` inside it, having query.

```java
// PreparedStatement example
pstmt = connect.prepareStatement("update studentInfo set sage=? where id=?");
pstmt.setString(1, name);
pstmt.setInt(2, id);
int rows = pstmt.executeUpdate();
if (rows == 0) {
    System.out.println("unable to update the data");
} else {
    System.out.println("data updated successfully!");
}
```

---

## stmt.executeUpdate() — For repeating queries

```java
// In PreparedStatement, we don't need to pass the query
stmt.executeQuery(query);      // for select
stmt.executeUpdate(query);     // for insert, update, delete
```
