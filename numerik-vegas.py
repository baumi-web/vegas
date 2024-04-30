import vegas
import math

def calculate_volume(x):
    # Parameters cone
    r = 1
    h = 2

    # points in cone?
    # x[0]∗∗2+x[1]∗∗2 -> sqrt. distance of z in xy

    if x[0]*2 + x[1]2 <= (x[2]/h)2 * r*2 and x[2] <= h:
        #return x[0]*2 + x[1]2 + x[2]*2  # function for integration
        return 1  # point is in cone
    else:
        return 0  # point is not in cone

    # Iteration & evaluation 
"""""
for iteration in range(10, 110, 10):
    for evaluation in range(1000, 11000, 1000):
        # def range of random numbers
        integ = vegas.Integrator([[-1, 1], [-1, 1], [0, 2]])
        result = integ(calculate_volume, nitn=iteration, neval=evaluation)
        mean_value = result.mean
        exact_volume = (1/3) * math.pi * 1**2 * 2
        print(f"Iterationen: {iteration}, Evaluationen: {evaluation}, mcVol: {mean_value}, ExVol: {exact_volume}x, diff: {abs(mean_value - exact_volume)}")
"""
for evaluation in range(1000, 11000, 1000):
        # def range of random numbers
        integ = vegas.Integrator([[-1, 1], [-1, 1], [0, 2]]) #limits
        result = integ(calculate_volume, nitn=40, neval=evaluation)
        """
        - nitn wird statisch auf 40 gesetzt -> Anz. Iterationen
        - neval wird mit jeder iteration erhöht-> Anz. generierte Zufallszahlen/Iteration
        """
        mean_value = result.mean
        exact_volume = (1/3) * math.pi * 1**2 * 2 # exact volume of the cone
        print(f"Iterations: {evaluation}, mcVol: {mean_value}, ExVol: {exact_volume}x, diff: {abs(mean_value - exact_volume)}")