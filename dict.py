student = {"Student No.": "10-1001",
           "Name": "Juan Dela Cruz",
           "Course": "BSIT",
           "Year": 2,
           "Age": 21}


while True:

    x = input("[1] Display\n[2] Edit\n[3] Exit\nChoose a Number: ")

    if x == "1":
        print(student)
        break
    elif x == "2":
        print("Keys: ")
        for j in student:
            print(j)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(" ")


        n =5
        for i in range(n):
            id = input("Enter key to update the value : ")
            value = input("enter Value: ")
            student[id] = value
            print((student))


    elif x== "3":
        print("Thank You!")
        break

    else:
        print("Wrong Input !!")

