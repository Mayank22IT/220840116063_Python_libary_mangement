import json
import os
from datetime import datetime
class Book:
    """Book class to represent book records"""
    def __init__(self, book_id, title, author, quantity, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.price = price
        self.active = True  # Logical deletion flag
    
    def to_dict(self):
        """Convert book object to dictionary for file storage"""
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'quantity': self.quantity,
            'price': self.price,
            'active': self.active
        }
    
    @staticmethod
    def from_dict(data):
        """Create book object from dictionary"""
        book = Book(data['book_id'], data['title'], data['author'], 
                   data['quantity'], data['price'])
        book.active = data.get('active', True)
        return book
    
    def add_book(self):
        """Add new book to library"""
        print("\n" + "-"*50)
        print("ADD BOOK")
        print("-"*50)
        
        book_id = input("Enter Book ID: ")
        
        # Check for duplicate Book ID
        for book in self.books:
            if book.book_id == book_id and book.active:
                print(f"Error: Book ID {book_id} already exists!")
                return
        
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        
        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
        except ValueError:
            print("Error: Invalid input for quantity or price!")
            return
        
        new_book = Book(book_id, title, author, quantity, price)
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' added successfully!")