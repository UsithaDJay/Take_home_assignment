from scheduler import Scheduler
from fileHandler import FileHandler

def main():
    # Read events from the JSON file
    file_name = "events.json"
    data = FileHandler.read_from_file(file_name)
    
    scheduler = Scheduler()
    scheduler.add_events_from_data(data)
    
    free_slots = scheduler.get_free_slots()
    print(free_slots)
    result = scheduler.format_free_slots(free_slots)
    # print(result)
    FileHandler.write_to_file(result, 'output.json')

if __name__ == "__main__":
    main()