import matplotlib.pyplot as plt

from Particle import Particle

def class SPH_Simulation(object):
    """docstring for SPH_Simulation."""
    def __init__(self, m_total, n_sph, boundary, timestep):
        # Store the initial parameters as class attributes.
        self.m_total, self.sph, self.boundary = m_total, n_sph, boundary
        # Calculate and store the mass of a single particle.
        self.m_particle = m_total / n_sph
        # Initialize list of Particle objects.
        self.particles = []
        for i in range(n_sph):
            self.particles.append(Particle(self.m_particle, random.uniform(0.0, boundary), 0.0))
        # Initialize list of densities corresponding to the location of each particle.
        self.densities = []
        for i in range(n_sph):
            densities.append(get_density(self.particles[i].position))
        # Initialize a list of net force on each particleself.
        forces = []
        for i in range(n_sph):
            forces.append(get_force(self.particles[i].position))

    # Runs the simulation and animates it.
    def run(self):
        while t <= t_max:
            self.update_densities()
            self.update_forces()
            self.step_forward()

    # Updates the list of densities to reflect current particle positions.
    def update_densities(self):
        for i in range(self.n_sph):
            densities[i] = get_density(self.particles[i].position)

    # Gets density at position of a particle due to neighboring particles.
    def get_density(self, position, kernel):
        for i in range(self.n_sph):
            separation = position - self.particles[i].position
            density += self.m_particle * kernel(separation, smoothing_length)
        return(density)

    # Updates the list of force to reflect current particle positions.
    def update_forces(self):
        return()

    # Gets the net force on a particle at a position due to neighboring particles.
    def get_force(self, position):
        return(force)
        
    # Gaussian smoothing kernel.
    def gaussian_kernel(r, h):
        q = r / h
        return((1.0/h**3/m.pi**1.5)*(m.exp(-q**2)))

    # Monaghan and Lattanzio (1985) spline smoothing kernel.
    def spline_kernel(r, h):
        q = r / h
        if q >= 0.0 && q <= 1.0:
            return((1.0/m.pi/h**2)*(1.0-1.5*q**2+0.75*q**3))
        elif q >= 1.0 && q <=2.0:
            return((1.0/4.0/m.pi/h**2)*(2.0-q)**3)
        elif q >=2:
            return(0.0)
        else:
            print("Error! q=r/h is negative, or of incorrect type!")
