class Mouse(object):
    def __init__(self, brand):
        self.USB = True
        self.battery = 100
        self.sensor = 1
        self.scroll_wheel = 1
        self.brand = brand

    def use_mouse(self):
        if not self.USB:
            print("Your mouse doesn't work.")
            print("It's not plugged in.")
            return
        if self.battery == 0:
            print("Better go change the batteries.")
            return

    def unplug_mouse(self):
        print("Can I see your mouse?")
        print("Oops. It's gone.")
        self.USB = False


my_mouse = Mouse("Logitech")
your_mouse = Mouse("Alien")

my_mouse.use_mouse()
your_mouse.unplug_mouse()
