from datetime import datetime
import time
import math, random, uuid

print("=================================")
print("Welcome to Multi-utility Toolkit ")
print("=================================")

#-------------------------DATE & TIME--------------------------------------
class Date_time:

    # Method for Current Date and time
    def Current_DT(self): #Current_DT(date and time)
        current = datetime.now()
        print("Current date and time:", current)

    # Method for finding difference of two date/time
    def Diff_date(self):
        ask_d1 = input("Enter the first date(YYYY-MM-DD): ")
        ask_d2 = input("Enter the second date(YYYY-MM-DD): ")
        date1 = datetime.strptime(ask_d1, "%Y-%m-%d")
        date2 = datetime.strptime(ask_d2, "%Y-%m-%d")
        delta = abs(date2 - date1) # abs used for convert negative value to positive value
        print("Difference:", delta)
        print("Days:", delta.days)

    def Format_Date(self):
        d = input("Enter a date (YYYY-MM-DD): ") # date is in string
        date_obj = datetime.strptime(d, "%Y-%m-%d") #convert string to date obj
        print("Formatted Date: ", date_obj.strftime("%A, %d %B %Y")) # convert date obj to string

    def Diff_time(self):
        ask_t1 = input("Enter the first time(HH:MM:SS): ")
        ask_t2 = input("Enter the second time(HH:MM:SS): ")
        date1 = datetime.strptime(ask_t1, "%H:%M:%S")
        date2 = datetime.strptime(ask_t2, "%H:%M:%S")
        diff = abs((date2 - date1)) # abs used for convert negative value to positive value
        print("Difference:", diff)
        print("Seconds:", diff.seconds)

    # Method for stopwatch
    def stopwatch(self):
        input("Press Enter to start stopwatch...")
        start_time = time.time()
        input("Press Enter to stop stopwatch...")
        end_time = time.time()
        Duration_time = end_time - start_time
        print("Duration time: %.2f seconds" % Duration_time)

    # Method for countdown
    def countdown(self):
        sec = int(input("Enter countdown time in seconds: "))
        for i in range(sec, 0, -1):
            print(i, end="\r")
            time.sleep(1)
        print("Time's up!")

#------------------------------------------MATHS-------------------------------------
class Maths:

    # method for finding factorial of any number
    def fact(self, num):
        if num <= 1:
            return 1
        else:
            return num * self.fact(num - 1)

    # method for calculating compound interest
    def interest(self):
        p = int(input("Enter Principal amount:")) # Principal amount
        rate = float(input("Enter Rate of Interest:")) # Rate of interest
        t = float(input("Enter time(in years): ")) # time
        n = 4 # compounded quarterly
        r = rate / 100
        a = p * (1 + r/n) ** (n*t) # formula
        CI = a - p
        print(f"Compound Interest: ₹{a:.2f}")

    # Method for trigonometric function
    def Trigonometry(self):
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle)
        print(f"sin({angle}) = {math.sin(rad):.2f}")
        print(f"cos({angle}) = {math.cos(rad):.2f}")
        print(f"tan({angle}) = {math.tan(rad):.2f}")

    # Method for calculate area shape given by user
    def Area_Shapes(self):
        print("1. Circle  2. Rectangle  3. Triangle")
        choice = int(input("Enter shape: "))
        match choice:
            case 1:
                r = float(input("Enter radius: "))
                print(f"Area of a Circle: {math.pi * r * r:.2f}")
            case 2:
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                print(f"Area of a Rectangle: {l * b:.2f}")
            case 3:
                b = float(input("Enter base: "))
                h = float(input("Enter height: "))
                print(f"Area of a Triangle: {0.5 * b * h:.2f}")
            case _:
                print("Invalid choice.Input between 1 to 3...")

#------------------------------RANDOM-DATA---------------------------------------------
class Random:

    # Method for generating random number
    def Random_Number(self):
        low = int(input("Enter lower limit: "))
        high = int(input("Enter upper limit: "))
        print("Random Number:", random.randint(low, high))

    # Method for generating random list
    def Random_List(self):
        items = int(input("How many random numbers in list? "))
        lst = [random.randint(1, 100) for _ in range(items)]
        print("Random List:", lst)

    # Method for generate random password
    def Random_Password(self):
        length = int(input("Enter password length: "))
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        passw = "".join(random.choice(chars) for _ in range(length))
        print("Random Password:", passw)

    # Method for generating random OTP
    def Random_OTP(self):
        otp = "".join(str(random.randint(0, 9)) for _ in range(6)) # generate OTP
        print("Your OTP:", otp)

# -------------------- UUID --------------------
class UUID:
    # Method for Generate UUID
    def Generate_UUID(self): # generate UUID
        print("Generated UUID:", uuid.uuid4())

# -------------------- FILE OPERATIONS --------------------
class File:
    # Method for creating a file
    def create_File(self):
        name = input("Enter filename: ")
        try:
            with open(name, "x") as f:
                print(f"File '{name}' created successfully.")
        except FileExistsError:
            print("File already exists.")

    # Method for writing something in existing file
    def write_File(self):
        name = input("Enter filename: ")
        data = input("Enter text to write: ")
        with open(name, "w") as f:
            f.write(data)
        print("Data written successfully.")

    # Method for reading file
    def read_File(self):
        name = input("Enter file name: ")
        try:
            with open(name, "r") as f:
                print("File content:\n", f.read())
        except FileNotFoundError:
            print("File not found.")

    # Method for appending data in file
    def append_File(self):
        name = input("Enter filename: ")
        data = input("Enter text to append: ") # File ma data append karavva mate
        with open(name, "a") as f:
            f.write("\n" + data)
        print("Data appended successfully.")

# -------------------- MODULE EXPLORER --------------------
class Module_Explore:
    def Explore(self):
        mod = input("Enter module name: ")
        try:
            module = __import__(mod)
            print(f"\nAvailable attributes in module '{mod}':\n") # show all the attributes of a module
            attributes = dir(module)
            for index, attr in enumerate(attributes, start=1): # give both index and attributes
                print(f"{index}. {attr}")
            print("\nTotal attributes found:", len(attributes))
        except ModuleNotFoundError:
            print(f"Error: The module '{mod}' was not found.")
        except Exception as e:
            print("An error occurred:", e)

# -------------------- MAIN MENU --------------------
while True:
    print('''
    Choose an Option:
    1. Datetime and Time Operation
    2. Mathematical Operation
    3. Random Data Generation
    4. Generate Unique Identifiers(UUID)
    5. File Operations (Custom Modules)
    6. Explore Module Attributes (dir())
    7. Exit
    ''')

    select = int(input("Enter Your Choice(1-7): "))

    match select:
        case 1:
            obj = Date_time()
            while True:
                print('''
                Datetime and Time Operation:
                1. Display Current Date and Time
                2. Calculate Difference Between two Dates/Times
                3. Format Date into Custom Format
                4. Stopwatch
                5. Countdown Timer
                6. Back to main menu
                ''')
                ch = int(input("Enter Your Choice: "))
                match ch:
                    case 1:
                        obj.Current_DT()
                    case 2:
                        print("1. Difference between two dates\n2. Difference between two times")
                        ch2 = int(input("Enter your choice: "))
                        if ch2 == 1:
                            obj.Diff_date()
                        elif ch2 == 2:
                            obj.Diff_time()
                    case 3:
                        obj.Format_Date()
                    case 4:
                        obj.stopwatch()
                    case 5:
                        obj.countdown()
                    case 6:
                        break

        case 2:
            obj = Maths()
            while True:
                print('''
                Mathematical Operation:
                1. Calculate Factorial
                2. Solve Compound Interest
                3. Trigonometric Calculations
                4. Area of Geometric Shapes
                5. Back to Main Menu
                ''')
                ch = int(input("Enter Your Choice: "))
                match ch:
                    case 1:
                        num = int(input("Enter number: "))
                        print("Factorial:", obj.fact(num))
                    case 2:
                        obj.interest()
                    case 3:
                        obj.Trigonometry()
                    case 4:
                        obj.Area_Shapes()
                    case 5:
                        break

        case 3:
            obj = Random()
            while True:
                print('''
                Random Data Generation:
                1. Generate Random Number
                2. Generate Random List
                3. Create Random Password
                4. Generate Random OTP
                5. Back to Main Menu
                ''')
                ch = int(input("Enter Your Choice: "))
                match ch:
                    case 1:
                        obj.Random_Number()
                    case 2:
                        obj.Random_List()
                    case 3:
                        obj.Random_Password()
                    case 4:
                        obj.Random_OTP()
                    case 5:
                        break

        case 4:
            obj = UUID()
            obj.Generate_UUID()

        case 5:
            obj = File()
            while True:
                print('''
                File Operation:
                1. Create a New File
                2. Write to a File
                3. Read From a File
                4. Append To a File
                5. Back to Main Menu
                ''')
                ch = int(input("Enter Your Choice: "))
                match ch:
                    case 1:
                        obj.create_File()
                    case 2:
                        obj.write_File()
                    case 3:
                        obj.read_File()
                    case 4:
                        obj.append_File()
                    case 5:
                        break

        case 6:
            obj = Module_Explore()
            obj.Explore()

        case 7:
            print("Exiting... Goodbye!")
            break

        case _:
            print("Invalid choice. Please enter a number between 1 and 7.")

