import logging
import random

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class BookRentalSystem:
    def __init__(self):
        # Dummy database
        self.books = {
            '1984': {'available': True},
            'Brave New World': {'available': False},
            'Fahrenheit 451': {'available': True},
        }
        logging.info("BookRentalSystem initialized with 3 books")

    def search_book(self, title):
        """Search for a book in the database"""
        logging.info(f"User searching for the book: {title}")
        if title in self.books:
            available = self.books[title]['available']
            logging.debug(f"Book '{title}' availability: {available}")
            return available
        else:
            logging.warning(f"Book '{title}' not found in the database")
            return False

    def rent_book(self, title):
        """Rent a book if it's available"""
        logging.info(f"User attempting to rent the book: {title}")
        if title in self.books:
            if self.books[title]['available']:
                self.books[title]['available'] = False
                logging.info(f"Book '{title}' has been rented")
                return True
            else:
                logging.warning(f"Book '{title}' is already rented out")
                return False
        else:
            logging.error(f"Book '{title}' does not exist")
            return False

    def return_book(self, title):
        """Return a book"""
        logging.info(f"User attempting to return the book: {title}")
        if title in self.books:
            if not self.books[title]['available']:
                self.books[title]['available'] = True
                logging.info(f"Book '{title}' has been returned")
                return True
            else:
                logging.warning(f"Book '{title}' was not rented out")
                return False
        else:
            logging.error(f"Book '{title}' does not exist in the system")
            return False

# Simulate user interaction
if __name__ == "__main__":
    system = BookRentalSystem()

    # Search for a book
    title = "1984"
    system.search_book(title)

    # Rent a book
    system.rent_book(title)

    # Try renting it again
    system.rent_book(title)

    # Return the book
    system.return_book(title)

    # Try returning the book again
    system.return_book(title)

