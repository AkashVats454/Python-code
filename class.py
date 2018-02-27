class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in {self.system}'

hoth = Planet('Hoth',200000, 5.5, 'Hoth System')
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The Gravity is: {hoth.gravity}')
print(hoth.orbit())

planetXR = Planet('Naboo', 300000, 8, 'Naboo system')
print(f'Name is: {planetXR.name}')
print(f'Radius is: {planetXR.radius}')
print(f'The Gravity is: {planetXR.gravity}')
print(planetXR.orbit())
