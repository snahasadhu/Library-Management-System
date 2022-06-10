import datetime


class LibraryManagementSystem:
    """
    Purpose: keep records of books.
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(id): {"book_title": line.replace("\n", ""), "lender_name": "", "issue_date": "",
                                              "status": "Available"}})
            id = id + 1

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books ID", "\t", "Title")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("book_title"), "- [", value.get("status"), "]")

    def search_book(self):
        search_book_name = input("Enter Book Name : ")

        similar_books = []

        for book_id, book_info in self.books_dict.items():
            book_title = book_info['book_title']
            status = book_info['status']

            if search_book_name in book_title:
                similar_books.append([book_id, book_title, status])

        for sb in similar_books:
            print(sb)


    def issue_books(self):
        books_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["status"] == "Available":
                print(
                    f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['issue_date']}")
                return self.issue_books()
            elif self.books_dict[books_id]["status"] == "Available":
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['issue_date'] = current_date
                self.books_dict[books_id]['status'] = "Already Issued"
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")

    def add_books(self):
        new_books = input("Enter Books Title :")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict)) + 1): {"book_title": new_books, "lender_name": "",
                                                                         "issue_date": "", "status": "Available"}})
            print(f"The books '{new_books}' has been added successfully !!!")

    def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['issue_date'] = ''
                self.books_dict[books_id]['status'] = 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")