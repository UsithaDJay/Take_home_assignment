import json
import datetime

def get_free_slots(file_name):
    # Reading the JSON file
    with open(file_name, 'r') as file:
        data = json.load(file)

    # Extracting the start and end times of events
    event_times = [(datetime.datetime.fromisoformat(event["start"]["dateTime"]).strftime('%Y-%m-%d %H:%M:%S'), 
                    datetime.datetime.fromisoformat(event["end"]["dateTime"]).strftime('%Y-%m-%d %H:%M:%S')) 
                   for event in data]
    
    
    
    # Sorting the events by their start times
    event_times.sort(key=lambda x: x[0])

    for time in event_times:
        print(time)

    # Define a starting time for a day (e.g., 00:00) and an ending time for a day (e.g., 23:59)
    day_start = event_times[0][0].split()[0] + " 00:00:00"
    day_end = event_times[-1][0].split()[0] + " 23:59:59"

    print(day_start)
    print(day_end)
    # Finding the free slots
    free_slots = []

    # Starting with the first possible free slot
    current_time = day_start

    for start, end in event_times:
        # If there's a gap between the current time and the next event's start time, we have a free slot
        if current_time < start:
            free_slots.append({
                "start_time": current_time,
                "end_time": start
            })
        # Updating the current time to the end of the event we just checked
        current_time = end

    # Checking for any remaining free time after the last event
    if current_time < day_end:
        free_slots.append({
            "start_time": current_time,
            "end_time": day_end
        })

    return free_slots

# Get free slots from the JSON file
file_name = "events.json"
free_slots = get_free_slots(file_name)
print(free_slots)

# Writing the free slots to a JSON file
result = {}

for entry in free_slots:
    date = entry['start_time'].split(' ')[0]
    start_time = entry['start_time'].split(' ')[1]
    end_time = entry['end_time'].split(' ')[1]

    if date not in result:
        result[date] = []

    result[date].append({'start_time': start_time, 'end_time': end_time})

with open('output.json', 'w') as f:
    json.dump(result, f, indent=2)

