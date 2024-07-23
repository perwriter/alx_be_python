class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor to handle the deletion of the Book instance."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for informal display."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official string representation for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
