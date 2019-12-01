#Task: Memoization of a f of type int -> int
#
#Solution: Memoization class stores result in hash table. 
#        : FIFO queue used to limit hashtable size 
#        : O(1) Complexity 

class memo:

    def __init__(self, f):
        self.f = f
        self.hashtbl = {}
        self.queue = list()

    def __call__(self, *args):
        if args not in self.hashtbl:
            self.dequeue()
            self.hashtbl[args] = self.f(*args)
            self.enqueue(*args)
        return self.hashtbl[args]

    def enqueue(self,item):
        if item not in self.queue:
            self.queue.insert(0,item)
            return True
        return False
    
    def dequeue(self):
        if len(self.queue) > 100:
            del self.hashtbl[self.queue.get()]
            return True
        return False


@memo
def function(n):
    return (24 * 6)^n


print(function(4))
