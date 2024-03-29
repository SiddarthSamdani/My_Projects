from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os 
import json 
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = r"C:\Users\Siddarth\Desktop\My_Projects\MyFolder_1"
folder_destination = r"C:\Users\Siddarth\Desktop\My_Projects\MyFolder_2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()