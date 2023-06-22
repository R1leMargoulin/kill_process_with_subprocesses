import subprocess as sub
import signal
import os
import time

def kill_process_and_sub(process):
    pids = [process.pid] #we create a list to put all the pid here
    for l in sub.check_output(["pgrep", "-P",str(process.pid)]).split(b'\n'): #we catch all the PIDs of the subprocess to put them in the pids list
        #print(l)
        if(l != b''):
            pids.append(int(float(l)))
    for pid in pids: #foreach pids we kill the associated process
        print("killing "+str(pid))
        os.kill(pid, signal.SIGTERM)
        
        
#---MAIN---
if __name__ == '__main__':
    proc = sub.Popen(["COMMAND", "ARG1", "ARG2", "..."])#CHANGE THIS COMMAND PARAMETERS
    time.sleep(5)
    kill_process_and_sub(proc)
  
