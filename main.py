import matplotlib.pyplot as plt
import measure

test_wave = measure.Triangle_wave(3, 1000)


plt.plot(test_wave.t, test_wave.original_y)
plt.show()