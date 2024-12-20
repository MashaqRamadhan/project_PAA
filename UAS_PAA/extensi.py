import random
import numpy as np
import matplotlib.pyplot as plt

last_three_digits_nim = 3
max_value = 250 - last_three_digits_nim

def generate_random_array(n, max_value):
    return np.random.choice(range(1, max_value + 1), n, replace=True)

def is_unique(arr):
    return len(arr) == len(set(arr))

def calculate_cases(n, max_value):
    worst_case = n * (n - 1) // 2
    average_case = 0
    unique_flag = False
    arr = generate_random_array(n, max_value)
    if is_unique(arr):
        unique_flag = True
        average_case = n
    else:
        average_case = n * (n - 1) // 2
    return unique_flag, worst_case, average_case

def analyze_cases(n_values, max_value):
    worst_cases = []
    average_cases = []
    for n in n_values:
        unique_flag, worst_case, average_case = calculate_cases(n, max_value)
        worst_cases.append(worst_case)
        average_cases.append(average_case)
    return worst_cases, average_cases

n_values = [100, 150, 200, 250, 300, 350, 400, 500]
worst_cases, average_cases = analyze_cases(n_values, max_value)

for i in range(len(n_values)):
    print(f"n={n_values[i]}, Worst Case={worst_cases[i]}, Average Case={average_cases[i]}")

with open('worst_avg.txt', 'w') as file:
    for i in range(len(n_values)):
        file.write(f"n={n_values[i]}, Worst Case={worst_cases[i]}, Average Case={average_cases[i]}\n")

plt.plot(n_values, worst_cases, label='Worst Case', color='red', marker='o')
plt.plot(n_values, average_cases, label='Average Case', color='blue', marker='x')
plt.xlabel('n (Jumlah Elemen)')
plt.ylabel('Jumlah Perbandingan')
plt.title('Perbandingan Kasus Terburuk dan Kasus Rata-rata')
plt.legend()
plt.grid(True)
plt.savefig('worst_avg_plot.pdf')
plt.show()
