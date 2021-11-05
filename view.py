#!/usr/bin/python3
import threading
import time
import PySimpleGUI as sg
import urllib
import urllib.request
from win10toast import ToastNotifier
n = ToastNotifier()
"""
    DESIGN PATTERN - Multithreaded Long Tasks GUI
    Presents one method for running long-running operations in a PySimpleGUI environment.
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    The "long work" is contained in the thread that is being started.
    July 2020 - Note that this program has been updated to use the new Window.write_event_value method.
    This method has not yet been ported to the other PySimpleGUI ports and is thus limited to the tkinter ports for now.

    Internally to PySimpleGUI, a queue.Queue is used by the threads to communicate with main GUI code
    The PySimpleGUI code is structured just like a typical PySimpleGUI program.  A layout defined,
        a Window is created, and an event loop is executed.
    This design pattern works for all of the flavors of PySimpleGUI including the Web and also repl.it
    You'll find a repl.it version here: https://repl.it/@PySimpleGUI/Async-With-Queue-Communicationspy
"""
from model import process_url

def long_operation_thread(seconds, window):
    """
    A worker thread that communicates with the GUI through a queue
    This thread can block for as long as it wants and the GUI will not be affected
    :param seconds: (int) How long to sleep, the ultimate blocking call
    :param gui_queue: (queue.Queue) Queue to communicate back to GUI that task is completed
    :return:
    """
    print('Starting thread - will sleep for {} seconds'.format(seconds))
    time.sleep(seconds)  # sleep for a while
    window.write_event_value('-THREAD-', '** DONE **')  # put a message into queue for GUI

def the_gui():
    """
    Starts and executes the GUI
    Reads data from a Queue and displays the data to the window
    Returns when the user exits / closes the window
    """
    sg.theme('Light Brown 3')

    layout = [[sg.Text('Enter a URL to get a synopsis')],
              [sg.Output(size=(80, 30))],
              [sg.Text('Craigslist Url '),
               sg.Input(key='-CRAIGURL-', size=(50, 1)),
               sg.Button('Analyze listing', bind_return_key=True)],
              [sg.Button('Click Me to Make it Go Faster'), sg.Button('Exit')], ]

    window = sg.Window('Craigslist Helper', layout)

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event.startswith('Analyze'):
            print('Processing listing...please wait.')
            threading.Thread(target=process_url, args=(values['-CRAIGURL-'], window), daemon=True).start()
        elif event == 'Click Me to Make it Go Faster':
            threading.Thread(target=n.show_toast, args=("Patience", "is also a form of action."), kwargs={"duration": 20}, \
                                                                                                daemon=True).start()
        elif event == '-THREAD-':
            print('', values[event])

    # if user exits the window, then close the window and exit the GUI func
    window.close()


