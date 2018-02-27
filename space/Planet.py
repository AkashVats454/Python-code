class Planet:

    shape = 'round'    # Class level attribute

    def __init__(self, name, radius, gravity, system):
        self.name = name   #Instance attribute
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in {self.system}'

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'planets rotates at the {speed}'



hoth = Planet('Hoth',200000, 5.5, 'Hoth System')
# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'The Gravity is: {hoth.gravity}')
# print(hoth.orbit())
# print(hoth.shape)

planetXR = Planet('Naboo', 300000, 8, 'Naboo system')
# print(f'Name is: {planetXR.name}')
# print(f'Radius is: {planetXR.radius}')
# print(f'The Gravity is: {planetXR.gravity}')
# print(planetXR.orbit())
# print(Planet.shape)
# print(planetXR.commons())
#print(Planet.orbit())
#print(Planet.spin('very high speed'))
