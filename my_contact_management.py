#in this we had just one problem is the phone number if we store it in case of int
#! the start zero is not count (001) = 1
#in case of string 
#? we need the number in case of int becasue str is useless in this project 

contacts = {}


while True:
    #printing the main screen for the user
    print("contact management \n")
    print("1. add a contact")
    print("2. view contact")
    print("3. edit a contact")
    print("4. EXIT")
    choice = input("\nplease choose a number from 1-4: ")

    #add a contact
    if choice == "1":

        contact_id = input("enter the contact id: ")
        contact_name = input("please type a name: ")


        #check the mobile phone if it's a digit
        while True:
            contact_phone = input("please type a phone number: ")
            if contact_phone.isdigit():
                contacts[contact_id] = {"name" : contact_name, "phone" : contact_phone}
                break
            else:
                print("this is a worng phone number")
        

        print(f"\n\n {contact_name} was added successfully ......\n\n")

    #view contact
    elif choice == "2":
        print(contacts)

    #edit contact
    elif choice == "3":
        id_to_edit = input("please enter an ID to edit: ")
        if id_to_edit == contacts[contact_id]:

            new_name = input("enter a new name: ")
            contacts[contact_id]["name"] = new_name


            #check the mobile phone if it's a digit
            while True:

                new_phone = input("enter a new phone: ")
                if new_phone.isdigit():
                    contacts[contact_id]["phone"] = new_phone
                    break

                else:
                    print("is not a number")


            print("\nsuccess .....")
        else:
            print(f"sorry, {id_to_edit} was not found......")

    #exit
    elif choice == "4":
        print("Exiting ......")
        break

    #invalid
    else:

        print("invalid choice!")
