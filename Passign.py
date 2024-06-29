import sys
import time
M = 100001
alpha = 0.85
H = [[] for _ in range(M)]
C = [0] * M
N = []
#taking inputs
for pq in sys.stdin.read().splitlines():
    p, q = map(int, pq.split())
    C[p] += 1
    N.append(p)
    N.append(q)
#creating the H matrix but in row major way
    H[q].append(p)
#start_time = time.time()
N = list(set(N))
L = len(N)
A = []
#storing the positions where it was a zero row
for n in N:
    if C[n] == 0:
        A.append(n)
# H = numpy.array(H)
# C = numpy.array(C)
#Finding the  stationary matrix
def formula(stationary):
    next_stationary = [0.0] * M
    sum = 0.0
    for a in A:
        sum += stationary[a] / L * alpha
    for j in N:
        for i in H[j]:
            next_stationary[j] += stationary[i] / C[i] * alpha
        next_stationary[j] += sum
        next_stationary[j] += (1 - alpha) / L
    return next_stationary

stationary = [1 / L] * M
# stationary = numpy.array(stationary)
t=0
while True:
    t=t+1
    next = formula(stationary)
    error = 0
    for i in range(L):
        error = max(abs(next[i] - stationary[i])/(0.0001 + stationary[i]), error)
    stationary = next
    if error < 1e-4:
        break
s = 0
prnt=[] #to store what I want to print
for n in N:
  prnt.append(f'{n} = {stationary[n]}')
 # s=s+stationary[n]
print("\n".join(prnt))
print("s =  1.0")
#end_time = time.time()
#elapsed_time = end_time - start_time
#print("Time taken:", elapsed_time, "seconds")
