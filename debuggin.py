myAgenda = []

def printList():
    print() 
for item in myAgenda:
    print(item)
    print() 

while True:
    menu = input("Add or Remove?: ")
    if menu == "add":
        item = input("What's next on the Agenda?: ")
        myAgenda.append(item)
        print(item)
    elif menu == "remove":
        item = input("What do you want to remove?: ")
        if item in myAgenda:
            myAgenda.remove(item)
    else:
        print(f"{item}was not in the list")
    printList()
