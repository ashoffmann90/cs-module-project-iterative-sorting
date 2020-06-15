class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f'{self.title}'


def insertion_sort_by_book_title(arr_of_books):
    # iterate through entire array
    # can skip first element since there's nothing to compare it to
    # do we want to iterate over books themselves, or indices
    # we do need to have access to the book before the current book
    # we need access to each index in order to facilitate this
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        # book_index will start at i
        # but we'll update it as we swap
        book_index = i

        # compare curr_book with the prev book
        # what do we compare by?
        # swap so long as the current book > previous book
        while book_index > 0 and curr_book.title < arr_of_books[book_index - 1].title:
            # swap them
            arr_of_books[book_index], arr_of_books[book_index -
                                                   1] = arr_of_books[book_index - 1], arr_of_books[book_index]
            # we need to keep track of our current book's changing index
            book_index -= 1

        return arr_of_books


arr_of_books = [
    Book('Harry Potter', 'F*** That B****', "Children's Fantasy"),
    Book('Game of Thonres', "Martin", "Adult Fantasy"),
    Book('Show Your Work', 'Austin Kleon', 'Self Help'),
    Book('LotR', 'JRR Tolkien', 'High Fantasy'),
    Book('Rust of Programming', 'Steve Klabnik', 'Programming'),
    Book('Way of Kings', 'Brandon Something', 'High Fantasy')
]

insertion_sort_by_book_title(arr_of_books)
for book in arr_of_books:
    print(book)
