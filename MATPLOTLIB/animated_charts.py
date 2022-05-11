import numpy as np
import matplotlib.pyplot as plt

labels = ["Chrome", "Firefox", "Safari"]
shares = np.array([
	[0.5, 0.3, 0.2],
	[0.4, 0.4, 0.2],
	[0.4, 0.1, 0.5],
	[0.5, 0.2, 0.3],
	[0.3, 0.2, 0.5],
	[0.3, 0.4, 0.3],
	[0.2, 0.3, 0.5],
	[0.3, 0.5, 0.2]
])

years = [2010 + i for i in range(8)]


plot_steps= np.array([shares[0]])

last_shares= shares[0]
for i in range(1, len(shares)):
	differences = shares[i] -last_shares
	differences /= 100

	for j in range(100):
		plot_steps = np.append(plot_steps, [last_shares+differences *j], 0)

print(plot_steps)
