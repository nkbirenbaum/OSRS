# SuperFastPython.com
# example of running a function with arguments in another process
from time import sleep
from multiprocessing import Process
 
# a custom function that blocks for a moment
def task(sleep_time, message):
    print("Start of task function.")
    sleep(sleep_time)
    print(message)
    print("End of task function.")
 
# entry point
if __name__ == '__main__':
    process = Process(target=task, args=(1.5, 'New message from another process'))
    process.start()
    print('Waiting for the process to finish...')
    process.join()
    print('Process completed.')
    print('Exiting program.')