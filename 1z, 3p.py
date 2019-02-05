import numpy as np
cur_x = -0.5  # The algorithm starts at x=3
cur_y = -0.5
rate = 1  # Learning rate
precision = 0.00001  # This tells us when to stop the algorithm
previous_step_size_x = 1
previous_step_size_y = 1
max_iters = 100000  # maximum number of iterations
iters = 0  # iteration counter


def grad_x(x1, y1):
    return x1*(np.sin(np.sqrt(x1**2 + y1**2))**2 - 0.5)/(500*(x1**2/1000 + y1**2/1000 + 1)**2) - 2*x1*np.sin(np.sqrt(x1**2 + y1**2))*\
           np.cos(np.sqrt(x1**2 + y1**2))/(np.sqrt(x1**2 + y1**2)*(x1**2/1000 + y1**2/1000 + 1))
def grad_y(x2, y2):
    return y2*(np.sin(np.sqrt(x2**2 + y2**2))**2 - 0.5)/(500*(x2**2/1000 + y2**2/1000 + 1)**2) - 2*y2*np.sin(np.sqrt(x2**2 + y2**2))*\
           np.cos(np.sqrt(x2**2 + y2**2))/(np.sqrt(x2**2 + y2**2)*(x2**2/1000 + y2**2/1000 + 1))
while previous_step_size_x > precision and previous_step_size_y > precision and iters < max_iters:
    prev_x = cur_x  # Store current x value in prev_x
    prev_y = cur_y
    cur_x = cur_x + rate * grad_x(prev_x, prev_y)  # Grad descent
    cur_y = cur_y + rate * grad_y(prev_x, prev_y)
    previous_step_size_x = abs(cur_x + prev_x)  # Change in x
    previous_step_size_y = abs(cur_y + prev_y)  # Change in y
    iters = iters + 1  # iteration count
    print("Iteration", iters, "\nX, Y value is", cur_x, cur_y)  # Print iterations

print("The local maximum occurs at", "x: ", cur_x, "y: ", cur_y)