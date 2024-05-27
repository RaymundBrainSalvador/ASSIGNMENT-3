import numpy as np

data_matrix = np.array([[11, 28, 15], [17, 26, 12], [19, 38, 20]])
np.savetxt('data_matrix.csv', data_matrix, delimiter=',')

print("CSV file saved successfully.")

names_array = np.array(["Alice", "Bob", "Charlie"])
np.save('names_array.npy', names_array)

print("Binary file saved successfully.")

array_one = np.array([[15, 9, 21], [6, 14, 8]])
array_two = np.array([[21, 17, 16], [8, 18, 15]])
np.savez_compressed('compressed_arrays.npz', array_one=array_one, array_two=array_two)

print("Compressed file saved successfully.")


loaded_matrix = np.loadtxt('data_matrix.csv', delimiter=',')
print("Loaded from CSV file:\n", loaded_matrix)

print()

loaded_names = np.load('names_array.npy')
print("Loaded from binary file:\n", loaded_names)

print()

compressed_file = np.load('compressed_arrays.npz')
loaded_array_one = compressed_file['array_one']
loaded_array_two = compressed_file['array_two']
print("Loaded from compressed file:\nArray One:\n", loaded_array_one, "\nArray Two:\n", loaded_array_two)