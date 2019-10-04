import matplotlib.pyplot as plt

def animate(self, i):

    self.stepForward()
    self.t += self.timestep

    # Updates the position of each patch with the new simulation data.
    for n in range(self.n_sph):
        self.patches[n].center = (self.particles[n].position)
    return(self.patches)

def display(self):

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
