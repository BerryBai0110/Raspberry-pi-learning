import time

with open("demand.csv", "r") as f:
    data = f.readlines()

data = [int(x.strip()) for x in data if x.strip() != ""]

while True:
    for demand in data:
        print("Current demand:", demand)

        if demand > 50:
            print("High demand → turn ON lights")
        else:
            print("Low demand → turn OFF lights")

        print("-----")
        time.sleep(2)
