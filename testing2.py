import subprocess
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import signal

# Path to the txt file to monitor
applio=__file__.replace(os.path.basename(__file__),"")
applio=applio.replace("\\","/")
applio=applio + "run-applio.bat"
audio=__file__.replace(os.path.basename(__file__),"")
audio=audio.replace("\\","/")
audio=audio+"assets/audios/tts_rvc_output.wav"

# Global variable to track the batch process
process = None

# Event handler class to monitor file changes
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global process
        # Check if the modified file is the one we're monitoring
        if event.src_path == audio:
            print(f'{audio} has been modified. Stopping the batch file...')
            stop_batch_file()
            observer.stop()

def stop_batch_file():
    global process
    if process:
        print("Terminating the batch file...")
        try:
            # Attempt to terminate the batch file process
            process.terminate()
            process.wait()  # Ensure the process terminates properly
            print("Batch file stopped.")
        except Exception as e:
            print(f"Error stopping batch file: {e}")
        process = None

def start_batch_file():
    global process
    print(f'Starting the batch file: {applio}')
    process = subprocess.Popen(applio, shell=True)
    # Give it a moment to start
    time.sleep(1)

# Set up file change monitoring
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)  # Monitor current directory

# Start monitoring
observer.start()

# Start the batch file
start_batch_file()

# Keep the script running while monitoring the file
try:
    while process and process.poll() is None:  # Continue running while the batch file is active
        time.sleep(1)  # Just wait for the file to be modified
except KeyboardInterrupt:
    print("Process interrupted.")
finally:
    observer.stop()
    observer.join()

print("Done.")