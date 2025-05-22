import numpy as np
import matplotlib.pyplot as plt

# "true" solution
def exponential(x):
    return np.exp(-3*x)

# reading data
out0 = [[float(x) for x in line.split()] # dt=10^0 run
        for line in open("data/output0.dat", "r").readlines()]

out1 = [[float(x) for x in line.split()] # dt=10^-1 run
        for line in open("data/output1.dat", "r").readlines()]

out2 = [[float(x) for x in line.split()] # dt=10^-2 run
        for line in open("data/output2.dat", "r").readlines()]

out3 = [[float(x) for x in line.split()] # dt=10^-3 run
        for line in open("data/output3.dat", "r").readlines()]

out4 = [[float(x) for x in line.split()] # dt=10^-4 run
        for line in open("data/output4.dat", "r").readlines()]

out5 = [[float(x) for x in line.split()] # dt=10^-5 run
        for line in open("data/output5.dat", "r").readlines()]

out6 = [[float(x) for x in line.split()] # dt=10^-6 run
        for line in open("data/output6.dat", "r").readlines()]

# transposing data for plotting
data0=np.copy(out0)
data1=np.copy(out1)
data2=np.copy(out2)
data3=np.copy(out3)
data4=np.copy(out4)
data5=np.copy(out5)
data6=np.copy(out6)

data0=np.transpose(data0)
data1=np.transpose(data1)
data2=np.transpose(data2)
data3=np.transpose(data3)
data4=np.transpose(data4)
data5=np.transpose(data5)
data6=np.transpose(data6)

# creating data for analytic solution
trueExp=exponential(data4[0])

# plotting
# plt.plot(data0[0],data0[1],label="dt=1e0")
plt.plot(data1[0],data1[1],label="dt=1e-1")
plt.plot(data2[0],data2[1],label="dt=1e-2")
plt.plot(data3[0],data3[1],label="dt=1e-3")
plt.plot(data4[0],data4[1],label="dt=1e-4")
# plt.plot(data5[0],data5[1],label="dt=1e-5")
# plt.plot(data6[0],data6[1],label="dt=1e-6")
plt.plot(data4[0],trueExp,label="Analytic")
plt.legend()
plt.title("Comparison of Step Sizes")
plt.savefig("plt/exp_comp.png")
plt.close()