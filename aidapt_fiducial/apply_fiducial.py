# by Tyler Viducic and Torri Jeski

import numpy as np
from event import Event
from fiducialCuts import FiducialCuts
import time

# Read in data here 

data_file = '/media/tylerviducic/Elements/aidapt/synthetic/clasfilter2_5M780.npy' # change to your path, obviously

input_array = np.load(data_file)
output_array = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
delete_row_list = []

num_rows, num_columns = input_array.shape

start = time.time()
for n in range(num_rows):

    row = input_array[n]
    event = Event(row)
    fd = FiducialCuts(event)

    if fd.check_event_pass():
        output_array = np.append(output_array, [row], axis=0)
    else:
        delete_row_list.append(n)


output_array = np.delete(output_array, 0, axis=0)

end = time.time()
print("Theoretical size of output array: " + str(num_rows - len(delete_row_list)))
num_rows, num_columns = output_array.shape

print('Size of output array: ' + str(num_rows))
print('time/event = ' + str((end - start)/2506780) + " seconds")
