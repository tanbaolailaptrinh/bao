import pandas as pd

dataASE = {'Lan chay thu n': [1, 2, 3, 4, 5],
        'Thoi gian chay (ASE    )': [0.1532286, 0.0004440, 0.0007132, 0.0007061, 0.0003221]}
print("ASE")
df = pd.DataFrame(dataASE)
print(df)
print("RSA")

data = {'Chay lan thu n': [1, 2, 3, 4, 5],
        'Thoi gian chay (RSA)': [0.1198, 0.0436, 0.0639, 0.0602, 0.0861]}

df = pd.DataFrame(data)

print(df)
import matplotlib.pyplot as plt

# Sample data
rsa_mean = 0.07472
rsa_std = 0.015714
ase_mean = 0.031282
ase_std = 0.067732

# Create bar chart
bar_width = 0.35
opacity = 0.8
index = [1, 2]
rsa_data = [rsa_mean, rsa_std]
ase_data = [ase_mean, ase_std]

fig, ax = plt.subplots()
rsa_bar = ax.bar(index, rsa_data, bar_width,
                 alpha=opacity, color='b', label='RSA')
ase_bar = ax.bar(index + bar_width, ase_data, bar_width,
                 alpha=opacity, color='g', label='ASE')

# Add labels, title, and legend
ax.set_xlabel('Statistics')
ax.set_ylabel('Time (seconds)')
ax.set_title('Comparison of RSA and ASE')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Mean', 'Standard Deviation'))
ax.legend()

plt.tight_layout()
plt.show()

