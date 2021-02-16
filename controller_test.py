import xbox


joy = xbox.Joystick()
while True:
        
    if joy.A():
        print("hi")
