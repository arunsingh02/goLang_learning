import time

def aa():
    t_end = time.time() + 12
    print(t_end)
    while time.time() < t_end:
        print(f'HIIII {time.time()} ')
        time.sleep(10)

aa()
