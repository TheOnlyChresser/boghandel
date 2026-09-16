import matplotlib.pyplot as plt

arr = []
maks = 20

for nummer in range(maks):
    for i in range(nummer):
        nummer *= (i + 1)
    arr.append(nummer)

plt.plot(arr)
plt.xlabel("n")
plt.ylabel("værdi")
plt.show()
