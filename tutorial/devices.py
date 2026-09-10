readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]
def list_devices(devices):
    for device in devices:
        print(f"{device['name']}: {device['temp']}")

list_devices(readings)

def average_temp(devices):
    return sum(device['temp'] for device in devices) / len(devices)

print(average_temp(readings))

def hottest_device(devices):
    return max(devices, key=lambda device: device['temp'])

print(hottest_device(readings))

def to_status(device):
    if device["online"]:
        status = "ok"
    else:
        status = "offline"
    return{
        "device": device["name"],
        "status": status,
        "celcius": device["temp"],
    }
print(to_status(readings[3]))

def by_room(devices):
    room_dict = {}
    for device in devices:
        room = device["room"]
        if room not in room_dict:
            room_dict[room] = []
        room_dict[room].append(device["name"])
    return room_dict

print(by_room(readings))