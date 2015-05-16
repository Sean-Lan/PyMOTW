#!/usr/bin/env python
from Queue import Queue
from threading import Thread
import time

num_of_thread = 3
queue = Queue()

class Task:
    def __init__(self, description):
        self.description = description


def performTasks(i, q):
    while True:
        print '%s: Looking for the next task' % i
        task = q.get()          # Block when q is empty()
        print '%s: Task description:' % i, task.description 
        time.sleep(5)           # Performing tasks takes time
        q.task_done()


for i in range(num_of_thread):
    worker = Thread(target=performTasks, args=(i, queue))
    # When the main thread exits, kill all the subthread with property daemon true.
    worker.setDaemon(True) 
    worker.start()

tasks = [ Task('Finish the paper'),
          Task('Welcome the foreign guy'),
          Task('Read the books'),
          Task('Work Out'),
        ]

for task in tasks:
    print 'Queuing:', task.description
    queue.put(task)             # Mimic the tasks coming at different time
    time.sleep(3)

print '*** Main threading waiting'
queue.join()                    # Wait all tasks done
print '** Done'
