# import threading
# import signal
# import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# # Function to be executed when a signal is received
# def signal_handler(sig, frame):
#     print(f"Received signal {sig}")

# # Register signal handlers in the main thread
# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

# # Function to be run in a separate thread
# def thread_function():
#     while True:
#         time.sleep(1)

# # Create and start the thread
# worker_thread = threading.Thread(target=thread_function)
# worker_thread.start()

# # Keep the main thread alive
# while True:
#     try:
#         time.sleep(1)
#     except KeyboardInterrupt:
#         break

# # Wait for the worker thread to finish
# worker_thread.join()