from SPH_Simulation import SPH_Simulation

# Run the simulation given total mass, particle count, and boundary.
def main(m_total, n_sph, boundary):

    simulation = SPH_Simulation(m_total, n_sph, boundary)
    simulation.run()

main()
