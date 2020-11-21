# Jamie Parra
"""F1 Simulator program"""
__author__ = "Jamie Parra"

import math


def choose_scenario():
    """This is the introduction of the program and home of the program where
    the user can return to try another one of the three different simulator
    options. The program also ends here as well if the user chooses to break
    the loop by choosing "no"."""
    retry = "yes"
    while retry == "yes":
        print("Welcome to the drivers practice program for the Italian GP, in"
              " Monza.\n")

        print("This is a simulator that predicts how fast you (the driver)"
              " will go on a race track in a Formula 1 car. \n")

        print("To begin select a practice program to acclimatize yourself to"
              " the track: \n1 -fuel conservation program \n2 -tire management"
              " program \n3 -qualifying program \n")

        practice_program = input("Enter program #: ")

        if practice_program == "3":
            calculate_acceleration_qualifying()
        elif practice_program == "2":
            calculate_acceleration_save_tires()
        elif practice_program == "1":
            calculate_acceleration()
        else:
            print("Invalid input")
        retry = input("\nRestart program? yes/no: ")
        if retry == "no":
            print("Goodbye!")


def speed_trap_calculator(units, initial_velocity_speed):
    """This function takes the users inputs of units of speed and number of
    speed from one of the practice programs and converts it to meters per
    second to be able to plug into the quadratic formula to find out how
    fast an accelerating F1 car would be traveling 400 meters down the track.
    Then it converts the speed at 400 meters and converts it back into KPH
    regard less of the units used by the user. It returns the speed in
    kilometers per hour at 400 meters from the start point."""
    if units == "kph":
        initial_velocity_in_m_per_s = initial_velocity_speed / 3.6
    elif units == "mph":
        initial_velocity_in_m_per_s = initial_velocity_speed * 0.447027778
    else:
        print("Invalid input for units.\nDefaulting to kph.")
        initial_velocity_in_m_per_s = float(initial_velocity_speed / 3.6)

    # Acceleration of a f1 car in m/s

    acceleration = 6.75

    # Distance from point a (20 meters after corner apex) to point b (halfway
    # to he next corner) is 400 meters in a relatively straight line.
    # quadratic equation to solve for time.

    a = .5 * acceleration
    c = 0

    time = (-initial_velocity_in_m_per_s - math.sqrt(
        (initial_velocity_in_m_per_s ** 2) - 4 * a * c)) / (
                   2 * a)

    time_at_final_position = time * -1

    # print(format(time_at_final_position, ".0f"))

    # Final velocity formula to solve for final Velocity ,
    # V_sub_f = V_sub_i + at

    final_velocity_m_per_s = initial_velocity_in_m_per_s + (
            acceleration * time_at_final_position)

    # Convert back to kph & mph

    final_velocity_kph = final_velocity_m_per_s * 3.6

    return final_velocity_kph


print(speed_trap_calculator.__doc__)


def mph_total(speed_kph):
    """This function converts the speed in kilometers per hour to miles per
    hour. It returns the speed in miles per hour."""
    final_velocity_mph = speed_kph * 0.621371
    return final_velocity_mph


def delta(units, initial_velocity_speed):
    """This function returns the time in seconds it takes for the F1 car to
    travel the 400 meters."""
    if units == "kph":
        initial_velocity_in_m_per_s = float(initial_velocity_speed / 3.6)
    elif units == "mph":
        initial_velocity_in_m_per_s = float(
            initial_velocity_speed * 0.447027778)
    else:
        print("Invalid input for units.\nDefaulting to kph.")
        initial_velocity_in_m_per_s = float(initial_velocity_speed / 3.6)

    # Acceleration of a f1 car in m/s

    acceleration = 6.75

    # Distance from point a (20 meters after corner apex) to point b (halfway
    # to he next corner) is 400 meters in a relatively straight line.
    # quadratic equation to solve for time.

    a = .5 * acceleration
    c = 0

    time = (-initial_velocity_in_m_per_s - math.sqrt(
        (initial_velocity_in_m_per_s ** 2) - 4 * a * c)) / (
                   2 * a)

    time_at_final_position = time * -1

    delta_1 = 7.407 - time_at_final_position

    return delta_1


# created a file for each of the three options to save all entries

def fuel_file(initial_velocity_speed, speed_mph, delta_time):
    """This function takes the input only from the calculate_acceleration
    function users initial speed (initial_velocity_speed), the final speed in
    units of miles per hour(speed_mph), and the time it takes to travel that
    distance (delta time) and saves it in a .csv file. It rounds numbers to
    whole numbers"""
    average_file = open("fuel_cons.times.csv", 'a')
    average_file.write("\nStart speed: " + str(initial_velocity_speed) + ',')
    average_file.write(" Final speed( in mph) 400 meters later: " + str(
        round(speed_mph)) + ',')
    average_file.write(" Time difference from low fuel mode race pace: " + str(
        round(delta_time)) + ' seconds,')


def tire_file(initial_velocity_speed, speed_mph, delta_time):
    """This function takes the input only from the
    calculate_acceleration_save_tires function users initial speed
    (initial_velocity_speed), the final speed in units of miles per
    hour(speed_mph), and the time it takes to travel that distance (delta time)
    and saves it in a .csv file. It rounds numbers to whole numbers"""
    average_file = open("tire_cons.times.csv", 'a')
    average_file.write("\nStart speed: " + str(initial_velocity_speed) + ',')
    average_file.write(" Final speed( in mph) 400 meters later: " + str(
        round(speed_mph)) + ',')
    average_file.write(" Time difference from tire wear mode race pace: "
                       + str(round(delta_time)) + ' seconds,')


def qualifying_file(initial_velocity_speed, speed_mph, delta_time):
    """This function takes the input only from the
    calculate_acceleration_qualifying function users initial speed
    (initial_velocity_speed), the final speed in units of miles per
    hour(speed_mph), and the time it takes to travel that distance (delta time)
    and saves it in a .csv file. It rounds numbers to whole numbers"""
    average_file = open("qualifying.times.csv", 'a')
    average_file.write("\nStart speed: " + str(initial_velocity_speed) + ',')
    average_file.write(" Final speed( in mph) 400 meters later: " + str(
        round(speed_mph)) + ',')
    average_file.write(" Time difference from qualifying mode race pace: "
                       + str(round(delta_time)) + ' seconds,')


# created a function to return the average of input and speed trap pace and
# time.

def fuel_average_file():
    """This functions returns all of the information saved on the file
    fuel_cons.times.csv up to 21 lines"""
    for i in range(1, 21):
        average_file = open("fuel_cons.times.csv", 'r')
        lines = average_file.read()
        return lines


def tire_average_file():
    """This functions returns all of the information saved on the file
    tire_cons.times.csv up to 21 lines"""
    for i in range(1, 21):
        average_file = open("tire_cons.times.csv", 'r')
        lines = average_file.read()
        return lines


def qualifying_average_file():
    """This functions returns all of the information saved on the file
    qualifying.times.csv up to 21 lines"""
    for i in range(1, 21):
        average_file = open("qualifying.times.csv", 'r')
        lines = average_file.read()
        return lines


def integer_verification():
    """Function verifies that only an integer is used"""
    try:
        initial_velocity = int(
            input("To find the pace and speed out of each corner, enter"
                  " the speed at one corner exit: "))
    except ValueError:
        print("Not an integer! Try again.")
    else:
        return initial_velocity


# first option

def calculate_acceleration():
    """This function simulates a fuel conservation exercise. It takes inputs
    for initial speed and units of speed and calls the speed trap function to
    solve for final speed and time returns a print statement depending
    on the final speed returned by the called speed trap function. It also
    prints the time returned from the called delta function. Then at the bottom
    once results are printed it gives the option to see previous entries, and
    asks if you want to retry this function, then if "no then function ends
    and returns to the choose_scenario function."""
    retry = "yes"
    while retry == "yes":
        print("\nIn this program, we are simulating a race scenario where we"
              " need to switch the car to lean fuel mixture, to last until the"
              " end of the race. \n")
        print("\nAs a driver the key to fuel conservation is to be more gentle"
              " with power delivery out of corners. \n")

        # The next function verifies the input is an integer and then assigns
        # the value to "initial_velocity_speed" to continue the flow of
        # execution

        initial_velocity_speed = integer_verification()

        units = input("Is this speed in mph or kph?: ")

        # calling functions to solve for final speed and having either unit
        # of speed available for the following while loops.

        speed_kph = speed_trap_calculator(units, initial_velocity_speed)

        speed_mph = mph_total(speed_kph)

        while units == "mph":
            if speed_mph < 160:
                print("\nExit speed is too slow, excessive fuel conservation,"
                      " speed trap is ",
                      format(speed_mph, ".0f"),
                      "MPH", sep='')
                break
            elif 160 <= speed_mph <= 167:
                print("\nGood average speed out of corner and fuel"
                      " conservation on target, speed trap is ",
                      format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif speed_mph > 167:
                print("\nQuick exit, missed fuel saving target, speed trap"
                      " is ", format(speed_mph, ".0f"), "MPH", sep='')
                break

        while units == "kph":
            if speed_kph < 257:
                print("\nExit speed is too slow, excessive fuel conservation,"
                      " speed trap is ",
                      format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif 257 <= speed_kph <= 270:
                print("\nGood average speed out of corner and fuel"
                      " conservation on target speed trap is ",
                      format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif speed_kph > 270:
                print("\nQuick exit, missed fuel saving target, speed trap"
                      " is ", format(speed_kph, ".0f"), "KPH", sep='')
                break

        # delta = difference in average time of 7.407 seconds with recorded
        # time
        # calling delta functions to solve for time over the distance covered.

        delta_time = delta(units, initial_velocity_speed)

        fuel_file(initial_velocity_speed, speed_mph, delta_time)

        print("Delta ", format(delta_time, ".3f"), "s from race pace \n",
              sep='')

        average_results = input("\nWould you like to display previous entry's"
                                " for this program? yes/no: ")
        if average_results == "yes":
            print(fuel_average_file())
        retry = input("\nTry again? yes/no: ")


# Second option

def calculate_acceleration_save_tires():
    """This function simulates a tire conservation exercise. It takes inputs
    for initial speed and units of speed and calls the speed trap function to
    solve for final speed and time returns a print statement depending
    on the final speed returned by the called speed trap function. It also
    prints the time returned from the called delta function. Then at the bottom
    once results are printed it gives the option to see previous entries, and
    asks if you want to retry this function, then if "no then function ends
    and returns to the choose_scenario function."""
    retry = "yes"
    while retry == "yes":
        print("\nIn this program, we are simulating a race scenario where we"
              " need to save tire life to possibly skip a pit stop. \n")
        print("\nAs a driver the key to tire management is smooth application"
              " of the brake and throttle. \n")

        # The next function verifies the input is an integer and then assigns
        # the value to "initial_velocity_speed" to continue the flow of
        # execution

        initial_velocity_speed = integer_verification()

        units = input("Is this speed in mph or kph?: ")

        # calling functions to solve for final speed and having either unit
        # of speed available for the following while loops.

        speed_kph = speed_trap_calculator(units, initial_velocity_speed)

        speed_mph = mph_total(speed_kph)

        while units == "mph":
            if speed_mph < 164:
                print("\nExit speed is too slow, excessive tire preservation,"
                      " speed trap is ",
                      format(speed_mph, ".0f"),
                      "MPH", sep='')
                break
            elif 164 <= speed_mph <= 167:
                print("\nGood average speed out of corner and tire"
                      " preservation on target, speed trap is ",
                      format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif speed_mph > 167:
                print("\nQuick exit, missed target, excessive tire wear, speed"
                      " trap is ",
                      format(speed_mph, ".0f"), "MPH",
                      sep='')
                break

        while units == "kph":
            if speed_kph < 264:
                print("\nExit speed is too slow, excessive tire preservation,"
                      " speed trap is ",
                      format(speed_kph, ".0f"),
                      "KPH", sep='')
                break
            elif 264 <= speed_kph <= 270:
                print("\nGood average speed out of corner and tire"
                      " preservation on target, speed trap is ",
                      format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif speed_kph > 270:
                print("\nQuick exit, missed target, excessive tire wear, speed"
                      " trap is ",
                      format(speed_kph, ".0f"), "KPH",
                      sep='')
                break

        # delta = difference in average time of 7.407 seconds with recorded
        # time
        # calling delta functions to solve for time over the distance covered.

        delta_time = delta(units, initial_velocity_speed)

        tire_file(initial_velocity_speed, speed_mph, delta_time)

        print("Delta ", format(delta_time, ".3f"), "s from race pace", sep='')

        average_results = input("\nWould you like to display previous entry's"
                                " for this program? yes/no: ")
        if average_results == "yes":
            print(tire_average_file())

        retry = input("\nTry again? yes/no: ")


# Third option

def calculate_acceleration_qualifying():
    """This function simulates a qualifying exercise. It takes inputs
    for initial speed and units of speed and calls the speed trap function to
    solve for final speed and time returns a print statement depending
    on the final speed returned by the called speed trap function. It also
    prints the time returned from the called delta function. Then at the bottom
    once results are printed it gives the option to see previous entries, and
    asks if you want to retry this function, then if "no then function ends
    and returns to the choose_scenario function."""
    retry = "yes"
    while retry == "yes":
        print("\nIn this program, we are simulating a qualifying session. This"
              " is where our lap time determines where we start at the"
              " beginning of the race \n")
        print("\nAs a driver, this is a chance to prove why you drive for us,"
              " showcase your skills and to drive the car at its limit. \n")

        # The next function verifies the input is an integer and then assigns
        # the value to "initial_velocity_speed" to continue the flow of
        # execution

        initial_velocity_speed = integer_verification()

        units = input("Is this speed in mph or kph?: ")

        # calling functions to solve for final speed and having either unit
        # of speed available for the following while loops.

        speed_kph = speed_trap_calculator(units, initial_velocity_speed)

        speed_mph = mph_total(speed_kph)

        while units == "mph":
            if speed_mph < 167:
                print("\nExit speed is very slow,completely missed target,"
                      " increase pace, speed trap is ",
                      format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif 167 <= speed_mph <= 170:
                print("\nAcceptable average speed out of corner, still below"
                      " target, increase pace, speed trap is ",
                      format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif speed_mph > 170:
                print("\nGood speed out of corner, keep pushing, speed trap"
                      " is ", format(speed_mph, ".0f"), "MPH", sep='')
                break

        while units == "kph":
            if speed_kph < 267:
                print("\nExit speed is very slow,completely missed target,"
                      " increase pace, speed trap is ",
                      format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif 267 <= speed_kph <= 274:
                print("\nAcceptable average speed out of corner, still below"
                      " target, increase pace, speed trap is ",
                      format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif 274.01 <= speed_kph <= 310:
                print(
                    "\nGood speed out of corner, keep pushing, speed trap is ",
                    format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif speed_kph >= 310.01:
                print("\nInvalid input, car can't go that fast but we wish it"
                      " could.. ")
                break

        # delta = difference in average time of 7.407 seconds with recorded
        # time
        # calling delta functions to solve for time over the distance covered.

        delta_time = delta(units, initial_velocity_speed)

        qualifying_file(initial_velocity_speed, speed_mph, delta_time)

        print("Delta ", format(delta_time, ".3f"), "s from race pace", sep='')

        average_results = input("\nWould you like to display previous entry's"
                                " for this program? yes/no: ")
        if average_results == "yes":
            print(qualifying_average_file())

        retry = input("\nTry again? yes/no: ")


choose_scenario()

# main source I used for final integration project assignment was PEP8 style
# guide at https://www.python.org/dev/peps/pep-0008/

# Source I used for docstrings was
# https://sites.google.com/site/profvanselow/software/pycharm

# one source I used for reading only the integers in a line only was from
# https://stackoverflow.com/questions/42989512/how-to-read-only-integers-from
# -a-file-with-strings-spaces-new-lines-and-integer


# one source I used was how to write functions within while loops on stack
# overflow @ https://stackoverflow.com/questions/44676100/python-unable-to
# -call-function-when-in-while-loop

