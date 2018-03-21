#!/usr/bin/python3
def read_a_number():
    n = int(input("Enter a positive number> "))
    if n > 0:
        return n
    else:
        raise Exception("This is not a positive number")
    
if __name__ == "__main__":
    print("---IMPORTANT---")
    print("'finally' does not work properly in Trinket!")
    print("Copy/paste the code in your IDE for full functionality")
    print("---END OF IMPORTANT---")
    valid_input = False
    att = 0
    # Repeat until we have a number
    while not valid_input:
        # Try doing something
        try:
            n = read_a_number()
            valid_input = True
        # Catch a ValueError exception: input is not a number (line 3)
        except ValueError as e:
            print("Please enter a number")
        # Catch any other exception
        except:
            print("Dear user, you just entered something I could not process. Sorry for any inconveniece.")
        # Executes in any case
        finally:
            att = att + 1
            if att > 3:
                # This exception crashes the program
                raise Exception("Too many tries")
    print("It took you %d attempts" % att)
    print("You entered ", n)
    print("%d * 2 = %d" % (n, n * 2))
    print("Continuing our program")
    print("This is the end of our broadcast")
    # Uncomment the following lines to see a custom Exception message
    #a = read_a_number()
    #print("You entered ", a)