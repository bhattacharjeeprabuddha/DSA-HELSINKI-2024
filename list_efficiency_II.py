import time

nums = []

def test_addition(n:int=10**5):
    start_time = time.time()
    for i in range(1, n+1):
        nums.append(i)
    end_time = time.time()
    return end_time - start_time

print(test_addition())

def test_deletion(n:int=10**5):
    start_time = time.time()
    for i in range(n):
        nums.pop(0)
    end_time = time.time()
    return end_time - start_time

print(test_deletion())



    


