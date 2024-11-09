import numpy as np
import matplotlib.pyplot as plt
import logging
logger = logging.getLogger(__name__)
from time import perf_counter
from scipy.stats import norm

def basic_Gibbs_sampler(X0, max_t_iterations=10**3, rho = .8):
    """
    Gibbs sampler targeting 2D-Normal theta with mean zero and covariance matrix of (Id plus correlation p)

    """
    #start timing here
    start_time = perf_counter()

    
    chain = np.zeros((max_t_iterations,2))
    x = chain[0] = X0
    for t in range(1, max_t_iterations):
        #X_t will be what is stored in the variable x after this is finished
        # order of subcomponents is arbitary here, following numbering given in description
        #in rvs() scale means stdev
        std_dev = np.sqrt(1-rho**2)
        #theta_1 | theta_-1, y
        x[0] = norm.rvs(loc = rho*x[1], scale = std_dev)
        #theta_2 | theta_-2, y
        x[1] = norm.rvs(loc = rho*x[0], scale = std_dev)

        #record X_t
        chain[t] = x

    #end timing here
    end_time = perf_counter()
    simulation_time = end_time-start_time
    logger.info(f"chain took {simulation_time:.2f} seconds")

    return chain

def simply_plot_the_chains(chains, fmt_plt="k-"):
    """
    plots 2D chains over time on the same plot
    """
    fig, ax = plt.subplots()
    for chain in chains:
        ax.plot(chain[:,0], chain[:,1], fmt_plt)
        #plot starting point
        ax.plot(*chain[0,:], "sk", markersize = 15)
    ax.set_title("")
    plt.show()