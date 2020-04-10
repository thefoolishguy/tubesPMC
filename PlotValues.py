import matplotlib.pyplot as plt
import pandas as pd

dataBase =  pd.read_csv('D:\Kuliah\Materi TEKNIK ELEKTRO\Semester 4\EL2008 Pemecahan Masalah dengan C\TUGAS\Tugas Besar\HasilTracking.txt',
             delimiter=' \t'  , engine='python', skiprows = 1)
 
# getMax value of Y
maxV =  dataBase.iloc[0]['V1']
maxI =  dataBase.iloc[0]['I1']

# Plot for V1
dataBase.plot(x = 'time', y = 'V1')
plt.ylim(0, 1.1*maxV)
plt.xlim(0)
plt.title('PLot Tegangan V1 terhadap waktu (V)')
plt.xlabel("Waktu (s)")
plt.ylabel("V1 (V)")
plt.show()

# Plot for V2
dataBase.plot(x = 'time', y = 'V2')
plt.ylim(0, 1.1*maxV)
plt.xlim(0)
plt.title('PLot Tegangan V2 terhadap waktu (V)')
plt.xlabel("Waktu (s)")
plt.ylabel("V2 (V)")
plt.show()

# Plot for V3
dataBase.plot(x = 'time', y = 'V3')
plt.ylim(0, 1.1*maxV)
plt.xlim(0)
plt.title('PLot Tegangan V3 terhadap waktu (V)')
plt.xlabel("Waktu (s)")
plt.ylabel("V3 (V)")
plt.show()

# Plot for V4
dataBase.plot(x = 'time', y = 'V4')
plt.ylim(0, 1.1*maxV)
plt.xlim(0)
plt.title('PLot Tegangan V4 terhadap waktu (V)')
plt.xlabel("Waktu (s)")
plt.ylabel("V4 (V)")
plt.show()

# Plot for I1
dataBase.plot(x = 'time', y = 'I1')
plt.ylim(0, 1.1*maxI)
plt.xlim(0)
plt.title('PLot Tegangan I1 terhadap waktu (A)')
plt.xlabel("Waktu (s)")
plt.ylabel("I1 (A)")
plt.show()

# Plot for I2
dataBase.plot(x = 'time', y = 'I2')
plt.ylim(0, 1.1*maxI)
plt.xlim(0)
plt.title('PLot Tegangan I2 terhadap waktu (A)')
plt.xlabel("Waktu (s)")
plt.ylabel("I2 (A)")
plt.show()

# Plot for I3
dataBase.plot(x = 'time', y = 'I3')
plt.ylim(0, 1.1*maxI)
plt.xlim(0)
plt.title('PLot Tegangan I3 terhadap waktu (A)')
plt.xlabel("Waktu (s)")
plt.ylabel("I3 (A)")
plt.show()

# Plot for I4
dataBase.plot(x = 'time', y = 'I4')
plt.ylim(0, 1.1*maxI)
plt.xlim(0)
plt.title('PLot Tegangan I4 terhadap waktu (A)')
plt.xlabel("Waktu (s)")
plt.ylabel("V4 (A)")
plt.show()

# Plot for Ic
dataBase.plot(x = 'time', y = 'Ic')
plt.ylim(0, 1.1*maxI)
plt.xlim(0)
plt.title('PLot Tegangan Ic terhadap waktu (A)')
plt.xlabel("Waktu (s)")
plt.ylabel("Vc (A)")
plt.show()

print(maxV , maxI)