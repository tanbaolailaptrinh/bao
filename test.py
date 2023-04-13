import matplotlib.pyplot as plt

# Sample data
rsa_mean = 0.07472
ase_mean = 0.031282

# Create bar chart
bar_width = 0.35
opacity = 0.8
index = [1, 2]
rsa_data = [rsa_mean, 0]
ase_data = [0, ase_mean]

fig, ax = plt.subplots()
rsa_bar = ax.bar(index, rsa_data, bar_width,
                 alpha=opacity, color='b', label='RSA')
ase_bar = ax.bar([i + bar_width for i in index], ase_data, bar_width,
                 alpha=opacity, color='g', label='ASE')

# Add labels, title, and legend
ax.set_xlabel('Statistics')
ax.set_ylabel('Time (seconds)')
ax.set_title('Comparison of RSA and ASE')
ax.set_xticks([i + bar_width/2 for i in index])
ax.set_xticklabels(('RSA', 'ASE'))
ax.legend()

plt.tight_layout()
plt.show()