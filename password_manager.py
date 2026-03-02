import csv
master_password="JNK@1428"


def add(username,platform,password):
    
        with open("password.csv","a") as file:
            data=[{"Username":username,"Platform":platform,"Password":password}]
            keys = [ "Username", "Platform","Password"]
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writerows(data)

def view(username,platform):
    with open("password.csv")as file:
        reader=csv.DictReader(file)
        available=False
        for row in reader:
            if row["Username"]==username and row["Platform"]==platform :
                print(" Username:{} Platform:{} Password {} ".format(row["Username"],row["Platform"],row["Password"]))
                available=True
        if not available:
            print("Your account doesn't exists.")
        return available
def report():
    with open("password.csv")as file:
        reader=csv.DictReader(file)
        for index,row in enumerate(reader):
                print("{}) Username:{} Platform:{} Password {} ".format(index+1,row["Username"],row["Platform"],row["Password"]))
             
        
count=5
while True:
    check_mPassword=input("Please enter your master password:")
    if check_mPassword==master_password:
        mode=input("If you want to add a new account press[n] if you want to view an existing account press[v] if you want to change your master password press[c] if you want a report pres[r]:").lower()
        if mode=="n":
            username=input("Please input your username for the account you are going to add:")
            platform=input("Please input the platform you created the account in:")
            password=input("Please input the password you used for this account:")
            add(username,platform,password)
        elif mode == "v":
            username=input("Please input your username to see the password:")
            platform=input("Please input the platform you created this account in:")
            view(username,platform)
        elif mode == "c":
            new_password=input("Please input your new password:")
            master_password=new_password
        elif mode=="r":
            report()
        else:
            print("Incorrect input!")
    else:
        count -= 1
        print("Incorrect password.You have {} attempts.".format(count))
    if count == 0:
        print("You have finished your attempts.")
        break


