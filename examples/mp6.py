# SuperFastPython.com
# example of extending the Process class
from time import sleep
from multiprocessing import Process
 
# custom process class
class CustomProcess(Process):
    # override the run function
    def run(self):
        print("Start of task function.")
        sleep(1)
        print('This is coming from another process')
        print("End of task function.")
 
# entry point
if __name__ == '__main__':
    process = CustomProcess()
    process.start()
    print('Waiting for the process to finish...')
    process.join()
    print('Process completed.')
    print('Exiting program.')