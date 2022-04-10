from dbhelper import DBHelper

def main():
    db = DBHelper()
    print("*********** Welcome ***********")
    while True:
        print()
        print('Press 1 to insert new user')
        print('Press 2 to display all user')
        print('Press 3 to delete user')
        print('Press 4 to update user')
        print('Press 5 to exit program')
        print()
        try:
            choice = int(input())
            if(choice==1):
                userId = int(input("Enter userId: "))
                userName = input("Enter userName: ")
                phone = input("Enter phone: ")
                db.insert_user(userId, userName, phone)
                
            elif(choice==2):
                db.fetch_all()

            elif(choice==3):
                userId = int(input("Enter userId to delete: "))
                db.delete_user(userId)

            elif(choice==4):
                userId = int(input("Enter userId: "))
                userName = input("Enter new userName: ")
                phone = input("Enter new phone: ")
                db.update_user(userId, userName, phone)

            elif(choice==5):
                break

            else:
                print("Invalid input! Try again")

        except Exception as e:
            print(e)
            print('Encountered some error! Try again')

if __name__ =="__main__":
    main()