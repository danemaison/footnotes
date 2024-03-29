#This script will parse an existing CSV file, which contains thousands of books, and store the information
#In our DB.

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('os.getenv("DATABASE_URL")')
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("books.csv")

    reader = csv.reader(f)

    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added book {title} by {author}")
    db.commit()


if __name__ == "__main__":
    main()
