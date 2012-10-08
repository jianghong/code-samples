from priorityqueue import PriorityQueue as Pqueue

class P():
    ''' Item suitable for enqueueing. '''
    def __init__(self, priority, name='u'):
	  self.priority = priority
	  self.name = name

    def get_priority(self):
	  return self.priority

    def __str__(self):
	  return self.name

if __name__ == '__main__':
    def time_tester():
	  import random
	  from time import time
	  bl = 10000
	  output = ''
	  for input in [
		bl,
		bl * 2,
		bl * 4,
		bl * 8,
		bl * 16,
		bl * 32,
		bl * 64]:
		
		output += '%s\t|' % (input)
		L = []
		for i in xrange(input):
		    L.append(P(random.randint(1,20)))
		a = time()
		pq = Pqueue(L)
		output += '\t%s' % (time() - a)

		b = time()
		for i in xrange(pq.size()):
		    pq.dequeue()
		output += '\t%s\n' % (time() - b)
	  return output

    def output_verification():
	  o1 = P(1, 'a')
	  o2 = P(1, 'b')
	  o3 = P(2, 'c')
	  o4 = P(3, 'd')
	  o5 = P(4, 'e')
	  o6 = P(2, 'f')
	  l = [o1, o2, o3, o4, o5, o6]
	  pq = Pqueue(l)
	  # Order should be: abcfde
	  return pq


    ##########################################
    def to_log():
	  log_msg = ''
	  log_msg += time_tester()
	  log_msg += str(output_verification()) + '\n'
	  f = open('timings.txt','a')
	  f.write('-------\n' + log_msg)
	  f.close()
    ##########################################
    
    to_log()
