# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines
import re

def get_input():
    with open("input", encoding="utf-8") as f:
        return f.read().splitlines()

def find_ints(line):
    return [int(i) for i in re.findall(r'\d+', line)]

def get_sections(lines):
    section = 0
    pages = set()
    books = []
    for line in lines:
        if not line:
            section = 1
        elif section == 0:
            pages.add(tuple(find_ints(line)))
        elif section == 1:
            books.append(find_ints(line))
    return pages, books

def get_book_score(book, pages):
    for p1 in range(len(book) - 1):
        for p2 in range(p1 + 1, len(book)):
            if (book[p2], book[p1]) in pages:
                return 0
    return book[len(book) // 2]

def try_swap(book, pages):
    for p1 in range(len(book) - 1):
        for p2 in range(p1 + 1, len(book)):
            if (book[p2], book[p1]) in pages:
                book[p1], book[p2] = book[p2], book[p1]
                return True
    return False

def reorder_book(book, pages):
    while try_swap(book, pages):
        pass

    return book[len(book) // 2]

def solve():
    lines = get_input()
    pages, books = get_sections(lines)
    incorrect_books = []

    p1 = 0
    for b in books:
        s = get_book_score(b, pages)
        if s == 0:
            incorrect_books.append(b)
        else:
            p1 += s

    p2 = sum(reorder_book(b, pages) for b in incorrect_books)
    print(f"P1: {p1} P2: {p2}")

solve()

