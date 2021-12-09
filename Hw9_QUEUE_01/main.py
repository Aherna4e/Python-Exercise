#Name: Alejandra Hernandez
#Date: 11/18/2020
#Desc: PriorityQueue uses the sort order of the contents of the queue to decide which to retrieve.'''

#https://pymotw.com/2/Queue/

import Queue

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()

q.put( Job(3, 'Mid-level job') )
q.put( Job(10, 'Low-level job') )
q.put( Job(1, 'Important job') )

while not q.empty():
    next_job = q.get()
    print('Processing job:', next_job.description)