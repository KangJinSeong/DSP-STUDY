'''
Date: 2022.02.15
Title: 디지털 필터 구조 설계(design) 및 구현(Implementation) FIR
By: Kang Jin Seong
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftshift, fft
from scipy.signal import chirp

class chap_6:
    def __init__(self, select):
        self.type = select 

    def FIR_direct_1(self):    # 제1형 직접형 IIR 필터
        tn = 5000   #총 데이터 샘플 수
        t = np.linspace(0, 1, tn)   # x축 설정
        input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method='linear')
        y  = [0] * tn
        for n in range(4, len(input)):
            y[n] = input[n] + 16.060625*input[n-4] + input[n-8]
        plt.figure()
        plt.plot(y, 'b'); plt.xlim(0,5000)
        plt.xlabel('samples, frequency[0~500Hz'); plt.grid()
        plt.title('Frequency filtering result of FIR direct filter')


    def FIR_linear_phase(self):    # 제2형 직접형 IIR 필터
        tn = 5000   #총 데이터 샘플 수
        t = np.linspace(0, 1, tn)   # x축 설정
        input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method='linear')
        y  = [0] * tn
        for n in range(4, len(input)):
            y[n] = (input[n] + input[n-8])+16.0625*input[n-4]
        plt.figure()
        plt.plot(y, 'b'); plt.xlim(0,5000)
        plt.xlabel('samples, frequency[0~500Hz'); plt.grid()
        plt.title('Frequency filtering result of FIR linear phase filter')

    def FIR_cascade(self):  # 직렬형 구조
        tn = 5000   #총 데이터 샘플 수
        t = np.linspace(0, 1, tn)   # x축 설정
        input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method='linear')
        y  = [0] * tn
        v1 = [0]*tn; v2 = [0]*tn; v3 = [0]*tn
        for n in range(4, len(input)):
            v1[n] = input[n] + 2.8284*input[n-1] + 4*input[n-2]
            v2[n] = v1[n] + 0.7071*v1[n-1] + 0.25*v1[n-2]
            v3[n] = v2[n] - 0.7071*v2[n-1] + 0.25*v2[n-2]
            y[n] = v3[n] - 2.8284*v3[n-1] + 4*v3[n-2]
        plt.figure()
        plt.plot(y, 'b'); plt.xlim(0,5000)
        plt.xlabel('samples, frequency[0~500Hz'); plt.grid()
        plt.title('Frequency filtering result of FIR cascade filter')        

    def main(self):
        if self.type == 1:
            self.FIR_direct_1()
        elif self.type == 2:
            self.FIR_cascade() 
        elif self.type == 3:
            self.FIR_linear_phase()  
        elif self.type == 0:
            self.FIR_direct_1()
            self.FIR_cascade()
            self.FIR_linear_phase()   
    

if __name__ == "__main__":
    print("START")
    result = chap_6(0)
    result.main()
    plt.show()
    # print('\n'*80)

