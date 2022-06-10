from library_management_system import LibraryManagementSystem


if __name__ == "__main__":
    try:
        myLMS = LibraryManagementSystem("list_of_books.txt", "Python's")
        press_key_list = {"s": "Search Book", "d": "Display Books", "i": "Issue Book", "a": "Add Book", "r": "Return Book", "q": "Quit"}
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()

            if key_press == "s":
                print("\nCurrent Selection : Search Book\n")
                myLMS.search_book()

            elif key_press == "i":
                print("\nCurrent Selection : Issue Book\n")
                myLMS.issue_books()

            elif key_press == "a":
                print("\nCurrent Selection : Add Book\n")
                myLMS.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : Display Books\n")
                myLMS.display_books()

            elif key_press == "r":
                print("\nCurrent Selection : Return Book\n")
                myLMS.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")
