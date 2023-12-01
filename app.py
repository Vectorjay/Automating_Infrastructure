import threading
import queue
import time
from flask import Flask, render_template

socketio = Flask(__name__)

@socketio.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(debug=True)

# Create a queue instance for communication between threads
message_queue = queue.Queue()

# Function to be run in a separate thread
def thread_function():
    while True:
        # Check if there's a message in the queue
        if not message_queue.empty():
            message = message_queue.get()
            print(f"Received message: {message}")
        time.sleep(1)

# Create and start the thread
worker_thread = threading.Thread(target=thread_function)
worker_thread.start()

# Main thread sending messages to the worker thread
for i in range(5):
    message = f"Message {i+1}"
    message_queue.put(message)
    print(f"Sent: {message}")
    time.sleep(2)

# Wait for the worker thread to finish
worker_thread.join()