from space.Planet import Planet
from space.calc import planet_mass, planet_vol

planetXR = Planet('Naboo', 300000, 8, 'Naboo system')
# print(f'Name: {planetXR.name}')
# print(planetXR.spin('very high speed'))

planetXR_mass = planet_mass(planetXR.gravity, planetXR.radius)
planetXR_vol = planet_vol(planetXR.radius)

print(f'{planetXR.name} has a mass of {planetXR_mass} and volume {planetXR_vol}')
