import matplotlib.pyplot as plt
import measure

test_obj = measure.Static_object(3, 1000)
test_obj.set_parameters([1,1,1])
test_obj.transform()
test_obj.noise(1, -0.5)
print(test_obj.LSM())
test_obj.plot_parameters_history()



# plt.plot(test_obj.t, test_obj.y)
# plt.show()