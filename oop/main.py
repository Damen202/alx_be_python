from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating thr __str__ method
    print(my_book) # Expected to use __str__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()