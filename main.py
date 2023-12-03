import matplotlib.pyplot as plt
import static

test_obj = static.Static_object(3000, 10000)
test_obj.set_parameters([2,6,1])
test_obj.transform()
test_obj.noise(0.1, -0.5)
print(test_obj.LSM())
test_obj.plot_parameters_history()



# plt.plot(test_obj.t, test_obj.y)
# plt.show()