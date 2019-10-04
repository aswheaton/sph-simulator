import matplotlib.pyplot as plt

from Particle import Particle

def class SPH_Simulation(object):
    """docstring for SPH_Simulation."""
    def __init__(self, m_total, n_sph, boundary, timestep):
        # Store the initial parameters as class attributes.
        self.m_total, self.sph, self.boundary, self.timestep = m_total, n_sph, boundary, timestep
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
        # Initialize a list of net force on each particle.
        self.forces = []
        for i in range(n_sph):
            forces.append(get_force(self.particles[i].position))

    # Runs the simulation and animates it.
    def run(self):
        # Creates figure and axes elements. Scales and labels them appropriately.
        self.figure = plt.figure()
        self.axes = plt.axes()
        self.axes.axis('scaled')
        self.axes.set_xlim(0.0, self.boundary)
        self.axes.set_ylim(0.0, self.boundary)
        self.axes.set_xlabel('x-coordinate (m)')
        self.axes.set_ylabel('y-coordinate (m)')

        # Creates a list of circles to be plotted by pyplot and adds them to the axes.
        self.patches = []

        for i in range(self.n_sph):
            # Syntax: plt.Circle((xpos,ypos), patch_size, color="string", animate=True)
            self.patches.append(plt.Circle((self.particles[i].position), 1.0, color="blue", animated=True))
        for i in range(self.n_sph):
            self.axes.add_patch(self.patches[i])

        # Animates the plot.
        self.animation = FuncAnimation(self.figure, self.animate, frames=self.maxIterations, repeat=False, interval=20, blit=True)
        # Show the plot.
        plt.show()

        # while self.t <= self.t_max:
        #     self.update_densities()
        #     self.update_forces()
        #     self.step_forward()

    def animate(self, i):
        self.step_forward()
        self.t += self.timestep
        # Updates the position of each patch with the new simulation data.
        for n in range(self.n_sph):
            self.patches[n].center = (self.particles[n].position)
        return(self.patches)

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

    # Calculates and returns an adaptive smoothing length based on the density
    # at the particle's position on the previous iteration. Hard coded to
    # include approximately 50 neighboring particles inside the smoothing length.
    # This is not ideally formulated, so will make more elegant later!
    def get_smoothing_length(self, i):
        density = self.densities[i]
        smoothing_length = 50.0 * self.m_particle / 2.0 / density
        return(smoothing_length)

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
