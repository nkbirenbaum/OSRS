# SuperFastPython.com
# example of running a function in another process
from time import sleep
from multiprocessing import Process
 
# a custom function that blocks for a moment
def task():
    print("Start of task.")
    sleep(1)
    print('End of task.')
 
# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task)
    # run the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process to finish...')
    process.join()
    print('Process completed.')