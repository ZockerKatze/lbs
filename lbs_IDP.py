# import datetime module
import datetime

# begrüßung (LOG.BOOK.SYSTEM)
print("L        BBBB        SSS ")
print("L        B   B      S     ")
print("L        BBBB        SSS ")
print("L     .. B   B  ..      S ")
print("LLLL  .. BBBB   ..  SSSS ")
print("")

print("Welcome to the L.B.S System ©")
print("Language = ENG")
print("")
print("Written by Rattatwingo")
print("")


# auswahl
while True:
    try:
        choice = input("Do you want to read or write a log File?\nW = Write\nR = Read\nEnter W or R: ")
        if choice.lower() not in ("w", "r"):
            raise ValueError("Invalid choice. Please enter W or R.")
        break
    except ValueError as e:
        print(str(e))
        print()

# wenn choice = W,R txt machen
if choice.lower() == "w":
    print("CREATING FILE")

    while True:
        try:
            # klumpat
            timestamp = datetime.datetime.now().strftime("%m%d")
            filename = "logs_" + timestamp + ".txt"

            with open(filename, "x") as f:
                break
        except FileExistsError:
            print(f"The file {filename} already exists. Please choose another name or delete the existing file.")
            print()

    print("FILE CREATED")

    while True:
        try:
            volt = float(input("Write Voltage here: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for voltage.")
            print()

    while True:
        try:
            amph = float(input("Write the Ah. consumption here: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for Ah. consumption.")
            print()

    while True:
        try:
            vmp = float(input("Write the VMP here: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for VMP.")
            print()

    while True:
        try:
            wh = float(input("Write the consumption of Watts in WH here: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for consumption of Watts in WH.")
            print()

    date = input("Now write the Date of entry:  ")

    with open(filename, "w") as f:
        f.write("LOGS:\n")
        f.write("VOLTAGE: {}\n".format(volt))
        f.write("Amp/h: {}\n".format(amph))
        f.write("VMP: {}\n".format(vmp))
        f.write("WH: {}\n".format(wh))
        f.write("DATE:  {}\n".format(date))

    print("Data written to file")

# wenn choice r read
elif choice.lower() == "r":
    while True:
        try:
            filename = input("Enter the name of the log file you want to read (including the file extension): ")
            with open(filename, "r") as f:
                contents = f.read()
                print(contents)
            break
        except FileNotFoundError:
            print("The specified file does not exist.")
            print()
        except PermissionError:
            print("You do not have permission to read this file.")
            print()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print()
        
    input("Press enter to exit...")
