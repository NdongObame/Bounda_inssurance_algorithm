import datetime

tarrif_color = {0: "does not qualify",
                1: "red",
                2: "orange",
                3: "green",
                4: "blue"}

####

print("welcome into Bounda insurance system"
      "\nThis is a database entry sytem")
date = datetime.date.today().year
#
# data entry
name = input("what's the client name :")

# age
error_loop = True
while error_loop:
    try:
        year_age = int(input("year of birth :"))
        error_loop = False
    except ValueError:
        print("wrong input please try again")
        error_loop = True
age = date - year_age

# license span
error_loop = True
while error_loop:
    try:
        lyear_age = int(input("year of license acquisition :"))
        error_loop = False
    except ValueError:
        print("wrong input please try again")
        error_loop = True
licence = date - lyear_age

# accidents
error_loop = True
while error_loop:
    try:
        accidents = int(input("number of accident :"))
        error_loop = False
    except ValueError:
        print("wrong input please try again")
        error_loop = True

# seniority
error_loop = True
while error_loop:
    try:
        year_seniority = int(input("when does the client enter the society :"))
        error_loop = False
    except ValueError:
        print("wrong input please try again")
        error_loop = True
seniority = date - year_seniority


# verification process###

def correct():
    print("name :" + name + "\nage : " + str(age) + " (" + str(year_age) + ")" + "\nlicense span :"
          + str(licence) + " (" + str(lyear_age) + ")" + "\nnumber of accident :" + str(accidents) +
          "\nseniority span :" + str(seniority) + " (" + str(year_seniority) + ")")

    verification1 = input("is that correct (y or n) : ").lower()

    while verification1 != "y" and verification1 != "n":
        error1 = input("invalid input. Is that correct (y or n): ").lower()
        verification1 = error1

    return verification1


verification2 = correct()
if verification2 == "n":
    while verification2 == "n":
        correction = input(
            "which infos is incorrect"
            "\n1-name"
            "\n2-age"
            "\n3-license "
            "\n4-number of accident"
            "\n5-seniority"
            "\n6-none"
            "\nenter(1-6):")

        if correction == "1":
            name = input("what's the client name :")

            print("name :" + name + "\nage : " + str(age) + " (" + str(year_age) + ")" + "\nlicense span :"
                  + str(licence) + " (" + str(lyear_age) + ")" + "\nnumber of accident :" + str(accidents) +
                  "\nseniority span :" + str(seniority) + " (" + str(year_seniority) + ")")

            verification2 = input("is that correct (y or n) :").lower()

        elif correction == "2":
            error_loop = True
            while error_loop:
                try:
                    year_age = int(input("year of birth :"))
                    error_loop = False
                except ValueError:
                    print("wrong input please try again")
                    error_loop = True
            age = date - year_age

            print("name :" + name + "\nage : " + str(age) + " (" + str(year_age) + ")" + "\nlicense span :"
                  + str(licence) + " (" + str(lyear_age) + ")" + "\nnumber of accident :" + str(accidents) +
                  "\nseniority span :" + str(seniority) + " (" + str(year_seniority) + ")")

            verification2 = input("is that correct (y or n) :").lower()

        elif correction == "3":
            error_loop = True
            while error_loop:
                try:
                    lyear_age = int(input("year of license acquisition :"))
                    error_loop = False
                except ValueError:
                    print("wrong input please try again")
                    error_loop = True
            licence = date - lyear_age

            print("name :" + name + "\nage : " + str(age) + " (" + str(year_age) + ")" + "\nlicense span :"
                  + str(licence) + " (" + str(lyear_age) + ")" + "\nnumber of accident :" + str(accidents) +
                  "\nseniority span :" + str(seniority) + " (" + str(year_seniority) + ")")

            verification2 = input("is that correct (y or n) :").lower()

        elif correction == "4":
            error_loop = True
            while error_loop:
                try:
                    accidents = int(input("number of accident :"))
                    error_loop = False
                except ValueError:
                    print("wrong input please try again")
                    error_loop = True

            print("name :" + name + "\nage : " + str(age) + " (" + str(year_age) + ")" + "\nlicense span :"
                  + str(licence) + " (" + str(lyear_age) + ")" + "\nnumber of accident :" + str(accidents) +
                  "\nseniority span :" + str(seniority) + " (" + str(year_seniority) + ")")

            verification2 = input("is that correct (y or n) :").lower()

        elif correction == "5":
            error_loop = True
            while error_loop:
                try:
                    year_seniority = int(input("when does the client enter the society :"))
                    error_loop = False
                except ValueError:
                    print("wrong input please try again")
                    error_loop = True
            seniority = date - year_seniority

            print("name :" + name + "\nage : " + str(age) + " (" + str(year_age) + ")" + "\nlicense span :"
                  + str(licence) + " (" + str(lyear_age) + ")" + "\nnumber of accident :" + str(accidents) +
                  "\nseniority span :" + str(seniority) + " (" + str(year_seniority) + ")")

            verification2 = input("is that correct (y or n) :").lower()

        elif correction == "6":
            verification2 = "y"

        else:
            print("invalid input, try again.")


# done###

def color(color):
    # red
    if age < 26 and licence < 3:
        color = + 1 - accidents
        return color
    # orange
    elif age < 26 and licence > 2 or age > 25 and licence < 3:
        color = + 2 - accidents
        return color
    # green
    elif age > 25 and licence > 2:
        color = + 3 - accidents
        return color
    else:
        return "input error"


number = color(0)

#  check for seniority
if number > 0 and seniority >= 5:
    number += 1

#  tarrif color verdict
if number <= 0:
    print(tarrif_color[0])
elif number > 0:
    print("the client qualify for tarrif option : " + tarrif_color[number])
    data_entry = input("add in the data base :"
                       "\n(y or n): ").lower()
    while data_entry != "y" and data_entry != "n":
        data_entry = input("invalid input. add in the data base (y or n):").lower()
    if data_entry == "y":
        tcolor = tarrif_color[number]
        database_entry = [name, age, licence, accidents, seniority, tcolor, date]
        data_base = open("Database.txt", "a")
        data_base.write("\n" + str(database_entry[0:6]))
        data_base.close()
        print("Entry was added in the data base")
    else:
        print("Entry wasn't added in the data base")
