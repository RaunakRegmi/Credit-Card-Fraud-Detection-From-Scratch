import matplotlib.pyplot as plt

N = [250, 500, 750, 1092]
collisions = [11, 43, 91, 184]
logistic_time = [0.042, 0.089, 0.131, 0.198]
tree_time = [0.115, 0.421, 0.982, 1.894]


plt.figure(figsize=(6, 4))
plt.plot(N, logistic_time, label='Logistic Regression (Parametric)', color='blue', marker='s', linewidth=2)
plt.plot(N, tree_time, label='Decision Tree (Non-Parametric)', color='red', marker='o', linewidth=2)
plt.title('Algorithmic Training Time Complexity Scaling Profiles', fontsize=11, fontweight='bold')
plt.xlabel('Dataset Size (Number of Transacted Records N)', fontsize=10)
plt.ylabel('Execution Fit Interval (Seconds)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('runtime_scaling_benchmark.png', dpi=300)
plt.close()


fig, ax1 = plt.subplots(figsize=(6, 4))
color = 'purple'
ax1.set_xlabel('Dataset Size (Number of Transacted Records N)', fontsize=10)
ax1.set_ylabel('Absolute Collision Event Count', color=color, fontsize=10)
ax1.plot(N, collisions, color=color, marker='^', linewidth=2, label='Collisions')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.6)

plt.title('Memory Architecture Stability Profile (K=3007)', fontsize=11, fontweight='bold')
fig.tight_layout()
plt.savefig('memory_stability_benchmark.png', dpi=300)
plt.close()
print("High-resolution figure graphics generated successfully!")