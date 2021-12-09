#Name:Alejandra
#Date:10/15/2020
#Program:HW6_StacksAndLinkedLists
#Desc: using pythons dynamic array to show stack implementation

def main():
    contacts= [{"Name":"Julia","Phone": "630-333-4445"}, {"Name":"Allison","Phone":"847-999-2061"},{"Name":"Ophelia","Phone":"773-202-9999"}]

    print("Unsorted: ")
    print(contacts)
    print()

    print("Sorted: ")
    print(sorted(contacts, key=lambda i: i['Name']))

    contacts.append({"Name":"Elizabeth","Phone":"867-232-1111"})
    print()
    print("New Phone Added....")

    print((sorted(contacts, key=lambda i: i['Name'])))
    contacts = (sorted(contacts, key=lambda i: i['Name']))
    print()


    print("DEMONSTRATING POP FUNC")
    print(contacts.pop())
    print()

    print("DISPLAYING LIST AFTER POP FUNCTION")
    print(sorted(contacts, key=lambda i: i['Name']))
    print()

    print("POPPING ALL THE DATA")
    for i in range(len(contacts)):
        if contacts == None:
            print("Finished")
        else:
            print("Now Popping. . .", contacts.pop())





main()