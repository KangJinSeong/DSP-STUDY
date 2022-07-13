'''
Date: 2021.12.15
Title: z- transform study
By: Kang Jin Seong
'''
import numpy as np
from scipy import signal

import matplotlib.pyplot as plt
from matplotlib import patches, rcParams

def zplane(b,a):
    ax = plt.subplot(1,1,1) # 그림팡을 만들고 단위원을 그린다.
    uc = patches.Circle((0,0), radius = 1, fill = False, color = 'black', ls = 'dashed')

    ax.add_patch(uc)

    if np.max(b) > 1:   #계수값 정규화
        kn = np.max(b)
        b = b/float(kn)

    else:
        kn = 1
    
    if np.max(a) > 1:
        kd = np.max(a)
        a = a/float(kd)

    else:
        kd = 1

    p = np.roots(a) #극점, 영점 결정
    z = np.roots(b)
    k = kn/float(kd)

    t1 = plt.plot(z.real, z.imag, 'go', ms = 10)    #영점 그리고 표시하기
    plt.setp(t1, markersize = 10, markeredgewidth = 1.0, markeredgecolor = 'k', markerfacecolor = 'g')

    t2 = plt.plot(p.real, p.imag, 'rx', ms = 10)
    plt.setp(t1, markersize = 12, markeredgewidth = 3.0, markeredgecolor = 'r', markerfacecolor = 'r')
    plt.title("pole_Zero Diagram"); plt.grid()

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    r = 1.5; plt.axis('scaled'); plt.axis([-r, r, -r, r])   #눈금 값 쓰기
    ticks = [-1, -.5, .5, 1]; plt.xticks(ticks); plt.yticks(ticks)


def main():
    b = [1,0]
    a = [1,-0.9]

    plt.figure(1); zplane(b,a)

    Omega,H = signal.freqz(b,a,100)
    magH = np.abs(H)
    phaH = np.angle(H)

    plt.figure(2)
    plt.subplot(2,1,1); plt.plot(Omega, magH, "blue");plt.grid()
    plt.ylabel("magnitude");plt.title("Magnitude & Phase Response")
    plt.subplot(2,1,2); plt.plot(Omega, phaH, "blue");plt.grid()
    plt.xlabel("frequency in radian"); plt.ylabel("phase")

    plt.show()

if __name__ == "__main__":
    main()
      