# Library Management Program (short & corrected)

# ---------- Add Books ----------
book = {}
def addbook(bookid, name, vol=2):
    book[bookid] = [name, vol]

n = int(input("Enter number of books to add: "))
for i in range(n):
    bid = int(input("Book ID: "))
    bname = input("Book Name: ")
    addbook(bid, bname)

print("\nBooks:", book)

# ---------- Add Borrowers ----------
borrower = {}
book_borrow = []

m = int(input("\nEnter number of borrowers: "))
for i in range(m):
    bid = int(input("Borrower ID: "))
    borrower[bid] = 0
    book_borrow.append(0)

print("Borrowers:", borrower)

# ---------- Issue Book ----------
bookid = int(input("\nEnter Book ID to issue: "))
if bookid in book:
    name, qty = book[bookid]
    if qty > 0:
        borrowerid = int(input("Enter Borrower ID: "))
        if borrowerid in borrower:
            book[bookid][1] -= 1
            index = list(borrower.keys()).index(borrowerid)
            book_borrow[index] = bookid
            print(f"✅ '{name}' issued to Borrower {borrowerid}")
        else:
            print("❌ Invalid Borrower ID")
    else:
        print("❌ Book not available")
else:
    print("❌ Invalid Book ID")

# ---------- Queries ----------
total_borrowers = len(book_borrow)
borrowed_count = total_borrowers - book_borrow.count(0)
avg_books = borrowed_count / total_borrowers

print("\nAverage books borrowed per member:", avg_books)
print("-" * 50)

# find most borrowed book
freq = {}
for b in book_borrow:
    if b > 0:
        freq[b] = freq.get(b, 0) + 1

if freq:
    max_book = max(freq, key=freq.get)
    min_book = min(freq, key=freq.get)
    print("Most borrowed book:", book[max_book][0])
    print("Least borrowed book:", book[min_book][0])
else:
    print("No book issued yet.")

print("-" * 50)
print("Members with no books:", book_borrow.count(0))
print("-" * 50)
