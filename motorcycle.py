import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"
    bike["engine_size"] = 250
    for key in bike:
        print(key)

    print(bike["make"])
    print(bike["engine_size"])

