#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.figure(figsize=(12, 8))
plt.suptitle('All in One', fontsize='x-small')
plt.subplot(3, 2, 1)
plt.plot(y0, 'r')
plt.xlabel('X', fontsize='x-small')
plt.ylabel('Y', fontsize='x-small')
plt.xlim(0,10)


plt.subplot(3, 2, 2)
plt.scatter(x1, y1, color='magenta', s=5)
plt.xlabel('Height (in)', fontsize='x-small')
plt.ylabel('Weight (lbs)', fontsize='x-small')
plt.title("Men's Height vs Weight", fontsize='x-small')


plt.subplot(3, 2, 3)
plt.plot(x2, y2)
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.title('Exponential Decay of C-14', fontsize='x-small')
plt.yscale('log')
plt.xlim(0,28650)


plt.subplot(3, 2, 4)
plt.plot(x3, y31, 'r--', label='C-14')
plt.plot(x3, y32, 'g-', label='Ra-226')
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.title('Exponential Decay of Radioactive Elements', fontsize='x-small')
plt.legend(fontsize='x-small')
plt.xlim(0,20000)
plt.ylim(0,1)


plt.subplot(3, 2, (5, 6))
plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
plt.xlabel('Grades', fontsize='x-small')
plt.ylabel('Number of Students', fontsize='x-small')
plt.title('Project A', fontsize='x-small')
plt.xlim(0, 100)
plt.xticks(range(0, 101, 10))
plt.ylim(0, 30)


plt.tight_layout()
plt.subplots_adjust(top=0.92)

plt.show()

