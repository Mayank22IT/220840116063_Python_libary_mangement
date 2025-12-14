# Library Management System – Internship Evaluation

## 📌 Problem Overview

Design and develop a **console-based Library Management System** that allows a librarian
to manage book records efficiently.

This problem statement is **language-independent** and can be implemented using:

- C
- C++
- Java
- Python

The objective is to evaluate students’ understanding of **core programming concepts**, logic building, and file handling.

---

## 🛠 Application Type

- Console-based application
- No external frameworks or libraries
- Data persistence using **file handling**

---

## 📚 Book Entity (Attributes)

Each book record must contain the following attributes:

- `bookId` – Unique identifier of the book  
- `title` – Book title  
- `author` – Author name  
- `quantity` – Number of available copies  
- `price` – Price of the book  
- `isActive` – Status flag  
  - `1` → Active  
  - `0` → Deleted (Logical deletion)

---

## ⚙️ Required Functionalities

Students must implement **only the following operations**:

---

### 1. Add Book
**Purpose:**  
Insert a new book record into the system.

**Description:**  
- Accept book details from the user  
- Book ID must be unique  
- Newly added book should be marked as active  

---

### 2. Update Book (By Book ID)
**Purpose:**  
Modify details of an existing book using its Book ID.

**Description:**  
- Ask user to enter the **Book ID**  
- Search the book using Book ID  
- Update fields such as title, author, quantity, or price  
- Only **active books** can be updated  

---

### 3. Delete Book (Logical Deletion – By Book ID)
**Purpose:**  
Delete a book logically using its Book ID.

**Description:**  
- Ask user to enter the **Book ID**  
- Search the book using Book ID  
- Mark the book as inactive using `isActive` flag  
- Book data must not be physically removed from file  

---

### 4. Display Books
**Purpose:**  
Display all available books in the library.

**Description:**  
- Display **only active books**  
- Data must be read from file  

---

### 5. Search Book (By Book ID)
**Purpose:**  
Search a book using its Book ID.

**Description:**  
- Perform a linear search  
- Search only active books  
- Display complete book details if found  

---

## 🧠 Concepts Expected to be Used

- Functions / Methods  
- Structures / Classes  
- Conditional statements  
- Looping  
- File handling  
- Logical deletion (active flag)  
- Menu-driven programming  

---
