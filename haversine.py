# It imports python modules
import sys, math, time
 
#########################################################    
# exit_program' Function - In order to exit the program #
#########################################################
def exit_program():
    print()
    print(r"""“All men dream: but not equally. Those who dream by night in the dusty recesses of their minds""") 
    print(r"""wake in the day to find that it was vanity: but the dreamers of the day are dangerous men, for""")
    print(r"""they may act their dreams with open eyes, to make it possible. This I did." """)
    print(r"""by T.E Lawrence "Lawrence of Arabia” """)
    print()
    print(r"""This python script was extracted from Antonio Bonaccorso's program called "Northern Lights" """) 
    print(r"""The name of this program is inspired by "Person of Interest" (an American science fiction crime drama""") 
    print(r"""television series created by Jonathan Nolan).""")
    print()
    print()
    time.sleep(3)
    print(r"""Although the intellectual property of this free program belongs to a third party, it supports the rescue""") 
    print(r"""activities of non-governmental organizations in the Mediterranean (and beyond) through word of mouth.""") 
    print(r"""It doesn't matter whether people speak well or poorly of the rescue activities of non-governmental organizations,""")
    print(r"""the important thing is that they are talked about.""")
    time.sleep(5)
    sys.exit(0)
#######################################################################################################################################    
# Degree of latitude (by A) (integer), minute of latitude (by A) (sexagesimal values), second of latitude (by A) (sexagesimal values) #
#######################################################################################################################################
# degree of latitude (by A) ... integer.    
def by_a_lat_degree():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of latitude (by A)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""North is indicated by a positive sign (+). South is indicated by a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        by_a_lat_int_degree_value = float(input("Enter the corresponding numeric value: "))
        int_degree= int(by_a_lat_int_degree_value)
        absint_degree= abs(int_degree)
        by_a_latitude_int_degree_value= math.copysign(absint_degree, by_a_lat_int_degree_value)
        r_ules = [by_a_lat_int_degree_value >=-90, by_a_lat_int_degree_value<=90]
        if all(r_ules):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_a_latitude_int_degree_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print("Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_a_lat_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_a_lat_int_degree_value)
            absint_degree= abs(int_degree)
            by_a_latitude_int_degree_value= math.copysign(absint_degree, by_a_lat_int_degree_value)
            r_ules = [by_a_lat_int_degree_value >=-90, by_a_lat_int_degree_value<=90]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_latitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()      
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""")
        print(r"""the Earth or another celestial body.""")
        print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of latitude (by A)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""North is indicated by a positive sign (+). South is indicated by a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_a_lat_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_a_lat_int_degree_value)
            absint_degree= abs(int_degree)
            by_a_latitude_int_degree_value= math.copysign(absint_degree, by_a_lat_int_degree_value)
            r_ules = [by_a_lat_int_degree_value >=-90, by_a_lat_int_degree_value<=90]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_latitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                  
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# minute of latitude (by A)... minutes in sexagesimal values
def by_a_lat_minute():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of latitude (by A)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_a_lat_int_minute_value = int(input("Enter the corresponding numeric value: "))
        ru_les = [by_a_lat_int_minute_value >=0, by_a_lat_int_minute_value<=59]
        if all(ru_les):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_a_lat_int_minute_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A minute of latitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_lat_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_a_lat_int_minute_value >=0, by_a_lat_int_minute_value<=59]
            if all(ru_les):
               print()    
               print("Data received.")
               print(r"""-------------------------------------------------------------------------------------------------------------------------""")
               return by_a_lat_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of latitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program() 
    except (ValueError, TypeError, EOFError, SyntaxError):
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A minute of latitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of latitude (by A)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_lat_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_a_lat_int_minute_value >=0, by_a_lat_int_minute_value<=59]
            if all(ru_les):
               print()    
               print("Data received.")
               print(r"""-------------------------------------------------------------------------------------------------------------------------""")
               return by_a_lat_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of latitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            print(r"""A minute of latitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# second of latitude (by A)... seconds in sexagesimal values
def by_a_lat_second():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of latitude (by A)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_a_lat_int_second_value = int(input("Enter the corresponding numeric value: "))
        rul_es = [by_a_lat_int_second_value >=0, by_a_lat_int_second_value<=59]
        if all(rul_es):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_a_lat_int_second_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A second of latitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_lat_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_a_lat_int_second_value >=0, by_a_lat_int_second_value<=59]
            if all(rul_es):
               print()    
               print("Data received.")
               print(r"""-------------------------------------------------------------------------------------------------------------------------""")
               return by_a_lat_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of latitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A second of latitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of latitude (by A)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""") 
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_lat_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_a_lat_int_second_value >=0, by_a_lat_int_second_value<=59]
            if all(rul_es):
               print()    
               print("Data received.")
               print(r"""-------------------------------------------------------------------------------------------------------------------------""")
               return by_a_lat_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of latitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""A second of latitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
#######################################################################################################################################    
# Degree of latitude (by B) (integer), minute of latitude (by B) (sexagesimal values), second of latitude (by B) (sexagesimal values) #
#######################################################################################################################################
# degree of latitude (by B) ... integer.    
def by_b_lat_degree():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of latitude (by B)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""North is indicated by a positive sign (+). South is indicated by a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        by_b_lat_int_degree_value = float(input("Enter the corresponding numeric value: "))
        int_degree= int(by_b_lat_int_degree_value)
        absint_degree= abs(int_degree)
        by_b_latitude_int_degree_value= math.copysign(absint_degree, by_b_lat_int_degree_value)
        r_ules = [by_b_lat_int_degree_value >=-90, by_b_lat_int_degree_value<=90]
        if all(r_ules):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_b_latitude_int_degree_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print("Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_b_lat_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_b_lat_int_degree_value)
            absint_degree= abs(int_degree)
            by_b_latitude_int_degree_value= math.copysign(absint_degree, by_b_lat_int_degree_value)
            r_ules = [by_b_lat_int_degree_value >=-90, by_b_lat_int_degree_value<=90]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_latitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""")
        print(r"""the Earth or another celestial body.""")
        print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of latitude (by B)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""North is indicated by a positive sign (+). South is indicated by a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_b_lat_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_b_lat_int_degree_value)
            absint_degree= abs(int_degree)
            by_b_latitude_int_degree_value= math.copysign(absint_degree, by_b_lat_int_degree_value)
            r_ules = [by_b_lat_int_degree_value >=-90, by_b_lat_int_degree_value<=90]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_latitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                  
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""In geography, latitude is a geographic coordinate that specifies the north-south position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print(r"""Latitude is given as an angle that ranges from −90° at the south pole to 90° at the north pole, with 0° at the Equator.""")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# minute of latitude (by B)... minutes in sexagesimal values
def by_b_lat_minute():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of latitude (by B)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_b_lat_int_minute_value = int(input("Enter the corresponding numeric value: "))
        ru_les = [by_b_lat_int_minute_value >=0, by_b_lat_int_minute_value<=59]
        if all(ru_les):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_b_lat_int_minute_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A minute of latitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_lat_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_b_lat_int_minute_value >=0, by_b_lat_int_minute_value<=59]
            if all(ru_les):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_lat_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of latitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()
    except (ValueError, TypeError, EOFError, SyntaxError):
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A minute of latitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of latitude (by B)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_lat_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_b_lat_int_minute_value >=0, by_b_lat_int_minute_value<=59]
            if all(ru_les):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_lat_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of latitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            print(r"""A minute of latitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# second of latitude (by B)... seconds in sexagesimal values
def by_b_lat_second():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of latitude (by B)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_b_lat_int_second_value = int(input("Enter the corresponding numeric value: "))
        rul_es = [by_b_lat_int_second_value >=0, by_b_lat_int_second_value<=59]
        if all(rul_es):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_b_lat_int_second_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A second of latitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_lat_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_b_lat_int_second_value >=0, by_b_lat_int_second_value<=59]
            if all(rul_es):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_lat_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of latitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()   
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A second of latitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of latitude (by B)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""") 
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_lat_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_b_lat_int_second_value >=0, by_b_lat_int_second_value<=59]
            if all(rul_es):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_lat_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of latitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""A second of latitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
 
##########################################################################################################################################    
# Degree of longitude (by A) (integer), minute of longitude (by A) (sexagesimal values), second of longitude (by A) (sexagesimal values) #
##########################################################################################################################################
# degree of longitude (by A) ... integer.    
def by_a_long_degree():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of longitude (by A)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""East is indicated with a positive sign (+). West with a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        by_a_long_int_degree_value = float(input("Enter the corresponding numeric value: "))
        int_degree= int(by_a_long_int_degree_value)
        absint_degree= abs(int_degree)
        by_a_longitude_int_degree_value= math.copysign(absint_degree, by_a_long_int_degree_value)
        r_ules = [by_a_long_int_degree_value >=-180, by_a_long_int_degree_value<=180]
        if all(r_ules):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_a_longitude_int_degree_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print("Longitude is given as an angle that ranges from −180° to 180°.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_a_long_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_a_long_int_degree_value)
            absint_degree= abs(int_degree)
            by_a_longitude_int_degree_value= math.copysign(absint_degree, by_a_long_int_degree_value)
            r_ules = [by_a_long_int_degree_value >=-180, by_a_long_int_degree_value<=180]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_longitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program() 
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""")
        print(r"""the Earth or another celestial body.""")
        print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of longitude (by A)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""East is indicated with a positive sign (+). West with a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_a_long_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_a_long_int_degree_value)
            absint_degree= abs(int_degree)
            by_a_longitude_int_degree_value= math.copysign(absint_degree, by_a_long_int_degree_value)
            r_ules = [by_a_long_int_degree_value >=-180, by_a_long_int_degree_value<=180]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_longitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                  
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# minute of longitude (by A)... minutes in sexagesimal values
def by_a_long_minute():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of longitude (by A)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_a_long_int_minute_value = int(input("Enter the corresponding numeric value: "))
        ru_les = [by_a_long_int_minute_value >=0, by_a_long_int_minute_value<=59]
        if all(ru_les):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_a_long_int_minute_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A minute of longitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_long_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_a_long_int_minute_value >=0, by_a_long_int_minute_value<=59]
            if all(ru_les):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_long_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of longitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()
    except (ValueError, TypeError, EOFError, SyntaxError):
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A minute of longitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of longitude (by A)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_long_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_a_long_int_minute_value >=0, by_a_long_int_minute_value<=59]
            if all(ru_les):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_long_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of longitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            print(r"""A minute of longitude (by A) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# second of longitude (by A)... seconds in sexagesimal values
def by_a_long_second():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of longitude (by A)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_a_long_int_second_value = int(input("Enter the corresponding numeric value: "))
        rul_es = [by_a_long_int_second_value >=0, by_a_long_int_second_value<=59]
        if all(rul_es):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_a_long_int_second_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A second of longitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_long_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_a_long_int_second_value >=0, by_a_long_int_second_value<=59]
            if all(rul_es):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_long_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of longitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A second of longitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of longitude (by A)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""") 
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_a_long_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_a_long_int_second_value >=0, by_a_long_int_second_value<=59]
            if all(rul_es):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_a_long_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of longitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""A second of longitude (by A) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
##########################################################################################################################################    
# Degree of longitude (by B) (integer), minute of longitude (by B) (sexagesimal values), second of longitude (by B) (sexagesimal values) #
##########################################################################################################################################
# degree of longitude (by B) ... integer.    
def by_b_long_degree():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of longitude (by B)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""East is indicated with a positive sign (+). West with a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        by_b_long_int_degree_value = float(input("Enter the corresponding numeric value: "))
        int_degree= int(by_b_long_int_degree_value)
        absint_degree= abs(int_degree)
        by_b_longitude_int_degree_value= math.copysign(absint_degree, by_b_long_int_degree_value)
        r_ules = [by_b_long_int_degree_value >=-180, by_b_long_int_degree_value<=180]
        if all(r_ules):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_b_longitude_int_degree_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print("Longitude is given as an angle that ranges from −180° to 180°.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_b_long_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_b_long_int_degree_value)
            absint_degree= abs(int_degree)
            by_b_longitude_int_degree_value= math.copysign(absint_degree, by_b_long_int_degree_value)
            r_ules = [by_b_long_int_degree_value >=-180, by_b_long_int_degree_value<=180]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_longitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""")
        print(r"""the Earth or another celestial body.""")
        print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (degrees of longitude (by B)).")
        print(r"""In mathematics, the sign of a real number is its property of being either positive, negative, or 0.""")
        print(r"""East is indicated with a positive sign (+). West with a negative sign (-).""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("It only accepts integers.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            by_b_long_int_degree_value = float(input("Enter the corresponding numeric value: "))
            int_degree= int(by_b_long_int_degree_value)
            absint_degree= abs(int_degree)
            by_b_longitude_int_degree_value= math.copysign(absint_degree, by_b_long_int_degree_value)
            r_ules = [by_b_long_int_degree_value >=-180, by_b_long_int_degree_value<=180]
            if all(r_ules):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_longitude_int_degree_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""") 
                print(r"""the Earth or another celestial body.""")
                print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                  
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""In geography, longitude is a geographic coordinate that specifies the east-west position of a point on the surface of""")
            print(r"""the Earth or another celestial body.""")
            print(r"""Longitude is given as an angle that ranges from −180° to 180°.""")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# minute of longitude (by B)... minutes in sexagesimal values
def by_b_long_minute():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of longitude (by B)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_b_long_int_minute_value = int(input("Enter the corresponding numeric value: "))
        ru_les = [by_b_long_int_minute_value >=0, by_b_long_int_minute_value<=59]
        if all(ru_les):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_b_long_int_minute_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A minute of longitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_long_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_b_long_int_minute_value >=0, by_b_long_int_minute_value<=59]
            if all(ru_les):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_long_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of longitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program() 
    except (ValueError, TypeError, EOFError, SyntaxError):
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A minute of longitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (minutes of longitude (by B)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_long_int_minute_value = int(input("Enter the corresponding numeric value: ")) 
            ru_les = [by_b_long_int_minute_value >=0, by_b_long_int_minute_value<=59]
            if all(ru_les):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_long_int_minute_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A minute of longitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            print(r"""A minute of longitude (by B) is a unit of angular measurement equal to 1/60 of a degree.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
# second of longitude (by B)... seconds in sexagesimal values
def by_b_long_second():
    print()
    try:
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of longitude (by B)):")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("You must enter an absolute integer value between 0 and 59.")
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")       
        by_b_long_int_second_value = int(input("Enter the corresponding numeric value: "))
        rul_es = [by_b_long_int_second_value >=0, by_b_long_int_second_value<=59]
        if all(rul_es):
            print()    
            print("Data received.")
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            return by_b_long_int_second_value
        else:
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print("Something went wrong. I need to retry the data request.")
            print(r"""A second of longitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you must enter an absolute integer value between 0 and 59.")
            time.sleep(3)
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_long_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_b_long_int_second_value >=0, by_b_long_int_second_value<=59]
            if all(rul_es):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_long_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of longitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()
    except (ValueError, TypeError, EOFError, SyntaxError):
        print()
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("Something went wrong. I need to retry the data request.")
        print(r"""A second of longitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print("I proceed with the data acquisition (seconds of longitude (by B)).")
        print(r"""-------------------------------------------------------------------------------------------------------------------------""") 
        print("You must enter an absolute integer value between 0 and 59.")
        time.sleep(3)
        try:
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")  
            by_b_long_int_second_value = int(input("Enter the corresponding numeric value: "))
            rul_es = [by_b_long_int_second_value >=0, by_b_long_int_second_value<=59]
            if all(rul_es):
                print()    
                print("Data received.")
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                return by_b_long_int_second_value
            else:
                print()
                print(r"""-------------------------------------------------------------------------------------------------------------------------""")
                print(r"""A second of longitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
                print("Therefore, you had to enter an absolute integer value between 0 and 59.")
                print("You failed to answer the question.") 
                print("The program will be closed.")
                exit_program()                                 
        except (ValueError, TypeError, EOFError, SyntaxError):
            print()
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print(r"""A second of longitude (by B) is a unit of angular measurement equal to 1/60 of a minute.""")
            print("Therefore, you had to enter an absolute integer value between 0 and 59.")
            print("You failed to answer the question.") 
            print("The program will be closed.")
            exit_program()
 
###############################################################################################################################             
# Piloting                                                                                                                    #
# INVERSE HAVERSINE FORMULA                                                                                                   #
# Distances between coordinates (from "A" to "B"): Latitude Δφ=φB-φA; Longitude Δλ=λB-λA                                      #
# if Δφ is positive you go to NORTH; if Δφ is negative you go to SOUTH;                                                       #
# if Δλ is positive you go to EAST; if Δλ is negative you go to WEST                                                          #
# The Inverse Haversine formula calculates the shortest distance between two points on a sphere using their latitudes and     #
# longitudes measured along the surface. The conventional radius of the earth is 6371 km.                                     #
###############################################################################################################################
# Δφ =latitude subtraction (a in the direction of b) 
def haversine_latba():
    # lat A and abs
    alatintdegree = by_a_lat_degree()
    alatminute = by_a_lat_minute()
    alatsecond = by_a_lat_second()
    absalatintdegree = abs (alatintdegree)
    absalatminute = abs (alatminute)
    absalatsecond = abs (alatsecond)
    # lat B and abs
    blatintdegree = by_b_lat_degree()
    blatminute = by_b_lat_minute()
    blatsecond = by_b_lat_second()
    absblatintdegree = abs (blatintdegree)
    absblatminute = abs (blatminute)
    absblatsecond = abs (blatsecond)
    # lat second B+A & B>A
    Δφplussecond = float (absblatsecond + absalatsecond)
    absΔφplussecond = abs(Δφplussecond)
    # lat minute B+A & B>A
    Δφplusminute = float (absblatminute + absalatminute)
    absΔφplusminute = abs(Δφplusminute)
    # lat second B-A & B>A
    Δφsecond = float (absblatsecond - absalatsecond)
    absΔφsecond = abs(Δφsecond)
    # lat minute B-A & B>A
    Δφminute = float (absblatminute - absalatminute)
    absΔφminute = abs(Δφminute) 
    # lat degree & B>A
    Δφdegree = float (blatintdegree - alatintdegree)
    absΔφdegree = abs(Δφdegree) 
    positiveornegativeΔφdegree= int(math.copysign(1, Δφdegree))
    # lat second B+A & B<A
    mΔφplussecond = float (absalatsecond + absblatsecond)
    mabsΔφplussecond = abs(mΔφplussecond)
    # lat minute B+A & B<A
    mΔφplusminute = float (absalatminute + absblatminute)
    mabsΔφplusminute = abs(mΔφplusminute)
    # lat second B-A & B<A
    mΔφsecond = float (absalatsecond - absblatsecond)
    mabsΔφsecond = abs(mΔφsecond)
    # lat minute B-A & B<A
    mΔφminute = float (absalatminute - absblatminute)
    mabsΔφminute = abs(mΔφminute) 
    # lat degree & B<A
    mΔφdegree = float (blatintdegree - alatintdegree)
    mabsΔφdegree = abs(mΔφdegree) 
    mpositiveornegativeΔφdegree= int(math.copysign(1, mΔφdegree))
    # In subtractions with values ​​with opposite signs, an addition is performed. B>A
    ruleslat1= [absΔφplussecond >= 0, absΔφplussecond <=59, absΔφplusminute >=0,  absΔφplusminute<=59, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]         
    ruleslat2= [absΔφplussecond >=59, ((absΔφplussecond//60)+absΔφplusminute)<=59,  absΔφplusminute>=0, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]
    ruleslat3= [absΔφplussecond >= 0, ((absΔφplussecond//60)+absΔφplusminute)>=59, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]
    ruleslat4=[absΔφplussecond >= 0, absΔφplussecond <=59, absΔφplusminute>=59, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]
    # In subtractions with values ​​with equal signs, a subtraction is performed. B>A
    ruleslat5= [absblatsecond >= absalatsecond, absΔφsecond<=59, absblatminute>=absalatminute, absΔφsecond<=59, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]         
    ruleslat6= [absblatsecond < absalatsecond, absblatminute>absalatminute, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]
    ruleslat7= [absblatsecond < absalatsecond, absblatminute<=absalatminute, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]
    ruleslat8= [absblatsecond >= absalatsecond, absΔφsecond <=59, absblatminute<absalatminute, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree >= absalatintdegree]
    # In subtractions with values ​​with opposite signs, an addition is performed. B<A
    ruleslat10= [absΔφplussecond >= 0, absΔφplussecond <=59, absΔφplusminute >=0,  absΔφplusminute<=59, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]         
    ruleslat20= [absΔφplussecond >=59, ((absΔφplussecond//60)+absΔφplusminute)<=59,  absΔφplusminute>=0, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]
    ruleslat30= [absΔφplussecond >= 0, ((absΔφplussecond//60)+absΔφplusminute)>=59, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]
    ruleslat40=[absΔφplussecond >= 0, absΔφplussecond <=59, absΔφplusminute>=59, math.copysign(1, alatintdegree)!=math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]
    # In subtractions with values ​​with equal signs, a subtraction is performed. B<A
    ruleslat50= [absalatsecond >= absblatsecond, absΔφsecond<=59, absalatminute>=absblatminute, absΔφsecond<=59, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]         
    ruleslat60= [absalatsecond < absblatsecond, absalatminute>absblatminute, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]
    ruleslat70= [absalatsecond < absblatsecond, absalatminute<=absblatminute, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]
    ruleslat80= [absalatsecond >= absblatsecond, absΔφsecond <=59, absalatminute<absblatminute, math.copysign(1, alatintdegree)==math.copysign(1, blatintdegree), absblatintdegree < absalatintdegree]
    # mathematical calculations      
    if all(ruleslat1):
        return Δφdegree, Δφplusminute, Δφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat2): 
        print()
        newΔφplussecond = int(Δφplussecond%60)
        newΔφplusminute = int(Δφplusminute+(Δφplussecond//60))
        return Δφdegree, newΔφplusminute, newΔφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat3):
        print()
        newΔφplussecond = int(Δφplussecond%60)
        newΔφplusminute = int(Δφplusminute+(Δφplussecond//60))
        definitiveΔφplusminute = int(newΔφplusminute%60)
        newΔφplusdegree = float(positiveornegativeΔφdegree*abs((absblatintdegree+absalatintdegree)+(newΔφplusminute//60)))
        return newΔφplusdegree, definitiveΔφplusminute, newΔφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat4):
        print()
        definitiveΔφplusminute = int(Δφplusminute%60)
        newΔφplusdegree = float(positiveornegativeΔφdegree*abs((absblatintdegree+absalatintdegree)+(Δφplusminute//60)))   
        return newΔφplusdegree, definitiveΔφplusminute, Δφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat5):
        return Δφdegree, Δφminute, Δφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat6):
        newΔφsecond=int((absblatsecond+60)-absalatsecond)
        definitiveΔφminute = int ((absblatminute-1)-absalatminute)
        return Δφdegree, definitiveΔφminute, newΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat7):
        newΔφsecond=int((absblatsecond+60)-absalatsecond)
        definitiveΔφminute = int(((absblatminute+60-1)-absalatminute))
        newΔφdegree= float(positiveornegativeΔφdegree*abs((absblatintdegree-1)-absalatintdegree))
        return newΔφdegree, definitiveΔφminute, newΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat8):
        definitiveΔφminute = int(((absblatminute+60)-absalatminute))
        newΔφdegree= float(positiveornegativeΔφdegree*abs((absblatintdegree-1)-absalatintdegree))    
        return newΔφdegree, definitiveΔφminute, absΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat10):
        return mΔφdegree, mΔφplusminute, mΔφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat20): 
        print()
        mnewΔφplussecond = int(mΔφplussecond%60)
        mnewΔφplusminute = int(mΔφplusminute+(mΔφplussecond//60))
        return mΔφdegree, mnewΔφplusminute, mnewΔφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat30):
        print()
        mnewΔφplussecond = int(mΔφplussecond%60)
        mnewΔφplusminute = int(mΔφplusminute+(mΔφplussecond//60))
        mdefinitiveΔφplusminute = int(mnewΔφplusminute%60)
        mnewΔφplusdegree = float(mpositiveornegativeΔφdegree*abs((absalatintdegree+absblatintdegree)+(mnewΔφplusminute//60)))
        return mnewΔφplusdegree, mdefinitiveΔφplusminute, mnewΔφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat40):
        print()
        mdefinitiveΔφplusminute = int(mΔφplusminute%60)
        newΔφplusdegree = float(mpositiveornegativeΔφdegree*abs((absalatintdegree+absblatintdegree)+(mΔφplusminute//60)))   
        return mnewΔφplusdegree, mdefinitiveΔφplusminute, mΔφplussecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat50):
        return mΔφdegree, mΔφminute, mΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat60):
        mnewΔφsecond=int((absalatsecond+60)-absblatsecond)
        mdefinitiveΔφminute = int ((absalatminute-1)-absblatminute)
        return mΔφdegree, mdefinitiveΔφminute, mnewΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat70):
        mnewΔφsecond=int((absalatsecond+60)-absblatsecond)
        mdefinitiveΔφminute = int(((absalatminute+60-1)-absblatminute))
        mnewΔφdegree= float(mpositiveornegativeΔφdegree*abs((absalatintdegree-1)-absblatintdegree))
        return mnewΔφdegree, mdefinitiveΔφminute, mnewΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all(ruleslat80):
        mdefinitiveΔφminute = int(((absalatminute+60)-absblatminute))
        mnewΔφdegree= float(mpositiveornegativeΔφdegree*abs((absalatintdegree-1)-absblatintdegree))    
        return mnewΔφdegree, mdefinitiveΔφminute, mabsΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
# for python the int numbers 0, 0.0, -0.0 are all =0. In order to make them different each other, I will use "str"
def checkzerohaversine_latba():
    callhaversine_latba=haversine_latba()
    Δφdegree= float(callhaversine_latba[0])
    Δφminute= int(callhaversine_latba[1])
    Δφsecond= int(callhaversine_latba[2])
    ################################################
    # φA and φB for "return"
    alatintdegree= float(callhaversine_latba[3])
    alatminute= int(callhaversine_latba[4])
    alatsecond= int(callhaversine_latba[5])
    blatintdegree= float(callhaversine_latba[6])
    blatminute= int(callhaversine_latba[7])
    blatsecond= int(callhaversine_latba[8])
    ################################################
    ruleszeronegative= [str(Δφdegree)==("-0.0")]
    ruleszeropositive= [str(Δφdegree)==("0.0")]
    if all(ruleszeronegative): 
        intdegreezerodivision=float("-0")
        stringdegreezerodivision= str(r"""-0""")
        absΔφminute=abs(int(Δφminute))
        absΔφsecond=abs(int(Δφsecond))
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print ("Subtracting latitude (a in the direction of b) is equivalent to:")
        print (stringdegreezerodivision,(r"""°"""),absΔφminute,(r"""'"""),absΔφsecond,(r"""" """))
        # intdegreezerodivision is a float
        return intdegreezerodivision, absΔφminute, absΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    elif all (ruleszeropositive):
        intdegreezerodivision=float("0")
        stringdegreezerodivision= str(r"""0""")
        absΔφminute=abs(int(Δφminute))
        absΔφsecond=abs(int(Δφsecond))
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print ("Subtracting latitude (a in the direction of b) is equivalent to:")
        print (stringdegreezerodivision,(r"""°"""),absΔφminute,(r"""'"""),absΔφsecond,(r"""" """))
        # intdegreezerodivision is a float
        return intdegreezerodivision, absΔφminute, absΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
    else:
        stringdegreezerodivision= str(int(Δφdegree))
        absΔφminute=abs(int(Δφminute))
        absΔφsecond=abs(int(Δφsecond))
        print(r"""-------------------------------------------------------------------------------------------------------------------------""")
        print ("Subtracting latitude (a in the direction of b) is equivalent to:")
        print (stringdegreezerodivision,(r"""°"""),absΔφminute,(r"""'"""),absΔφsecond,(r"""" """))
        return Δφdegree, absΔφminute, absΔφsecond, alatintdegree, alatminute, alatsecond, blatintdegree, blatminute, blatsecond
# Δλ =longitude subtraction (a in the direction of b) 
def haversine_longba():
    # long A and abs
    alongintdegree = by_a_long_degree()
    alongminute = by_a_long_minute()
    alongsecond = by_a_long_second()
    absalongintdegree = abs (alongintdegree)
    absalongminute = abs (alongminute)
    absalongsecond = abs (alongsecond)
    # long B and abs
    blongintdegree = by_b_long_degree()
    blongminute = by_b_long_minute()
    blongsecond = by_b_long_second()
    absblongintdegree = abs (blongintdegree)
    absblongminute = abs (blongminute)
    absblongsecond = abs (blongsecond)
    # long second B+A & B>A
    Δλplussecond = float (absblongsecond + absalongsecond)
    absΔλplussecond = abs(Δλplussecond)
    # long minute B+A & B>A
    Δλplusminute = float (absblongminute + absalongminute)
    absΔλplusminute = abs(Δλplusminute)
    # long second B-A & B>A
    Δλsecond = float (absblongsecond - absalongsecond)
    absΔλsecond = abs(Δλsecond)
    # long minute B-A & B>A
    Δλminute = float (absblongminute - absalongminute)
    absΔλminute = abs(Δλminute) 
    # long degree & B>A
    Δλdegree = float (blongintdegree - alongintdegree)
    absΔλdegree = abs(Δλdegree) 
    positiveornegativeΔλdegree= int(math.copysign(1, Δλdegree))
    # long second B+A & B<A
    mΔλplussecond = float (absalongsecond + absblongsecond)
    mabsΔλplussecond = abs(mΔλplussecond)
    # long minute B+A & B<A
    mΔλplusminute = float (absalongminute + absblongminute)
    mabsΔλplusminute = abs(mΔλplusminute)
    # long second B-A & B<A
    mΔλsecond = float (absalongsecond - absblongsecond)
    mabsΔλsecond = abs(mΔλsecond)
    # long minute B-A & B<A
    mΔλminute = float (absalongminute - absblongminute)
    mabsΔλminute = abs(Δλminute) 
    # long degree & B<A
    mΔλdegree = float (blongintdegree - alongintdegree)
    mabsΔλdegree = abs(mΔλdegree) 
    mpositiveornegativeΔλdegree= int(math.copysign(1, mΔλdegree))
    # In subtractions with values ​​with opposite signs, an addition is performed & B>A
    ruleslong1= [absΔλplussecond >= 0, absΔλplussecond <=59, absΔλplusminute >=0,  absΔλplusminute<=59, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]         
    ruleslong2= [absΔλplussecond >=59, ((absΔλplussecond//60)+absΔλplusminute)<=59,  absΔλplusminute>=0, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]
    ruleslong3= [absΔλplussecond >= 0, ((absΔλplussecond//60)+absΔλplusminute)>=59, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]
    ruleslong4=[absΔλplussecond >= 0, absΔλplussecond <=59, absΔλplusminute>=59, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]
    # In subtractions with values ​​with equal signs, a subtraction is performed & B>A
    ruleslong5= [absblongsecond >= absalongsecond, absΔλsecond<=59, absblongminute>=absalongminute, absΔλsecond<=59, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]         
    ruleslong6= [absblongsecond < absalongsecond, absblongminute>absalongminute, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]
    ruleslong7= [absblongsecond < absalongsecond, absblongminute<=absalongminute, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]
    ruleslong8= [absblongsecond >= absalongsecond, absΔλsecond <=59, absblongminute<absalongminute, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree >= absalongintdegree]
    # In subtractions with values ​​with opposite signs, an addition is performed & B<A
    ruleslong10= [mabsΔλplussecond >= 0, mabsΔλplussecond <=59, mabsΔλplusminute >=0,  mabsΔλplusminute<=59, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]         
    ruleslong20= [mabsΔλplussecond >=59, ((mabsΔλplussecond//60)+mabsΔλplusminute)<=59, mabsΔλplusminute>=0, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]
    ruleslong30= [mabsΔλplussecond >= 0, ((mabsΔλplussecond//60)+mabsΔλplusminute)>=59, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]
    ruleslong40= [mabsΔλplussecond >= 0, mabsΔλplussecond <=59, mabsΔλplusminute>=59, math.copysign(1, alongintdegree)!=math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]
    # In subtractions with values ​​with equal signs, a subtraction is performed & B<A
    ruleslong50= [absalongsecond >= absblongsecond, mabsΔλsecond<=59, absalongminute>=absblongminute, mabsΔλsecond<=59, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]         
    ruleslong60= [absalongsecond < absblongsecond, absalongminute>absblongminute, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]
    ruleslong70= [absalongsecond < absblongsecond, absalongminute<=absblongminute, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]
    ruleslong80= [absalongsecond >= absblongsecond, mabsΔλsecond <=59, absalongminute<absblongminute, math.copysign(1, alongintdegree)==math.copysign(1, blongintdegree), absblongintdegree < absalongintdegree]
    # mathematical calculations      
    if all(ruleslong1):
        Δλdegree= float(Δλdegree)
        Δλminute= int(Δλplusminute)
        Δλsecond= int(Δλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
    elif all(ruleslong2): 
        print()
        newΔλplussecond = int(Δλplussecond%60)
        newΔλplusminute = int(Δλplusminute+(Δλplussecond//60)) 
        Δλdegree= float(Δλdegree)
        Δλminute= int(newΔλplusminute)
        Δλsecond= int(newΔλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
    elif all(ruleslong3):
        print()
        newΔλplussecond = int(Δλplussecond%60)
        newΔλplusminute = int(Δλplusminute+(Δλplussecond//60))
        definitiveΔλplusminute = int(newΔλplusminute%60)
        newΔλplusdegree = float(positiveornegativeΔλdegree*abs((absblongintdegree+absalongintdegree)+(newΔλplusminute//60)))
        Δλdegree= float(newΔλplusdegree)
        Δλminute= int(definitiveΔλplusminute)
        Δλsecond= int(newΔλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond        
    elif all(ruleslong4):
        print()
        definitiveΔλplusminute = int(Δλplusminute%60)
        newΔλplusdegree = float(positiveornegativeΔλdegree*abs((absblongintdegree+absalongintdegree)+(Δλplusminute//60))) 
        Δλdegree= float(newΔλplusdegree)
        Δλminute= int(definitiveΔλplusminute)
        Δλsecond= int(Δλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond     
    elif all(ruleslong5):
        Δλdegree= float(Δλdegree)
        Δλminute= int(Δλminute)
        Δλsecond= int(Δλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond       
    elif all(ruleslong6):
        newΔλsecond=int((absblongsecond+60)-absalongsecond)
        definitiveΔλminute = int ((absblongminute-1)-absalongminute) 
        Δλdegree= float(Δλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(newΔλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond    
    elif all(ruleslong7):
        newΔλsecond=int((absblongsecond+60)-absalongsecond)
        definitiveΔλminute = int(((absblongminute+60-1)-absalongminute))
        newΔλdegree= float(positiveornegativeΔλdegree*abs((absblongintdegree-1)-absalongintdegree))
        Δλdegree= float(newΔλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(newΔλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond   
    elif all(ruleslong8):
        definitiveΔλminute = int(((absblongminute+60)-absalongminute))
        newΔλdegree= float(positiveornegativeΔλdegree*abs((absblongintdegree-1)-absalongintdegree))
        Δλdegree= float(newΔλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(absΔλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
        return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond        
    elif all(ruleslong10):
        Δλdegree= float(mΔλdegree)
        Δλminute= int(mΔλplusminute)
        Δλsecond= int(mΔλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
    elif all(ruleslong20): 
        print()
        mnewΔλplussecond = int(mΔλplussecond%60)
        mnewΔλplusminute = int(mΔλplusminute+(mΔλplussecond//60)) 
        Δλdegree= float(mΔλdegree)
        Δλminute= int(mnewΔλplusminute)
        Δλsecond= int(mnewΔλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
    elif all(ruleslong30):
        print()
        mnewΔλplussecond = int(mΔλplussecond%60)
        mnewΔλplusminute = int(mΔλplusminute+(mΔλplussecond//60))
        mdefinitiveΔλplusminute = int(mnewΔλplusminute%60)
        mnewΔλplusdegree = float(mpositiveornegativeΔλdegree*abs((absalongintdegree+absblongintdegree)+(mnewΔλplusminute//60)))
        Δλdegree= float(mnewΔλplusdegree)
        Δλminute= int(mdefinitiveΔλplusminute)
        Δλsecond= int(mnewΔλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond        
    elif all(ruleslong40):
        print()
        mdefinitiveΔλplusminute = int(mΔλplusminute%60)
        mnewΔλplusdegree = float(mpositiveornegativeΔλdegree*abs((absalongintdegree+absblongintdegree)+(mΔλplusminute//60))) 
        Δλdegree= float(mnewΔλplusdegree)
        Δλminute= int(mdefinitiveΔλplusminute)
        Δλsecond= int(mΔλplussecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond     
    elif all(ruleslong50):
        Δλdegree= float(mΔλdegree)
        Δλminute= int(mΔλminute)
        Δλsecond= int(mΔλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond       
    elif all(ruleslong60):
        mnewΔλsecond=int((absalongsecond+60)-absblongsecond)
        mdefinitiveΔλminute = int ((absalongminute-1)-absblongminute) 
        Δλdegree= float(mΔλdegree)
        Δλminute= int(mdefinitiveΔλminute)
        Δλsecond= int(mnewΔλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond    
    elif all(ruleslong70):
        mnewΔλsecond=int((absalongsecond+60)-absblongsecond)
        mdefinitiveΔλminute = int(((absalongminute+60-1)-absblongminute))
        mnewΔλdegree= float(mpositiveornegativeΔλdegree*abs((absalongintdegree-1)-absblongintdegree))
        Δλdegree= float(mnewΔλdegree)
        Δλminute= int(mdefinitiveΔλminute)
        Δλsecond= int(mnewΔλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond   
    elif all(ruleslong80):
        mdefinitiveΔλminute = int(((absalongminute+60)-absblongminute))
        mnewΔλdegree= float(mpositiveornegativeΔλdegree*abs((absalongintdegree-1)-absblongintdegree))
        Δλdegree= float(mnewΔλdegree)
        Δλminute= int(mdefinitiveΔλminute)
        Δλsecond= int(mabsΔλsecond)
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            absΔλminute=abs(int(Δλminute))
            absΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print ("Subtracting longitude (a in the direction of b) is equivalent to:")
            print (stringdegreezerodivision,(r"""°"""),absΔλminute,(r"""'"""),absΔλsecond,(r"""" """))
        return Δλdegree, absΔλminute, absΔλsecond, alongintdegree, alongminute, alongsecond, blongintdegree, blongminute, blongsecond  
# By definition, longitude cannot exceed 180°, so we must consider the complement obtained by subtracting 360° like long B - long A
def haversine_completionlong():
    # long A and abs
    callhaversine_longba= haversine_longba()
    alongintdegree = float(callhaversine_longba[0])
    alongminute = int(callhaversine_longba[1])
    alongsecond = int(callhaversine_longba[2])
    #########################################
    # λA and λB for "return"
    longaintdegree = float(callhaversine_longba[3])
    longaminute = int(callhaversine_longba[4])
    longasecond = int(callhaversine_longba[5])
    longbintdegree = float(callhaversine_longba[6])
    longbminute = int(callhaversine_longba[7])
    longbsecond = int(callhaversine_longba[8])
    #########################################
    absalongintdegree = abs (alongintdegree)
    absalongminute = abs (alongminute)
    absalongsecond = abs (alongsecond)
    # long B and abs
    blongintdegree = float("360")
    blongminute = int("0")
    blongsecond = int("0")
    absblongintdegree = abs (blongintdegree)
    absblongminute = abs (blongminute)
    absblongsecond = abs (blongsecond)
    # long second B-A 
    Δλsecond = float (absblongsecond - absalongsecond)
    absΔλsecond = abs(Δλsecond)
    # long minute B-A
    Δλminute = float (absblongminute - absalongminute)
    absΔλminute = abs(Δλminute) 
    # long degree 
    positiveornegativeΔλdegree= int(-(math.copysign(1, alongintdegree)))
    Δλdegree= float(positiveornegativeΔλdegree*abs(absblongintdegree-absalongintdegree))
    # For <= 179° longitude.
    ruleslong1= [alongintdegree>=0,alongintdegree<=179]
    # For >= -179° longitude.
    ruleslong2= [alongintdegree<=0,alongintdegree>=-179]
    # For = 180° longitude.
    ruleslong11= [alongintdegree==180,alongminute==0,alongsecond==0]
    # For = -180° longitude.
    ruleslong21= [alongintdegree==-180,alongminute==0,alongsecond==0]
    # In subtractions with values ​​with equal signs, a subtraction is performed
    ruleslong5= [alongintdegree>=float("180"), absblongsecond >= absalongsecond, absΔλsecond<=59, absblongminute>=absalongminute, absΔλsecond<=59]         
    ruleslong6= [alongintdegree>=float("180"), absblongsecond < absalongsecond, absblongminute>absalongminute]
    ruleslong7= [alongintdegree>=float("180"), absblongsecond < absalongsecond, absblongminute<=absalongminute]
    ruleslong8= [alongintdegree>=float("180"), absblongsecond >= absalongsecond, absΔλsecond <=59, absblongminute<absalongminute]
    ruleslong51= [alongintdegree<=float("-180"), absblongsecond >= absalongsecond, absΔλsecond<=59, absblongminute>=absalongminute, absΔλsecond<=59]         
    ruleslong61= [alongintdegree<=float("-180"), absblongsecond < absalongsecond, absblongminute>absalongminute]
    ruleslong71= [alongintdegree<=float("-180"), absblongsecond < absalongsecond, absblongminute<=absalongminute]
    ruleslong81= [alongintdegree<=float("-180"), absblongsecond >= absalongsecond, absΔλsecond <=59, absblongminute<absalongminute]
    # mathematical calculations      
    if all(ruleslong1):
        ruΔλdegree= float(alongintdegree)
        ruΔλminute= int(alongminute)
        ruΔλsecond= int(alongsecond)
        return ruΔλdegree, ruΔλminute, ruΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong2):
        ruΔλdegree= float(alongintdegree)
        ruΔλminute= int(alongminute)
        ruΔλsecond= int(alongsecond)
        return ruΔλdegree, ruΔλminute, ruΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong11):
        ruΔλdegree= float(alongintdegree)
        ruΔλminute= int(alongminute)
        ruΔλsecond= int(alongsecond)
        return ruΔλdegree, ruΔλminute, ruΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong21):
        ruΔλdegree= float(alongintdegree)
        ruΔλminute= int(alongminute)
        ruΔλsecond= int(alongsecond)
        return ruΔλdegree, ruΔλminute, ruΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong5):
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            return Δλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong6):
        newΔλsecond=int((absblongsecond+60)-absalongsecond)
        definitiveΔλminute = int ((absblongminute-1)-absalongminute)
        ruΔλdegree= float(Δλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(newΔλsecond)
        ruleszeronegative= [str(ruΔλdegree)==("-0.0")]
        ruleszeropositive= [str(ruΔλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(ruΔλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return ruΔλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond  
    elif all(ruleslong7):
        newΔλsecond=int((absblongsecond+60)-absalongsecond)
        definitiveΔλminute = int(((absblongminute+60-1)-absalongminute))
        newΔλdegree= float(positiveornegativeΔλdegree*abs((absblongintdegree-1)-absalongintdegree))
        ruΔλdegree= float(newΔλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(newΔλsecond)
        ruleszeronegative= [str(ruΔλdegree)==("-0.0")]
        ruleszeropositive= [str(ruΔλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(ruΔλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return ruΔλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong8):
        definitiveΔλminute = int(((absblongminute+60)-absalongminute))
        newΔλdegree= float(positiveornegativeΔλdegree*abs((absblongintdegree-1)-absalongintdegree))
        ruΔλdegree= float(newΔλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(absΔλsecond)
        ruleszeronegative= [str(ruΔλdegree)==("-0.0")]
        ruleszeropositive= [str(ruΔλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(ruΔλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return ruΔλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong51):
        ruleszeronegative= [str(Δλdegree)==("-0.0")]
        ruleszeropositive= [str(Δλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(Δλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            return Δλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong61):
        newΔλsecond=int((absblongsecond+60)-absalongsecond)
        definitiveΔλminute = int ((absblongminute-1)-absalongminute)
        ruΔλdegree= float(Δλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(newΔλsecond)
        ruleszeronegative= [str(ruΔλdegree)==("-0.0")]
        ruleszeropositive= [str(ruΔλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(ruΔλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return ruΔλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond  
    elif all(ruleslong71):
        newΔλsecond=int((absblongsecond+60)-absalongsecond)
        definitiveΔλminute = int(((absblongminute+60-1)-absalongminute))
        newΔλdegree= float(positiveornegativeΔλdegree*abs((absblongintdegree-1)-absalongintdegree))
        ruΔλdegree= float(newΔλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(newΔλsecond)
        ruleszeronegative= [str(ruΔλdegree)==("-0.0")]
        ruleszeropositive= [str(ruΔλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(ruΔλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return ruΔλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
    elif all(ruleslong81):
        definitiveΔλminute = int(((absblongminute+60)-absalongminute))
        newΔλdegree= float(positiveornegativeΔλdegree*abs((absblongintdegree-1)-absalongintdegree))
        ruΔλdegree= float(newΔλdegree)
        Δλminute= int(definitiveΔλminute)
        Δλsecond= int(absΔλsecond)
        ruleszeronegative= [str(ruΔλdegree)==("-0.0")]
        ruleszeropositive= [str(ruΔλdegree)==("0.0")]
        if all(ruleszeronegative): 
            intdegreezerodivision=float("-0")
            stringdegreezerodivision= str(r"""-0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        elif all (ruleszeropositive):
            intdegreezerodivision=float("0")
            stringdegreezerodivision= str(r"""0""")
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print(r"""-------------------------------------------------------------------------------------------------------------------------""")
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return intdegreezerodivision, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond
        else:
            stringdegreezerodivision= str(int(ruΔλdegree))
            intabsΔλminute=abs(int(Δλminute))
            intabsΔλsecond=abs(int(Δλsecond))
            print (r"""By definition, longitude cannot exceed 180°, so you must consider the complement obtained by subtracting 360°:""")
            print (stringdegreezerodivision,(r"""°"""),intabsΔλminute,(r"""'"""),intabsΔλsecond,(r"""" """))
            # intdegreezerodivision is a float
            return ruΔλdegree, intabsΔλminute, intabsΔλsecond, longaintdegree, longaminute, longasecond, longbintdegree, longbminute, longbsecond   
###############################################################################################################################################    
# It converts sexagesimal values of distances between coordinates (from "A" to "B"): Latitude Δφ=φB-φA; Longitude Δλ=λB-λA to radian.         #
# for inverse harversine formula                                                                                                              # 
############################################################################################################################################### 
# mathematical calculations
def lat_long_ba_in_radian():
    latba=checkzerohaversine_latba()
    longba=haversine_completionlong()
    degreeΔlatba=float(latba[0])
    minuteΔlatba=int(latba[1])
    secondΔlatba=int(latba[2])
    degree_lata=float(latba[3])
    minute_lata=int(latba[4])
    second_lata=int(latba[5])
    degree_latb=float(latba[6])
    minute_latb=int(latba[7])
    second_latb=int(latba[8])
    degreeΔlongba=float(longba[0])
    minuteΔlongba=int(longba[1])
    secondΔlongba=int(longba[2])
    degree_longa=float(longba[3])
    minute_longa=int(longba[4])
    second_longa=int(longba[5])
    degree_longb=float(longba[6])
    minute_longb=int(longba[7])
    second_longb=int(longba[8])
    # degreeΔlatba
    absfldegreeΔlatba=abs(degreeΔlatba)
    absdegreeΔlatba= abs (int(degreeΔlatba))
    # degree_lata
    absfldegree_lata=abs(degree_lata)
    absdegree_lata= abs (int(degree_lata))
    # degree_latb
    absfldegree_latb=abs(degree_latb)
    absdegree_latb= abs (int(degree_latb))
    # degreeΔlongba
    absfldegreeΔlongba=abs(degreeΔlongba)
    absdegreeΔlongba= abs (int(degreeΔlongba))
    # degree_longa
    absfldegree_longa=abs(degree_longa)
    absdegree_longa= abs (int(degree_longa))
    # degree_longb
    absfldegree_longb=abs(degree_longb)
    absdegree_longb= abs (int(degree_longb))    
    try :
        # degreeΔlatba, minuteΔlatba, secondΔlatba
        positive_or_negative_operator_of_degreeΔlatba= (degreeΔlatba/absfldegreeΔlatba)
        from_second_to_degreeΔlatba= secondΔlatba/3600
        from_minute_to_degreeΔlatba= minuteΔlatba/60
        decimaldegreeΔlatbavalue= float((positive_or_negative_operator_of_degreeΔlatba) * abs(absdegreeΔlatba + from_second_to_degreeΔlatba + from_minute_to_degreeΔlatba))
        pi_degreeΔlatba = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degreeΔlatba_in_radian = float (pi_degreeΔlatba/180)
        sexagesimal_values_of_degreeΔlatbas_in_radian= float(decimaldegreeΔlatbavalue * on_e_degreeΔlatba_in_radian)
        # degree_lata, minute_lata, second_lata
        positive_or_negative_operator_of_degree_lata= (degree_lata/absfldegree_lata)
        from_second_to_degree_lata= second_lata/3600
        from_minute_to_degree_lata= minute_lata/60
        decimaldegree_latavalue= float((positive_or_negative_operator_of_degree_lata) * abs(absdegree_lata + from_second_to_degree_lata + from_minute_to_degree_lata))
        pi_degree_lata = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_lata_in_radian = float (pi_degree_lata/180)
        sexagesimal_values_of_degree_latas_in_radian= float(decimaldegree_latavalue * on_e_degree_lata_in_radian)
        # degree_latb, minute_latb, second_latb
        positive_or_negative_operator_of_degree_latb= (degree_latb/absfldegree_latb)
        from_second_to_degree_latb= second_latb/3600
        from_minute_to_degree_latb= minute_latb/60
        decimaldegree_latbvalue= float((positive_or_negative_operator_of_degree_latb) * abs(absdegree_latb + from_second_to_degree_latb + from_minute_to_degree_latb))
        pi_degree_latb = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_latb_in_radian = float (pi_degree_latb/180)
        sexagesimal_values_of_degree_latbs_in_radian= float(decimaldegree_latbvalue * on_e_degree_latb_in_radian)
        # degreeΔlongba, minuteΔlongba, secondΔlongba
        positive_or_negative_operator_of_degreeΔlongba= (degreeΔlongba/absfldegreeΔlongba)
        from_second_to_degreeΔlongba= secondΔlongba/3600
        from_minute_to_degreeΔlongba= minuteΔlongba/60
        decimaldegreeΔlongbavalue= float((positive_or_negative_operator_of_degreeΔlongba) * abs(absdegreeΔlongba + from_second_to_degreeΔlongba + from_minute_to_degreeΔlongba))
        pi_degreeΔlongba = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degreeΔlongba_in_radian = float (pi_degreeΔlongba/180)
        sexagesimal_values_of_degreeΔlongbas_in_radian= float(decimaldegreeΔlongbavalue * on_e_degreeΔlongba_in_radian)
        # degree_longa, minute_longa, second_longa
        positive_or_negative_operator_of_degree_longa= (degree_longa/absfldegree_longa)
        from_second_to_degree_longa= second_longa/3600
        from_minute_to_degree_longa= minute_longa/60
        decimaldegree_longavalue= float((positive_or_negative_operator_of_degree_longa) * abs(absdegree_longa + from_second_to_degree_longa + from_minute_to_degree_longa))
        pi_degree_longa = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_longa_in_radian = float (pi_degree_longa/180)
        sexagesimal_values_of_degree_longas_in_radian= float(decimaldegree_longavalue * on_e_degree_longa_in_radian)
        # degree_longb, minute_longb, second_longb
        positive_or_negative_operator_of_degree_longb= (degree_longb/absfldegree_longb)
        from_second_to_degree_longb= second_longb/3600
        from_minute_to_degree_longb= minute_longb/60
        decimaldegree_longbvalue= float((positive_or_negative_operator_of_degree_longb) * abs(absdegree_longb + from_second_to_degree_longb + from_minute_to_degree_longb))
        pi_degree_longb = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_longb_in_radian = float (pi_degree_longb/180)
        sexagesimal_values_of_degree_longbs_in_radian= float(decimaldegree_longbvalue * on_e_degree_longb_in_radian)
        #######################################################
        return sexagesimal_values_of_degreeΔlatbas_in_radian, sexagesimal_values_of_degree_latas_in_radian, sexagesimal_values_of_degree_latbs_in_radian, sexagesimal_values_of_degreeΔlongbas_in_radian, sexagesimal_values_of_degree_longas_in_radian, sexagesimal_values_of_degree_longbs_in_radian, degreeΔlatba, minuteΔlatba, secondΔlatba, degree_lata, minute_lata, second_lata, degree_latb, minute_latb, second_latb, degreeΔlongba, minuteΔlongba, secondΔlongba, degree_longa, minute_longa, second_longa, degree_longb, minute_longb, second_longb  
    except (ZeroDivisionError):
        # degreeΔlatba, minuteΔlatba, secondΔlatba
        positive_or_negative_operator_of_degreeΔlatba= int(math.copysign(1, (degreeΔlatba)))
        from_second_to_degreeΔlatba= secondΔlatba/3600
        from_minute_to_degreeΔlatba= minuteΔlatba/60
        decimaldegreeΔlatbavalue= float((positive_or_negative_operator_of_degreeΔlatba) * abs(absdegreeΔlatba + from_second_to_degreeΔlatba + from_minute_to_degreeΔlatba))
        pi_degreeΔlatba = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degreeΔlatba_in_radian = float(pi_degreeΔlatba/180)
        sexagesimal_values_of_degreeΔlatbas_in_radian= float(decimaldegreeΔlatbavalue * on_e_degreeΔlatba_in_radian)
        # degree_lata, minute_lata, second_lata
        positive_or_negative_operator_of_degree_lata= int(math.copysign(1, (degree_lata)))
        from_second_to_degree_lata= second_lata/3600
        from_minute_to_degree_lata= minute_lata/60
        decimaldegree_latavalue= float((positive_or_negative_operator_of_degree_lata) * abs(absdegree_lata + from_second_to_degree_lata + from_minute_to_degree_lata))
        pi_degree_lata = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_lata_in_radian = float(pi_degree_lata/180)
        sexagesimal_values_of_degree_latas_in_radian= float(decimaldegree_latavalue * on_e_degree_lata_in_radian)
        # degree_latb, minute_latb, second_latb
        positive_or_negative_operator_of_degree_latb= int(math.copysign(1, (degree_latb)))
        from_second_to_degree_latb= second_latb/3600
        from_minute_to_degree_latb= minute_latb/60
        decimaldegree_latbvalue= float((positive_or_negative_operator_of_degree_latb) * abs(absdegree_latb + from_second_to_degree_latb + from_minute_to_degree_latb))
        pi_degree_latb = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_latb_in_radian = float(pi_degree_latb/180)
        sexagesimal_values_of_degree_latbs_in_radian= float(decimaldegree_latbvalue * on_e_degree_latb_in_radian)
        # degreeΔlongba, minuteΔlongba, secondΔlongba
        positive_or_negative_operator_of_degreeΔlongba= int(math.copysign(1, (degreeΔlongba)))
        from_second_to_degreeΔlongba= secondΔlongba/3600
        from_minute_to_degreeΔlongba= minuteΔlongba/60
        decimaldegreeΔlongbavalue= float((positive_or_negative_operator_of_degreeΔlongba) * abs(absdegreeΔlongba + from_second_to_degreeΔlongba + from_minute_to_degreeΔlongba))
        pi_degreeΔlongba = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degreeΔlongba_in_radian = float(pi_degreeΔlongba/180)
        sexagesimal_values_of_degreeΔlongbas_in_radian= float(decimaldegreeΔlongbavalue * on_e_degreeΔlongba_in_radian)
        # degree_longa, minute_longa, second_longa
        positive_or_negative_operator_of_degree_longa= int(math.copysign(1, (degree_longa)))
        from_second_to_degree_longa= second_longa/3600
        from_minute_to_degree_longa= minute_longa/60
        decimaldegree_longavalue= float((positive_or_negative_operator_of_degree_longa) * abs(absdegree_longa + from_second_to_degree_longa + from_minute_to_degree_longa))
        pi_degree_longa = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_longa_in_radian = float(pi_degree_longa/180)
        sexagesimal_values_of_degree_longas_in_radian= float(decimaldegree_longavalue * on_e_degree_longa_in_radian)
        # degree_longb, minute_longb, second_longb
        positive_or_negative_operator_of_degree_longb= int(math.copysign(1, (degree_longb)))
        from_second_to_degree_longb= second_longb/3600
        from_minute_to_degree_longb= minute_longb/60
        decimaldegree_longbvalue= float((positive_or_negative_operator_of_degree_longb) * abs(absdegree_longb + from_second_to_degree_longb + from_minute_to_degree_longb))
        pi_degree_longb = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
        on_e_degree_longb_in_radian = float(pi_degree_longb/180)
        sexagesimal_values_of_degree_longbs_in_radian= float(decimaldegree_longbvalue * on_e_degree_longb_in_radian)
        #######################################################
        return sexagesimal_values_of_degreeΔlatbas_in_radian, sexagesimal_values_of_degree_latas_in_radian, sexagesimal_values_of_degree_latbs_in_radian, sexagesimal_values_of_degreeΔlongbas_in_radian, sexagesimal_values_of_degree_longas_in_radian, sexagesimal_values_of_degree_longbs_in_radian, degreeΔlatba, minuteΔlatba, secondΔlatba, degree_lata, minute_lata, second_lata, degree_latb, minute_latb, second_latb, degreeΔlongba, minuteΔlongba, secondΔlongba, degree_longa, minute_longa, second_longa, degree_longb, minute_longb, second_longb  
# distance from inverse haverine formula (km and NM) 
def inverse_haversine_distances_between_coordinates():
    radian = lat_long_ba_in_radian()
    # conversion radian to decimal degree too (from floating_point_radians_conversion_in_floatpoint_degrees() function)
    ludolphianπ = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
    one_radian_in_floatpoint_degree = float(180/ludolphianπ)
    # conversion decimal degree to radian too (from floating_point_degree_conversion_in_radian() function)
    π = float(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
    one_degree_in_radian = float(π/180)
    degreeΔlatba_in_radian = radian[0]
    degreeΔlatba_in_radian_in_floatpoint_degree= float(degreeΔlatba_in_radian*one_radian_in_floatpoint_degree)
    degree_lata_in_radian = radian[1]
    degree_lata_in_radian_in_floatpoint_degree= float(degree_lata_in_radian*one_radian_in_floatpoint_degree)
    degree_latb_in_radian = radian[2]
    degree_latb_in_radian_in_floatpoint_degree= float(degree_latb_in_radian*one_radian_in_floatpoint_degree)
    degreeΔlongba_in_radian = radian[3]
    degreeΔlongba_in_radian_in_floatpoint_degree= float(degreeΔlongba_in_radian*one_radian_in_floatpoint_degree)
    degree_longa_in_radian = radian[4]
    degree_longa_in_radian_in_floatpoint_degree= float(degree_longa_in_radian*one_radian_in_floatpoint_degree)
    degree_longb_in_radian = radian[5]
    degree_longb_in_radian_in_floatpoint_degree= float(degree_longb_in_radian*one_radian_in_floatpoint_degree)
    degreeΔlatba= radian[6]
    # stringdegree_ : for python int(-0.0) = +0
    stringdegreeΔlatba=str(0) and degreeΔlatba==str(0.0) or str(-0) and degreeΔlatba==str(-0.0) or str(int(degreeΔlatba))
    minuteΔlatba= radian[7]
    secondΔlatba= radian[8]
    degree_lata= radian[9] 
    stringdegree_lata=str(0) and degree_lata==str(0.0) or str(-0) and degree_lata==str(-0.0) or str(int(degree_lata))
    minute_lata= radian[10]
    second_lata= radian[11]
    degree_latb= radian[12]
    stringdegree_latb=str(0) and degree_latb==str(0.0) or str(-0) and degree_latb==str(-0.0) or str(int(degree_latb))
    minute_latb= radian[13]
    second_latb= radian[14] 
    degreeΔlongba= radian[15]
    stringdegreeΔlongba=str(0) and degreeΔlongba==str(0.0) or str(-0) and degreeΔlongba==str(-0.0) or str(int(degreeΔlongba))
    minuteΔlongba= radian[16]
    secondΔlongba= radian[17]
    degree_longa= radian[18]
    stringdegree_longa=str(0) and degree_longa==str(0.0) or str(-0) and degree_longa==str(-0.0) or str(int(degree_longa))
    minute_longa= radian[19]
    second_longa= radian[20]
    degree_longb= radian[21]
    stringdegree_longb=str(0) and degree_longb==str(0.0) or str(-0) and degree_longb==str(-0.0) or str(int(degree_longb))
    minute_longb= radian[22]
    second_longb= radian[23]
    earthradius_km= float("6371")
    inversehaversineformula = float (2 * earthradius_km * math.asin(math.sqrt((pow(math.sin(degreeΔlatba_in_radian / 2), 2) + math.cos(degree_lata_in_radian) * math.cos(degree_latb_in_radian) * pow(math.sin(degreeΔlongba_in_radian / 2), 2)))))
    # conversion of inversehaversineformula in miles from floating_point_kilometres_conversion_in_floatpoint_miles() function
    fl_oatpointkilometres= float(inversehaversineformula)
    one_mile_in_kilometres = float(1.852)
    conversion_inversehaversineformula_kilometres_miles = float(fl_oatpointkilometres/one_mile_in_kilometres)
    print()
    time.sleep(3)
    print()
    print((r"""Δφ=φB-φA="""),str(degreeΔlatba_in_radian),(r"""rad or"""),str(degreeΔlatba_in_radian_in_floatpoint_degree),(r"""° or"""),stringdegreeΔlatba,(r"""°"""),str(minuteΔlatba),(r"""'"""),str(secondΔlatba),(r"""" """)) 
    print((r"""Δλ=λB-λA="""),str(degreeΔlongba_in_radian),(r"""rad or"""),str(degreeΔlongba_in_radian_in_floatpoint_degree),(r"""° or"""),stringdegreeΔlongba,(r"""°"""),str(minuteΔlongba),(r"""'"""),str(secondΔlongba),(r"""" """))
    print((r"""φA="""),str(degree_lata_in_radian),(r"""rad or"""),str(degree_lata_in_radian_in_floatpoint_degree),(r"""° or"""),stringdegree_lata,(r"""°"""),str(minute_lata),(r"""'"""),str(second_lata),(r"""" """))
    print((r"""λA="""),str(degree_longa_in_radian),(r"""rad or"""),str(degree_longa_in_radian_in_floatpoint_degree),(r"""° or"""),stringdegree_longa,(r"""°"""),str(minute_longa),(r"""'"""),str(second_longa),(r"""" """))
    print((r"""φB="""),str(degree_latb_in_radian),(r"""rad or"""),str(degree_latb_in_radian_in_floatpoint_degree),(r"""° or"""),stringdegree_latb,(r"""°"""),str(minute_latb),(r"""'"""),str(second_latb),(r"""" """))
    print((r"""λB="""),str(degree_longb_in_radian),(r"""rad or"""),str(degree_longb_in_radian_in_floatpoint_degree),(r"""° or"""),stringdegree_longb,(r"""°"""),str(minute_longb),(r"""'"""),str(second_longb),(r"""" """))     
    print((r"""Distances between coordinates (from "A" to "B") is"""),str(inversehaversineformula),(r"""km or"""),str(conversion_inversehaversineformula_kilometres_miles),(r"""NM"""))   
    print()
    print(r"""The distances between coordinates formula is not an exact measurement because the Inverse Haversine formula assumes that """)
    print(r"""the Earth is a perfect sphere, instead it is an oblate spheroid.""")
    print()
    print()
    time.sleep(3)
    print(r"""“All men dream: but not equally. Those who dream by night in the dusty recesses of their minds""") 
    print(r"""wake in the day to find that it was vanity: but the dreamers of the day are dangerous men, for""")
    print(r"""they may act their dreams with open eyes, to make it possible. This I did." """)
    print(r"""by T.E Lawrence "Lawrence of Arabia” """)
    print()
    print(r"""This python script was extracted from Antonio Bonaccorso's program called "Northern Lights" """) 
    print(r"""The name of this program is inspired by "Person of Interest" (an American science fiction crime drama""") 
    print(r"""television series created by Jonathan Nolan).""")
    print()
    print()
    time.sleep(3)
    print(r"""Although the intellectual property of this free program belongs to a third party, it supports the rescue""") 
    print(r"""activities of non-governmental organizations in the Mediterranean (and beyond) through word of mouth.""") 
    print(r"""It doesn't matter whether people speak well or poorly of the rescue activities of non-governmental organizations,""")
    print(r"""the important thing is that they are talked about.""")
    return degreeΔlatba_in_radian, degree_lata_in_radian, degree_latb_in_radian, degreeΔlongba_in_radian, degree_longa_in_radian, degree_longb_in_radian, inversehaversineformula, conversion_inversehaversineformula_kilometres_miles, degreeΔlatba, minuteΔlatba, secondΔlatba, degree_lata, minute_lata, second_lata, degree_latb, minute_latb, second_latb, degreeΔlongba, minuteΔlongba, secondΔlongba, degree_longa, minute_longa, second_longa, degree_longb, minute_longb, second_longb, degreeΔlatba_in_radian_in_floatpoint_degree, degree_lata_in_radian_in_floatpoint_degree, degree_latb_in_radian_in_floatpoint_degree, degreeΔlongba_in_radian_in_floatpoint_degree, degree_longa_in_radian_in_floatpoint_degree, degree_longb_in_radian_in_floatpoint_degree
# it calls inverse_haversine_distances_between_coordinates() function
def formula_inverse_haversine_distances_between_coordinates():
     
    print(r"""-------------------------------------------------------------------------------------------------------------------------""")
    print(r"""FORMULA OF INVERSE HAVERSINE""")
    print(r"""by Antonio Bonaccorso with CC BY-NC-SA 4.0""")
    print(r"""-------------------------------------------------------------------------------------------------------------------------""")
    print(r"""Distances between coordinates (from "A" to "B"): Latitude Δφ=φB-φA; Longitude Δλ=λB-λA""")
    print(r"""if Δφ is positive you go to NORTH; if Δφ is negative you go to SOUTH;""")
    print(r"""if Δλ is positive you go to EAST; if Δλ is negative you go to WEST""")
    print(r"""The Inverse Haversine formula calculates the shortest distance between two points on a sphere using their latitudes and""") 
    print(r"""longitudes measured along the surface. The conventional radius of the earth is 6371 km.""")
    print(r"""-------------------------------------------------------------------------------------------------------------------------""")
    print()
    inverse_haversine_distances_between_coordinates()
    time.sleep(3)
    print()
 
formula_inverse_haversine_distances_between_coordinates()
