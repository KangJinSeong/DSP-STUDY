'''
Date: 2022.02.08
Title: 디지털 필터 구조 설계(design) 및 구현(Implementation)
By: Kang Jin Seong
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftshift, fft
from scipy.signal import chirp

class chap_6:
    def __init__(self, select):
        self.type = select 

    def IIR_direct_1(self):    # 제1형 직접형 IIR 필터
        tn = 5000   #총 데이터 샘플 수
        t = np.linspace(0, 1, tn)   # x축 설정
        input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method='linear')
        y = [0] * tn
        v = [0] * tn
        for n in range(4, len(input)):
            v[n] = 1/16*input[n] - 3/16*input[n-1] + 11/16*input[n-2] -27/16*input[n-3] + 18/16*input[n-4]
            y[n] = v[n] -12/16*y[n-1] -2/16*y[n-2] + 4/16*y[n-3] + 1/16*y[n-4]
                
        # IIR 필터 제1 직접형 구현
        fs = 1e3    #1kHz
        # IIR_direct_1_output = [0]*tn    #필터 출력 어레이 설정
        IIR_direct_1_output = y    #필터 출력 계산
        NFFT = len(IIR_direct_1_output)
        f = np.arange(start = -NFFT/2, stop = NFFT/2)*(fs/NFFT)
        M = fftshift(fft(IIR_direct_1_output,NFFT))/NFFT
        plt.figure()
        plt.subplot(3,1,1)
        plt.plot(t,input)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid();plt.ylabel("Amplitude")
        plt.title("Chirp Signal")       
        plt.subplot(3,1,2)
        plt.plot(IIR_direct_1_output, "b"); plt.xlim(0,5000)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid()
        plt.title("frequency filtering result of IIR Direct-1 filter")
        plt.subplot(3,1,3)
        plt.plot(f,M);plt.grid()
        plt.tight_layout()

    def IIR_direct_2(self):    # 제2형 직접형 IIR 필터
        fs = 1e3    #1kHz
        tn = 5000   #총 데이터 샘플 수
        t = np.linspace(0, 1, tn)   # x축 설정
        input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method='linear')
        y = [0] * tn
        v = [0] * tn
        for n in range(4, len(input)):
           v[n] = input[n] - 12/16*v[n-1] - 2/16*v[n-2] +4/16*v[n-3] + 1/16*v[n-4]
           y[n] = 1/16*v[n] -3/16*v[n-1] +11/16*v[n-2] - 27/16*v[n-3] + 18/16*v[n-4]
        IIR_direct_2_output = y    #필터 출력 계산
        NFFT = len(IIR_direct_2_output)
        f = np.arange(start = -NFFT/2, stop = NFFT/2)*(fs/NFFT)
        M = fftshift(fft(IIR_direct_2_output,NFFT))/NFFT
        plt.figure()
        plt.subplot(3,1,1)
        plt.plot(t,input)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid();plt.ylabel("Amplitude")
        plt.title("Chirp Signal")       
        plt.subplot(3,1,2)
        plt.plot(IIR_direct_2_output, "b"); plt.xlim(0,5000)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid()
        plt.title("frequency filtering result of IIR Direct-2 filter")
        plt.subplot(3,1,3)
        plt.plot(f,M);plt.grid()
        plt.tight_layout()             

    def IIR_transposed_direct_2(self):    # 전치 제 2형 직접형 IIR 필터
        tn = 5000   #총 데이터 샘플 수
        t = np.linspace(0, 1, tn)   # x축 설정
        input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method='linear')
        y = [0] * tn
        v = [0] * tn
        for n in range(4, len(input)):
           y[n] = 1/16*input[n]+(-3/16*input[n-1]-12/16*y[n-1])+(11/16*input[n-2]-2/16*y[n-2])+(-27/16*input[n-3]+4/16*y[n-3])+(18/16*input[n-4]+1/16*y[n-4])
        IIR_transposed_direct_2_output = y    #필터 출력 계산
        plt.figure()
        plt.subplot(2,1,1)
        plt.plot(t,input)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid();plt.ylabel("Amplitude")
        plt.title("Chirp Signal")       
        plt.subplot(2,1,2)
        plt.plot(IIR_transposed_direct_2_output, "b"); plt.xlim(0,5000)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid()
        plt.title("frequency filtering result of IIR Transposed Direct-2 filter")        
        plt.tight_layout()

    def IIR_cascade(self):  # 직렬형 구조
        tn = 5000   #총 데이터 샘플 수
        t = np.linspace(0, 1, tn)   # x축 설정
        input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method='linear')
        y = [0] * tn
        v = [0] * tn
        for n in range(4, len(input)):
            v[n] = input[n]-v[n-1]+(9*input[n-2]-0.5*v[n-2])
            y[n] = 1/16*(v[n]+(-3*v[n-1]+0.25*y[n-1]) + (2*v[n-2]+0.125*y[n-2]))
        IIR_cascade_output = y    #필터 출력 계산
        plt.figure()
        plt.subplot(2,1,1)
        plt.plot(t,input)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid();plt.ylabel("Amplitude")
        plt.title("Chirp Signal")       
        plt.subplot(2,1,2)
        plt.plot(IIR_cascade_output, "b"); plt.xlim(0,5000)
        plt.xlabel("samples, frequency[0~500Hz]");plt.grid()
        plt.title("frequency filtering result of IIR Cascade filter")        
        plt.tight_layout()       

    def main(self):
        if self.type == 1:
            self.IIR_direct_1()
        elif self.type == 2:
            self.IIR_direct_2()
        elif self.type == 3:
            self.IIR_transposed_direct_2()
        elif self.type == 4:
            self.IIR_cascade()    
        elif self.type == 0:
            self.IIR_direct_1()
            self.IIR_direct_2()
            self.IIR_transposed_direct_2()
            self.IIR_cascade()  
    

if __name__ == "__main__":
    print("START")
    result = chap_6(0)
    result.main()
    plt.show()
    # print('\n'*80)
      