from playwright.sync_api import sync_playwright



class PlayWright:
    _playwright = None
    _context = None
    _browser = None

    def __new__(cls):
        if cls._playwright is None:
            cls._playwright = sync_playwright().start()



    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()



class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # cls._instance = Singleton()
        return cls._instance

    def cal(self, num1, num2):
        return num1+num2


instance1 = Singleton()
instance2 = Singleton()
instance3 = Singleton()

# instance1.cal(1,2)
print(str(instance1)+" "+str(instance3)+" "+str(instance2))
print(instance1 is instance2 is instance3)
