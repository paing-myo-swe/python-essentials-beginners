import time

def sayHello():
    print('Hello World')


start = time.perf_counter()
sayHello()
end = time.perf_counter()

print("Execution time", end - start)
    