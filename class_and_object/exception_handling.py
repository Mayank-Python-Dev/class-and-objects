def try_except(x,y):

    try:
        print(x/y)

    except Exception as e :
        print("hey user you can't divide a number", e)

try_except(10,0)

def try_except1(x,y):

    try:
        print(x/y)
        ui = int(input("enter a number : "))  # give a char value
        print(ui)

    except ZeroDivisionError as i:
        print(f"hey user you can't divide a number", i)

    except ValueError as i:
        print(f"you have to give an int values")

try_except1(10,0)

def resource_open_and_close(x,y):

    try:
        print("resource_open")
        print(x/y)

    except Exception as e:
        print("Error :", e)

    finally:
        # finally block will always execute.. does not matter if you have an error or not
        print("resource_close")

resource_open_and_close(10,0)
