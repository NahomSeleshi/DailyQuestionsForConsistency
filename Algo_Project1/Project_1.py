import math
import time

def algorithm9(n):
    j = 2
    while (j < n):
        k = j
        while (k < n):
            k = k*k
        j += math.log10(k)

start = time.perf_counter()
algorithm9(1000000)
end = time.perf_counter()
print(f"{end - start:0.10f}")