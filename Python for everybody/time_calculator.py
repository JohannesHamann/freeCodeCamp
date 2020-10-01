def add_time(start, duration, day= None):
    # setting up lookup tables in both directions
    AM_PM_dic = {"AM":0 , "PM":1}
    AM_PM_keys_list = list(AM_PM_dic.keys())
    AM_PM_value_list = list(AM_PM_dic.values())
    days_dic = {"monday":0 , "tuesday":1 , "wednesday":2 , "thursday":3 , "friday":4 , "saturday":5 , "sunday":6}
    days_dic_key_list = list(days_dic.keys())
    days_dic_value_list = list(days_dic.values())
    # extracting information from arguments
    eingabe = start.split()
    zeit = eingabe[0].split(":")
    hours_start = int(zeit[0])
    minutes_start = int(zeit[1])
    AM_PM_start = AM_PM_dic[eingabe[1]]
    if day != None:
        day_start = days_dic[day.lower()]
    # extracing information from "duration"
    zeit_add = duration.split(":")
    hours_add = int(zeit_add[0])
    minutes_add = int(zeit_add[1])
    # implementing calculation formula
    minutes_after_addition = divmod(minutes_start + minutes_add, 60)
    
    hours_after_addition = divmod(hours_start + hours_add + minutes_after_addition[0]  , 12)
    hours_result = hours_after_addition[1]
    if hours_after_addition[1] == 0:  
        # so that there is 12:04 AM and not 00:04 AM
        hours_result = 12
    full_12_cicles = hours_after_addition[0]
    minutes_result = str(minutes_after_addition[1]).zfill(2)


    # -------> durchs modden oben bekommt man zeiten 00:04 AM statt 12:04 AM , dies muss behoben werden

    AM_PM_result = AM_PM_keys_list[AM_PM_value_list.index((AM_PM_start+full_12_cicles)%2)]
    full_days_later = (full_12_cicles + AM_PM_start)//2


    # --------> hier muss unterteilt werden in eine Darstellung falls day != None und falls day == None ist und nicht so kreuz und quer wie gerade
    if day != None and full_days_later != 0:
        day_result = days_dic_key_list[days_dic_value_list.index((day_start + full_days_later)%7)].capitalize()
        new_time = str(hours_result) +  ":" + minutes_result + " " + AM_PM_result + ", " + day_result + " (" + str(full_days_later) +" days later" +")"
    if full_days_later ==1:
        new_time = str(hours_result) +  ":" + minutes_result + " " + AM_PM_result + " (next day)"
    if full_days_later == 0:
        new_time = str(hours_result) +  ":" + minutes_result + " " + AM_PM_result
    elif full_days_later > 1 and day == None:
        new_time = str(hours_result) +  ":" + minutes_result + " " + AM_PM_result + " (" + str(full_days_later) +" days later" +")"
    return new_time

print ( add_time("12:16 PM", "23:46", "tuesday"))

