import numpy as np

def mass_to_radius(mass, droplet_density):
    return  np.cbrt(3*mass/(4*np.pi*droplet_density))

def radius_to_mass(radius, droplet_density):
    return 4/3 *np.pi*radius**3*droplet_density