import numpy as np
import matplotlib.pyplot as plt

# "true" solution
def exponential(x):
    return np.exp(-3*x)

# reading data
out0 = [[float(x) for x in line.split()] # dt=10^0 run
        for line in open("../data/output0.dat", "r").readlines()]

out1 = [[float(x) for x in line.split()] # dt=10^-1 run
        for line in open("../data/output1.dat", "r").readlines()]

out2 = [[float(x) for x in line.split()] # dt=10^-2 run
        for line in open("../data/output2.dat", "r").readlines()]

out3 = [[float(x) for x in line.split()] # dt=10^-3 run
        for line in open("../data/output3.dat", "r").readlines()]

out4 = [[float(x) for x in line.split()] # dt=10^-4 run
        for line in open("../data/output4.dat", "r").readlines()]

out5 = [[float(x) for x in line.split()] # dt=10^-5 run
        for line in open("../data/output5.dat", "r").readlines()]

# out6 = [[float(x) for x in line.split()] # dt=10^-6 run
#         for line in open("../data/output6.dat", "r").readlines()]

# transposing data for plotting
out0=out0.T
out1=out1.T
out2=out2.T
out3=out3.T
out4=out4.T
out5=out5.T
# out6=out6.T

# creating data for analytic solution
trueExp=exponential(out5[0])

# plotting
plt.plot(out0[0],out0[1],label="dt=1e0")
plt.plot(out1[0],out1[1],label="dt=1e-1")
plt.plot(out2[0],out2[1],label="dt=1e-2")
plt.plot(out3[0],out3[1],label="dt=1e-3")
plt.plot(out4[0],out4[1],label="dt=1e-4")
plt.plot(out5[0],out5[1],label="dt=1e-5")
# plt.plot(out6[0],out6[1],label="dt=1e-6")
plt.plot(out5[0],trueExp,label="Analytic")
plt.legend()
plt.title("Comparison of Step Sizes")
plt.show()