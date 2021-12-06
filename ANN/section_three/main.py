import time

import numpy as np

from ANN.section_one.credentials import get_path_of_Datasets
from ANN.section_one.utils.utilsV1 import load_data
from ANN.section_three.utils.utilsV3 import L_layer_model


def run_program():
    path = get_path_of_Datasets()
    train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig = load_data(path)
    x_train = np.zeros((102, 1962))
    y_train = np.zeros((4, 1962))
    for i in range(1962):
        for j in range(102):
            x_train[j, i] = train_set_x_orig[i][j]
    for i in range(1962):
        for j in range(4):
            y_train[j, i] = train_set_y_orig[i][j]
    x_section_three = x_train[:, 0:200]
    y_section_three = y_train[:, 0:200]
    start_time = time.time()
    val = L_layer_model(x_section_three, y_section_three, [102, 150, 60, 4], num_epochs=20, print_cost=True)
    print("\n--- %s seconds ---" % (time.time() - start_time))
    return val


sum_of_costs = 0
for i in range(10):
    print(f"\nrunning program with i = {i}\n")
    sum_of_costs += run_program()

print(f"average cost is {sum_of_costs / 200}")
