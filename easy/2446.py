from datetime import datetime

def haveConflict(e1, e2):
    time_obj1 = datetime.strptime(e1[1], "%H:%M").time()
    time_obj2 = datetime.strptime(e2[0], "%H:%M").time()
    return time_obj1 <= time_obj2

print(haveConflict(["01:15", "02:00"], ["02:00", "03:00"]))
