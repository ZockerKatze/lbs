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
print("Written by Rattatwingo in 2023")
print("")


# auswahl
choice = input("Do you want to read or write a log File?\nW = Write\nR = Read\nEnter W or R: ")

# wenn choice = W,R txt machen
if choice == "W":
    print("CREATING FILE")

    # klumpat
    timestamp = datetime.datetime.now().strftime("%m%d")
    filename = "logs_" + timestamp + ".txt"

    print("FILE CREATED")

    volt = input("Write Voltage here: ")
    amph = input("Write the Ah. consumption here: ")
    vmp = input("Write the VMP here: ")
    wh = input("Write the consumption of Watts in WH here: ")
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
elif choice == "R":
    filename = input("Enter the name of the log file you want to read (including the file extension): ")

    try:
        with open(filename, "r") as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("The specified file does not exist.")
        
    input("Press enter to exit...")

# wenn nicht w,r dann INVALID
else:
    print("Invalid choice. Please enter W or R.")
