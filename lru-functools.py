import functools
import timeit


@functools.lru_cache(maxsize=5)
def get_book_info(isbn):
    # Retrive book from database using isbn
    return "book object with isbn: {0}".format(isbn)

start = timeit.default_timer()
print(get_book_info(1))
print(get_book_info(2))
print(get_book_info(1))
print(get_book_info(4))
print(get_book_info(5))
print(get_book_info(4))
print(get_book_info(3))
print(get_book_info(6))
print(get_book_info(4))


stop = timeit.default_timer()

print("Time:", stop - start)