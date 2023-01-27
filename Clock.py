import time

def clock_mech():
    global sec_start, sec_end, min_start, hour_start, days
    sec_start = 0; sec_end = 60; min_start = 0; hour_start = 0; days = 0

    while True:
        sec_start = sec_start + 1
        time.sleep(1)
        
        if sec_start == 60:
            sec_start = 0
            min_start += 1

        if min_start == 60:
            min_start = 0
            hour_start += 1

        if hour_start == 24:
            hour_start = 0
            days += 1

        print("It is " + str(days) + " days " + str(hour_start) + " hours " + str(min_start) + " minutes and " + str(sec_start) + " seconds!")

clock_mech()


    
    
