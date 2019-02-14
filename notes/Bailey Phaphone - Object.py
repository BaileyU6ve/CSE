class Mouse(object):
    def __init__(self, brand):
        self.USB = True
        self.battery = True
        self.sensor = 1
        self.scroll_wheel = 1
        self.brand = brand

    def use_mouse(self):
        if not self.USB:
            print("Your mouse doesn't work.")
            print("It's not plugged in.")


my_phone = Mouse("Logitech")
