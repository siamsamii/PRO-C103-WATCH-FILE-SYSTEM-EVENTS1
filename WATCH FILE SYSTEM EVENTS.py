import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):
    """
    Handles file system events (creation, modification, movement, deletion).
    """

    def __init__(self):
      
        self.from_dir = "<Enter the path to the directory you want to monitor>"


        self.event_handler = self
        self.observer = Observer()

        # Schedule watching the specified directory
        self.observer.schedule(self.event_handler, self.from_dir, recursive=True)

        # Start the observer thread
        self.observer.start()

        print("Monitoring directory:", self.from_dir)

    def on_created(self, event):
        print(f"New file created: {event.src_path}")

    def on_modified(self, event):
        print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        print(f"File moved: {event.src_path} -> {event.dest_path}")

    def on_deleted(self, event):
        print(f"File deleted: {event.src_path}")

    def stop(self):
        """
        Stops the observer thread when called.
        """
        try:
            print("\nPress any key to stop...")
            sys.stdin.read(1)  # Read a single character from standard input
        except KeyboardInterrupt:
            print("\nStopping observer...")

        self.observer.stop()