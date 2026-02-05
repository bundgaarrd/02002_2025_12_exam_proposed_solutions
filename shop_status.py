# Opgave 10 (Shop Status)

# Needs refactoring

def shop_status(day, hour):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    open_hour = 9
    close_hour = 17
    open_status = False
    for i in range(len(days)):
        if (day == days[i]):
            # If open
            if (i < 5) and (open_hour <= hour < close_hour):
                open_status = True
                return (open_status, days[i], close_hour)
            # If closed
            elif (i < 5) and not(open_hour <= hour < close_hour):
                open_status = False
                return (open_status, days[i+1], open_hour)
            # If weekend and closed
            else:
                open_status = False
                return (open_status, days[0], open_hour)