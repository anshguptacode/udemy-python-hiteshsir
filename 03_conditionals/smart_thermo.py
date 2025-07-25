device_status="active"
temprature =99
if device_status=="active":
    if temprature>35:
        print("HIgh Temprature")
    else:
        print("Temprature is Normal")
else:
    print("device is offline")
