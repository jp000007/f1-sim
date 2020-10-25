#Jamie Parra
def f1sim():
    
    import math

    import re

    print("Welcome to the drivers practice program for the Italian GP, in Monza.\n")

    print("This is a simulator that predicts how fast you (the driver) will go on a race track in a Formula 1 car. \n")

    print("To begin select a practice program to acclimatize yourself to the track: \n1 -fuel conservation program \n2 -tire management program \n3 -qualifying program \n")

    practice_program = input("Enter program #: ")


    def intro():
        print("To begin select a practice program to acclimatize yourself to the track: \n1 -fuel conservation program \n2 -tire management program \n3 -qualifying program \n")
        practice_program = input("Enter program #: ")
        return practice_program




    def speed_trap_calculator(units, initial_velocity_speed):
        if units == ("kph"):
            initial_velocity_in_m_per_s = initial_velocity_speed / 3.6
        elif units == ("mph"): 
            initial_velocity_in_m_per_s = initial_velocity_speed * 0.447027778
                



        # Acceleration of a f1 car in m/s

        acceleration = 6.75


        # Distance from point a (20 meters after corner apex) to point b (halfway to he next corner) is 400 meters in a realatively straight line.
        # quadratic equation to solve for time.
        

        a = .5 * acceleration
        b = initial_velocity_in_m_per_s
        c = 0

        time = (-initial_velocity_in_m_per_s - math.sqrt((b**2) - 4 * a * c)) / (2 * a)

        time_at_final_position = time * -1

        #print(format(time_at_final_position, ".0f"))


        # Final velocity formula to solve for final Velocity , Vsubf = Vsubi + at 

        final_velocity_mpers = initial_velocity_in_m_per_s + (acceleration * time_at_final_position)

        # Convert back to kph & mph

        final_velocity_kph = final_velocity_mpers * 3.6
        return final_velocity_kph

        


    def mph_total():

        final_velocity_mph = speed_trap_calculator(units, initial_velocity_speed)
        return final_velocity_mph




    def delta():
        if units == ("kph"):
            initial_velocity_in_m_per_s = float(initial_velocity_speed / 3.6)
        elif units == ("mph"): 
            initial_velocity_in_m_per_s = float(initial_velocity_speed * 0.447027778)
                



        # Acceleration of a f1 car in m/s

        acceleration = 6.75


        # Distance from point a (20 meters after corner apex) to point b (halfway to he next corner) is 400 meters in a realatively straight line.
        # quadratic equation to solve for time.
        

        a = .5 * acceleration
        b = initial_velocity_in_m_per_s
        c = 0

        time = (-initial_velocity_in_m_per_s - math.sqrt((b**2) - 4 * a * c)) / (2 * a)

        time_at_final_position = time * -1

        delta = 7.407 - time_at_final_position

        return delta
# created a file for each of the three programs to save all entrys

    def fuelfile():
        avrgfile = open("fuelcons.times.csv", 'a')
        avrgfile.write("\nStart speed: " + str(initial_velocity_speed) + ',')
        avrgfile.write(" Final speed( in mph) 400 meters later: " + str(round(speed_mph)) + ',')
        avrgfile.write(" Time difference from low fuel mode race pace: " + str(round(delta_time))+ ' seconds,')

    def tirefile():
        avrgfile = open("tirecons.times.csv", 'a')
        avrgfile.write("\nStart speed: " + str(initial_velocity_speed) + ',')
        avrgfile.write(" Final speed( in mph) 400 meters later: " + str(round(speed_mph)) + ',')
        avrgfile.write(" Time difference from tire wear mode race pace: " + str(round(delta_time))+ ' seconds,')

    def qualifile():
        avrgfile = open("quali.times.csv", 'a')
        avrgfile.write("\nStart speed: " + str(initial_velocity_speed) + ',')
        avrgfile.write(" Final speed( in mph) 400 meters later: " + str(round(speed_mph)) + ',')
        avrgfile.write(" Time difference from qualy mode race pace: " + str(round(delta_time))+ ' seconds,')
        
# created a function to return the average of input and speed trap pace and time.

    def fuelaveragefile():
        numer = 0
        for i in range(1,21):
            avrgfile = open("fuelcons.times.csv", 'r')
            lines = avrgfile.read()
            return lines

    def tireaveragefile():
        numer = 0
        for i in range(1,21):
            avrgfile = open("tirecons.times.csv", 'r')
            lines = avrgfile.read()
            return lines

    def qualiaveragefile():
        numer = 0
        for i in range(1,21):
            avrgfile = open("quali.times.csv", 'r')
            lines = avrgfile.read()
            return lines
                                      
        

    # first program

    while(practice_program == ("1")):
        print("\nIn this program, we are simulating a race scenario where we need to switch the car to lean fuel mixture, to last until the end of the race. \n")
        print("\nAs a driver the key to fuel conservation is to be more gentle with power delivery out of corners. \n")
        initial_velocity_speed = int(input("To find the pace and speed out of each corner, enter the speed at one corner exit: "))
        units = input("Is this speed in mph or kph?: ")

    #calling functions above
        
        speed_kph = speed_trap_calculator(units, initial_velocity_speed)

        speed_mph = mph_total()

        

        while units == ("mph"):
            if (speed_mph < 160):
                print("\nExit speed is too slow, exessive fuel conservation, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif (speed_mph >= 160) and (speed_mph <= 167):
                print("\nGood average speed out of corner and fuel conservtion on target, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif (speed_mph > 167):
                print("\nQuick exit, missed fuel saving target, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break


        while units == ("kph"):
            if (speed_kph < 257):
                print("\nExit speed is too slow, exessive fuel conservation, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif (speed_kph >= 257) and (speed_kph <= 270):
                print("\nGood average speed out of corner and fuel conservtion on target speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif (speed_kph > 270):
                print("\nQuick exit, missed fuel saving target, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break

        #delta = difference in average time of 7.407 seconds with recorded time , delta = time - average time, negative delta is quicker pace, positive delta is slower pace


        delta_time =  delta()

        fuelfile()


        print("Delta ", format(delta_time, ".3f"), "s from race pace \n", sep='')

        

        average_results = input("\nWould you like to display previous entry's for this program? yes/no: ")
        if average_results == ("yes"):
            print(fuelaveragefile())
        


        retry = input("\nTry again? yes/no: ")

        if retry == ("yes"):
            continue
        elif retry == ("no"):
            diff_program = input("Choose a different program? yes/no: ")
            if diff_program == ("yes"):
                f1sim()                    
            else:
                print("Goodbye")
                break


        
    # Second program
            

    while practice_program == ("2"):
        print("\nIn this program, we are simulating a race senario where we need to save tire life to possibly skip a pit stop. \n")
        print("\nAs a driver the key to tire mangement is smooth application of the brake and throttle. \n")
        initial_velocity_speed = int(input("To find the pace and speed out of each corner, enter the speed at one corner exit: "))
        units = input("Is this speed in mph or kph?: ")

        #calling functions above
        
        speed_kph = speed_trap_calculator(units, initial_velocity_speed)

        speed_mph = mph_total()

        while units == ("mph"):
            if (speed_mph < 164):
                print("\nExit speed is too slow, exessive tire preservation, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif (speed_mph >= 164) and (speed_mph <= 167):
                print("\nGood average speed out of corner and tire preservation on target, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif (speed_mph > 167):
                print("\nQuick exit, missed target, exessive tire wear, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break


        while units == ("kph"):
            if (speed_kph < 264):
                print("\nExit speed is too slow, exessive tire preservation, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif (speed_kph >= 264) and (speed_kph <= 270):
                print("\nGood average speed out of corner and tire preservation on target, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif (speed_kph > 270):
                print("\nQuick exit, missed target, exessive tire wear, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break

        #delta = difference in average time of 7.407 seconds with recorded time , delta = time - average time, negative delta is quicker pace, positive delta is slower pace


        delta_time =  delta()

        tirefile()

        print("Delta ", format(delta_time, ".3f"), "s from race pace", sep='')

        average_results = input("\nWould you like to display previous entry's for this program? yes/no: ")
        if average_results == ("yes"):
            print(tireaveragefile())

        retry = input("\nTry again? yes/no: ")

        if retry == ("yes"):
            continue
        elif retry == ("no"):
            diff_program = input("Choose a different program? yes/no: ")
            if diff_program == ("yes"):
                f1sim()                    
            else:
                print("Goodbye")
                break




    # Third program


    while practice_program == ("3"):
        print("\nIn this program, we are simulating a qualifying session. This is where our lap time determines where we start at the beginning of the race \n")
        print("\nAs a driver, this is a chance to prove why you drive for us, showcase your skills and to drive the car at its limit. \n")
        initial_velocity_speed = int(input("To find the pace and speed out of each corner, enter the speed at one corner exit: "))
        units = input("Is this speed in mph or kph?: ")

        #calling functions above
        
        speed_kph = speed_trap_calculator(units, initial_velocity_speed)

        speed_mph = mph_total()

        while units == ("mph"):
            if (speed_mph < 167):
                print("\nExit speed is very slow,completely missed target, increase pace, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif (speed_mph >= 167) and (speed_mph <= 170):
                print("\nAcceptable average speed out of corner, still below target, increase pace, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break
            elif (speed_mph > 170):
                print("\nGood speed out of corner, keep pushing, speed trap is ", format(speed_mph, ".0f"), "MPH", sep='')
                break


        while units == ("kph"):
            if (speed_kph < 267):
                print("\nExit speed is very slow,completely missed target, increase pace, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif (speed_kph >= 267) and (speed_kph <= 274):
                print("\nAcceptable average speed out of corner, still below target, increase pace, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif (speed_kph >= 274.01) and (speed_kph <= 310):
                print("\nGood speed out of corner, keep pushing, speed trap is ", format(speed_kph, ".0f"), "KPH", sep='')
                break
            elif (speed_kph >= 310.01):
                print("\nInvalid input, car can't go that fast but we wish it could.. ")
                break

        #delta = difference in average time of 7.407 seconds with recorded time , delta = time - average time, negative delta is quicker pace, positive delta is slower pace


        delta_time =  delta()

        qualifile()

        print("Delta ", format(delta_time, ".3f"), "s from race pace", sep='')

        average_results = input("\nWould you like to display previous entry's for this program? yes/no: ")
        if average_results == ("yes"):
            print(qualiaveragefile())

        retry = input("\nTry again? yes/no: ")

        if retry == ("yes"):
            continue
        elif retry == ("no"):
            diff_program = input("Choose a different program? yes/no: ")
            if diff_program == ("yes"):
                f1sim()                    
            else:
                print("Goodbye")
                break


f1sim()


#one source I used for reading only the integers in a line only was from https://stackoverflow.com/questions/42989512/how-to-read-only-integers-from-a-file-with-strings-spaces-new-lines-and-intege


#one source I used was how to write functions within while loops on stack overflow @ https://stackoverflow.com/questions/44676100/python-unable-to-call-function-when-in-while-loop


