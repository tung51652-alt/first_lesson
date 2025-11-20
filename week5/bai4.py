schedule = []


def create_event(*event):
    e = {'name': event[0], 'day':event[1], 'time': event[2]}
    return e

def add_event(event):
    schedule.append(event)

def find_by_day(day):
    for i in schedule:
        if(i['day'] == day):
            print(i)

def remove_event(event):
    for i in schedule:
        if(i['name'] == event):
            schedule.remove(i)

def export_schedule():
    for i in schedule:
        print(f"{i['day']:<5}{i['time']:>10}-{i['name']:>15}")

add_event(create_event('math', 'tuesday', '9:00'))
add_event(create_event('english', 'monday', '19:00'))
add_event(create_event('law', 'thursday', '7:00'))
remove_event('math')
export_schedule()
find_by_day('monday')
