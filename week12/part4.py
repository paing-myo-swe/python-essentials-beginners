import time
import datetime

def sayHello():
    print('Hello World')


start = time.perf_counter()
sayHello()
end = time.perf_counter()

print("Execution time", end - start)

given_date = datetime.datetime(2023, 12, 25)
print(given_date.strftime('%A'))