from functions import *
import logging 
logger = logging.getLogger(__name__)
logging.basicConfig( level=logging.INFO)

FULL_CHAIN_ITERATIONS = 10
# X_0 = np.array([2.5, 2.5])
# list_of_chains = []
# for starting_point in [
#     [-2.5,-2.5],[-2.5,2.5],[2.5,2.5],[2.5,-2.5]  ]:
#     list_of_chains.append( basic_Gibbs_sampler(starting_point, FULL_CHAIN_ITERATIONS) )
starting_points = np.array([[-2.5,-2.5], [-2.5,2.5],[2.5,2.5],[2.5,-2.5]])
list_of_chains = [basic_Gibbs_sampler(x_0, FULL_CHAIN_ITERATIONS) for x_0 in starting_points]
simply_plot_the_chains(list_of_chains)