import time
import timeit

# My implementation of LRU cache using hashmap and doubly linked list
class Node:

    def __init__(self, book):
        self.book = book
        self.prev = None
        self.next = None

    
class DLL:

    def __init__(self, max_len):
        self.head = None
        self.tail = None
        self.len = 0
        self.max_len = max_len


    def _remove(self, node) -> Node:
        if node.prev:
            node.prev.next = node.next
            
        # If removed node doesnt have prev, its the head and now we need new head. 
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        # If removed node doesnt have next, its the tail and now we need new tail.
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

        return node


    def _append(self, node):
        # When list is empty
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


    def hit(self, hit_node):
        if self.tail is not hit_node:
            self._remove(hit_node)
            self._append(hit_node)


    def miss(self, new_node):
        removed_node = None
        if self.len < self.max_len:
            self._append(new_node)
            self.len += 1

        else:
            removed_node = self._remove(self.head)
            self._append(new_node)
        
        return removed_node

    def print_list(self):
        curr = self.head
        while curr != None:
            print("->", curr.book.isbn, end="")
            curr = curr.next
        print("\n")
        

class Book:

    def __init__(self, isbn, stuff):
        self.isbn = isbn
        self.stuff = stuff


def get_book_info(isbn) -> Book:
    # Fake delay to simulate lookup from database
    time.sleep(0.5)
    return Book(isbn, "Got book from database")

def print_hashmap(hashmap):
    for key in hashmap:
        print(key, hashmap[key].book)

# For constant lookup. Key is isbn and value is corresponding Node object
hashmap = {}

# For constant add/remove
dll = DLL(5)

def wrapper(isbn) -> Book:

    if isbn in hashmap:
        book_node = hashmap[isbn]
        dll.hit(book_node)
        return book_node.book


    else:
        book_from_database = get_book_info(isbn)
    
        book_node = Node(book_from_database) 
        hashmap[isbn] = book_node

        removed_node = dll.miss(book_node)
        
        if removed_node != None:
            hashmap.pop(removed_node.book.isbn)

        return book_from_database

start = timeit.default_timer()

wrapper(1)
wrapper(2)
wrapper(1)
wrapper(4)
wrapper(5)
wrapper(4)
wrapper(3)
wrapper(6)
wrapper(4)

# get_book_info(1)
# get_book_info(2)
# get_book_info(1)
# get_book_info(4)
# get_book_info(5)
# get_book_info(4)
# get_book_info(3)
# get_book_info(6)
# get_book_info(4)

stop = timeit.default_timer()

print("Time: ", stop - start)

dll.print_list()

print_hashmap(hashmap)



