from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createFile():
    try:
        print("================== All Files =====================")
        readFileAndFolder()
        print("================= Create File name =================")
        name = input("Please tall your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as file:
                print("================= Write the data ================")
                data = input("What you want to write in this file :- ")
                file.write(data)
            print("!! File created successfully !!")
        else:
            print("This file is already exist")

    except Exception as err:
        print(f"An error occured as {err}")

def readFile():
    try:
        print("================== All Files =====================")
        readFileAndFolder()
        name = input("Please tall which file you want to read :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("================== Reading file ===================")
            with open(p, "r") as file:
                data = file.read()
                print(data)
            print("!! The file is readed successfully !!")

        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occured as {err}")


def updateFile():
    try:
        print("================== All Files =====================")
        readFileAndFolder()
        name = input("Please tall which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("===================== Updating File ===================")
            print("Press 1 for changing the name of your file :- ")
            print("Press 2 for overwrite the data of your file :- ")
            print("Press 3 for appending some content of your file :- ")

            print("---------------------------------------------------------")
            res = int(input("Please tall your response :- "))
            if res == 1:
                print("------------------- Create new File -----------------------")
                name2 = input("Please tall your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
                print("!! File name is changed successfully !!")

            elif res == 2:
                with open(p, 'w') as file:
                    print("------------------ Overwrite Data ------------------------")
                    data = input("Please tall what you want to write this is overwrite the data :- ")
                    file.write(data)
                    print("!! Data is overwrite successfully !!")

            elif choice == 3:
                with open(p, 'a') as file:
                    print("-------------------- Append Data ---------------------------")
                    data = input("Please tall what you want to append the data :- ")
                    file.write(" "+data)
                    print("!! Data is appended successfully !!")

        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occured as {err}")


def deleteFile():
    try:
        print("================== All Files =====================")
        readFileAndFolder()
        print("---------------------------------------------------")
        name = input("Which file you want to delete :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("------------------- Delete File -----------------")
            print(f"! {name} file is deleted successfully !")

        else:
            print("! No such file exist !")

    except Exception as err:
        print(f"An error occured as {err}")
        
    

while True:
    print("===================================================")
    print("                  ! File handling !                 ")
    print("----------------------------------------------------")
    print("Press 1 for Create the file :- ")
    print("Press 2 for Reading the file :- ")
    print("Press 3 for Updating the file :- ")
    print("Press 4 for Delation the file :- ")
    print("Press 1 for Exit the project :- ")

    print("-----------------------------------------------------")
    choice = int(input("Please enter your response :- "))
    if choice == 1:
        createFile()
    elif choice == 2:
        readFile()
    elif choice == 3:
        updateFile()
    elif choice == 4:
        deleteFile()
    elif choice == 5:
        print("!! Thank you for using website !!")
        break
    else:
        print("Invalid choice, try again")