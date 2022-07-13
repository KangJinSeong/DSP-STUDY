'''
Date: 2021.12.07
Title: z- transform study
By: Kang Jin Seong
'''

import numpy as np
from scipy import signal

def convole_m(x,nx,h,nh):
    nyb = min(nx) + min(nh)
    nye = max(nx) + max(nh)
    ny = np.arange(nyb,nye+1)
    y = np.convolve(x,h)
    return y, ny

def impseq(n0,n1,n2):
    N = n2-n1+1
    x = np.zeros(N)
    n = np.arange(N)
    for i in range(N):
        if i==n0: x[i] = 1
    return x,n

def stepseq(n0,n1,n2):
    N = n2-n1+1
    x = np.zeros(N)
    n = np.arange(N)
    for i in range(N):
        if i-n0>=0: x[i] = 1
    return x,n

    


def main():
    # x1 = [1,2,3]; n1 = np.arange(-1,2)
    # print('x1(n) = ',x1,'n1 = ',n1)
    # x2 = [2,4,3,5]; n2 = np.arange(-2,2)
    # print('x2(n) = ',x2,'n2 = ',n2)
    # x3,n3 = convole_m(x1,n1,x2,n2)
    # print('x3(n) = ',x3,'n3 = ',n3)

    b = [0,0,0,0.25,-0.5,0.0625]
    a = [1,-1,0.75,-0.25,0.0625]

    N = 8

    delta,n = impseq(0,0,7); print('impulse=',delta)
    x = signal.lfilter(b,a,delta); print('x(n) = ', x)
    n = np.arange(N)

    s,n1 = stepseq(2,0,7); print('step u(n-2) =', s);
    x = (n1-2)*np.power(0.5,n1-2)*np.cos(np.pi/3*(n1-2))*s
    print('x(n) =',x)


if __name__ == "__main__":
    main()
