import matplotlib.pyplot as plt
import measure

test_wave = measure.Static_object(3, 1000)
test_wave.set_parameters([1,1,1])
test_wave.transform()

# plt.plot(test_wave.t, test_wave.u)
# plt.show()