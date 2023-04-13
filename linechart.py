import matplotlib.pyplot as plt

# RSA data
rsa_x = [1, 2, 3, 4, 5]
rsa_y = [0.1198, 0.0436, 0.0639, 0.0602, 0.0861]

# ASE data
ase_x = [1, 2, 3, 4, 5]
ase_y = [0.1532286, 0.0004440, 0.0007132, 0.0007061, 0.0003221]

# Create line chart
fig, ax = plt.subplots()
ax.plot(rsa_x, rsa_y, color='blue', label='RSA')
ax.plot(ase_x, ase_y, color='green', label='ASE')

# Add labels, title, and legend
ax.set_xlabel('Run')
ax.set_ylabel('Time (seconds)')
ax.set_title('RSA vs ASE')
ax.legend()

plt.show()
