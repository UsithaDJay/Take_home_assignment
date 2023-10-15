import datetime
from event import Event

class Scheduler:
    def __init__(self):
        self.events = []

    def add_event(self, start, end):
        event = Event(start, end)
        self.events.append(event)

    def add_events_from_data(self, data):
        for event_data in data:
            start = datetime.datetime.fromisoformat(event_data["start"]["dateTime"]).strftime('%Y-%m-%d %H:%M:%S')
            end = datetime.datetime.fromisoformat(event_data["end"]["dateTime"]).strftime('%Y-%m-%d %H:%M:%S')
            self.add_event(start, end)

    def sort_events(self):
        self.events.sort(key=lambda event: event.start_time)

    def get_free_slots(self):
        # Sort the events by start time
        self.sort_events()
        free_slots = []

        current_time = self.events[0].start_time.split()[0] + " 00:00:00"
        last_event_end = self.events[-1].end_time

        while current_time.split()[0] <= last_event_end.split()[0]:
            # If there's an event for the current day, we process it
            if self.events and current_time.split()[0] == self.events[0].start_time.split()[0]:
                for event in list(self.events):  # Loop through a copy of the list
                    if current_time.split()[0] != event.start_time.split()[0]:
                        # Next event is on a different day, so break out of the loop
                        break
                    
                    if current_time < event.start_time:
                        free_slots.append({
                            "start_time": current_time,
                            "end_time": event.start_time
                        })

                    current_time = event.end_time
                    self.events.remove(event)  # Remove the event as it's already processed

                # For the time after the last event on this day
                if current_time.split()[1] != "23:59:59":
                    free_slots.append({
                        "start_time": current_time,
                        "end_time": current_time.split()[0] + " 23:59:59"
                    })
                    current_time = (datetime.datetime.fromisoformat(current_time) + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
                else:
                    current_time = (datetime.datetime.fromisoformat(current_time) + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
            
            # If no event for the current day, we add the whole day as a free slot
            else:
                free_slots.append({
                    "start_time": current_time,
                    "end_time": current_time.split()[0] + " 23:59:59"
                })
                current_time = (datetime.datetime.fromisoformat(current_time) + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')

        return free_slots



    def format_free_slots(self, free_slots):
        result = {}
        for entry in free_slots:
            date = entry['start_time'].split(' ')[0]
            start_time = entry['start_time'].split(' ')[1]
            end_time = entry['end_time'].split(' ')[1]
            if date not in result:
                result[date] = []
            result[date].append({'start_time': start_time, 'end_time': end_time})
        return result