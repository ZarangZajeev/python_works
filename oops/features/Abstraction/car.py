from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelarate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Swift(Car):

    def start(self):
        print("Swift car Starts")

    def accelarate(self):
        print("Swift car Accearates")

    def stop(self):
        print("Swif car stops")

obj=Swift()
obj.start()
obj.accelarate()