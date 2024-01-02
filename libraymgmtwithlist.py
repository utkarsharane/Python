books=[]
while True:
    print("---------My Book Library--------")
    print("1:create\n2:show books\n3:issue books\n4:return books\n5:exit")
    choice=int(input("enter your choice number"))
    if choice==1:
        bookcount=int(input("enter count for books that you want to store in db="))
        for i in range(1,bookcount+1):
            title=input(f"enter {i} book title=")
            books.append(title)
    elif(choice==2):
        print("Available Books",books)
    elif choice==3:
        issuebook=input("enter book title name that you want issue=")
        if issuebook in books:
            books.remove(issuebook)
            print("book issued sucessfully")
        else:
            print("Please check isbn number or book not available")
    elif choice==4:
        returnbook=input("enter book title name that you want return=")
        if returnbook not in books:
            books.append(returnbook)
            print("book returned sucessfully")
        else:
            print("Please check title name")

    elif choice==5:
        break
    else:
        print("enter choice between 1 to 5")
    

