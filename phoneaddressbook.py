import os


# ---------------------------------------------------------#
def Add_Details():
    entry = []
    name = input("Please Enter the Name: ")
    ph_no = input("Please Enter Phone Number: ")
    entry.append(name)  # Append name to the list entrty
    entry.append(ph_no)  # Append ph_no to the list entrty
    return entry


# ---------------------------------------------------------#
def bub_sort(dirList):
    length = len(dirList) - 1
    unsorted = True
    while unsorted:
        unsorted = False
    for element in range(0, length):
        if dirList[element] > dirList[element + 1]:
            temp = dirList[element + 1]
            dirList[element + 1] = dirList[element]
            dirList[element] = temp
    # print(dirList)
    unsorted = True


# ---------------------------------------------------------#
def Save_Data_To_File(dirlist):
    f = open("Phone_Directory.txt", "w")
    for n in dirlist:
        f.write(n[0])  # writes the name
        f.write(",")  # writes a comma
        f.write(n[1])  # writes the number
        f.write("\n")  # writes a new line
    f.close()


# ---------------------------------------------------------#
def Display():
    if os.path.isfile("Phone_Directory.txt") == 0:
        print("Sorry you Dont have any Contacts in your Phone Address Book.")
        print("Please Create it!!!!")
    elif os.stat("Phone_Directory.txt").st_size == 0:
        # Check if File Contains data or not
        print("Address Book is empty")
    else:
        f = open("Phone_Directory.txt", "r")
        text = f.read()
        print(text)
        f.close()


# ---------------------------------------------------------#


def Search():
    name = input("Enter the Name:")
    f = open("Phone_Directory.txt", "r")
    result = []
    for line in f:
        if name in line:
            found = True
            break
        else:
            found = False

    if found == True:
        print("The Name of Person Exist in Directory:")
        print(line.replace(",", ":"))
    else:
        print("The Name Does not Exist in Directory")


# ---------------------------------------------------------#
def get_choice():
    print("1)\tAdd New Phone Number to a List of Phone Book Directory:")
    print("2)\tSort Names in Ascending Order")
    print("3)\tSave all Phone Numbers to a File")
    print("4)\tPrint all Phone Book Directory on the Console")
    print("5)\tSearch Phone Number from Phone Directory")
    print("6)\tPlease Write 6 to exit from the menu:")
    ch = input("Please Enter the Choice:")
    return ch


# ---------------------------------------------------------#
# main program
if os.path.isfile("Phone_Directory.txt") == 0:
    print("Sorry you Dont have any Contacts in your Phone Address Book.")
    print("Please Create it!!!!")
    directory = []
else:
    print("Already Your Phone Book has Some Contacts")
    print(" You can See it!!!")
    directory = []
    f = open("Phone_Directory.txt", "r")
    for line in f:
        if line.endswith("\n"):
            line = line[:-1]
            directory.append(line.strip().split(","))
    f.close()
# directory = []
c = True
while c:
    ch = get_choice()
    if ch == "1":
        e = Add_Details()
        directory.append(e)

    if ch == "2":
        bub_sort(directory)
        print("Contents of Phone Book Sorted Successfully!!!!")

    if ch == "3":
        Save_Data_To_File(directory)
        print("Data Saved to Phone Book Successfully!!!")

    if ch == "4":
        Display()

    if ch == "5":
        Search()

    if ch == "6":
        print("Thanks a Lot for using Our Application")
        c = False
# ---------------------------------------------------------#
