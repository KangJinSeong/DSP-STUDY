'''
Date: 2021.12.27
Title: 창설계 관련한 FIR 필터 공부
By: Kang Jin Seong
'''

import numpy as np
from scipy import signal
from scipy.signal import chirp
import matplotlib.pyplot as plt


class window_study:
    def ideal_lp(self, Omega_c, M): #이상적인 LPF 임펄스 응답 구하는 함수
        alpha = (M-1)/2 #임펄스 응답의 중심
        nt = np.arange(0,M) #시퀀스 축
        n = nt-alpha    #시퀀스 이동
        fc = Omega_c/np.pi  #차단 주파수
        hd = fc*np.sinc(fc*n)   #이상적인 저역통과 필터의 임펄스 응답
        return hd

    def hanning_lowpass(self):
        Omega_p = 0.2*np.pi; Omega_s = 0.3*np.pi    #통과대역에지주파수, 저지대역에지주파수
        tr_widh = Omega_s - Omega_p #천이 대역폭
        M = int(np.ceil(6.6*np.pi/tr_widh))+1; print('M = ', M) # 창 길이
        Omega_c = (Omega_s+Omega_p)/2   #차단 주파수
        nt = np.arange(0,M) #시퀀스 축
        hd = self.ideal_lp(Omega_c, M)  # 이상적인 LPF 임펄스 응답
        wn = signal.hamming(M)  #해밍 창 함수
        hn = hd * wn    #유한 임펄스 응답
        nf,H = signal.freqz(hn) #주파수축, 주파수 응답
        H_dB = 20*np.log10(abs(H))  #주파수 응답(dB)

        plt.subplot(3,1,1); plt.stem(nt,hn,'b');plt.grid()
        plt.ylabel('h(n)');plt.xlabel('n');plt.xlim(0,M-1)
        plt.title('Impulse response, Frequency response, Freqeuency filtering result')

        plt.subplot(3,1,2);plt.plot(nf/np.pi,H_dB,'b');plt.grid();plt.xlim(0,1)
        plt.xlabel('frequency in pi radians'); plt.ylabel('Magnitude(dB)')

        t = np.linspace(0,1,5000)
        xn = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method = 'linear')   #처프 신호 생성
        yn = np.convolve(hn,xn) #컨볼루션으로 출력 생성
        
        plt.subplot(3,1,3);plt.plot(yn,'b');plt.xlim(0,5000)
        plt.xlabel('Samples(frequency(0~500[Hz]))'); plt.grid()
        plt.tight_layout()

    def hanning_highpass(self):
        Omega_p = 0.7*np.pi; Omega_s = 0.6*np.pi    #통과대역에지줖자수, 저지대역에지주파수
        tr_width = Omega_p - Omega_s    #천이 대역폭
        M = int(np.ceil(6.2*np.pi/tr_width)); print("M = ",M)   #창 길이
        Omega_c = (Omega_s + Omega_p)/2 # 차단 주파수
        nt = np.arange(0,M) #시퀀스 축
        hd = self.ideal_lp(np.pi, M) - self.ideal_lp(Omega_c,M) #이상적인 HPF 임펄스 응답
        wn = signal.hanning(M)  # 핸 창 함수
        hn = hd * wn    #유한 임펄스 응답
        nf,H = signal.freqz(hn) #주파수축, 주파수 응답
        H_dB = 20*np.log10(abs(H))  #주파수 응답(dB)

        plt.subplot(3,1,1); plt.stem(nt,hn,'b');plt.grid()
        plt.ylabel('h(n)');plt.xlabel('n');plt.xlim(0,M-1)
        plt.title('Impulse response, Frequency response, Freqeuency filtering result')

        plt.subplot(3,1,2);plt.plot(nf/np.pi,H_dB,'b');plt.grid();plt.xlim(0,1)
        plt.xlabel('frequency in pi radians'); plt.ylabel('Magnitude(dB)')

        t = np.linspace(0,1,5000)
        xn = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method = 'linear')   #처프 신호 생성
        yn = np.convolve(hn,xn) #컨볼루션으로 출력 생성
        
        plt.subplot(3,1,3);plt.plot(yn,'b');plt.xlim(0,5000)
        plt.xlabel('Samples(frequency(0~500[Hz]))'); plt.grid()
        plt.tight_layout()  
    def Blackmann_bandpass(self):
        Omega_s1 = 0.2*np.pi; Omega_p1 = 0.35*np.pi # 하위 저지대역과 통과대역에지 주파수
        Omega_p2 = 0.65*np.pi; Omega_s2 = 0.8*np.pi # 상위 통과대역과 저지대역에지 주파수
        tr_width = np.min([(Omega_p1 - Omega_s1), (Omega_s2 - Omega_p2)]) # 천이 대역폭
        M = int(np.ceil(11*np.pi/tr_width)) + 1; print("M = ", M)   # 창길이
        Omega_c1 = (Omega_s1 + Omega_p1)/2; Omega_c2 = (Omega_s2+Omega_p2)/2    #차단 주파수
        nt = np.arange(0,M) #시퀀스 축
        hd = self.ideal_lp(Omega_c2, M)-self.ideal_lp(Omega_c1, M)  #이상적인 LPF 임펄스 응답
        wn = signal.blackman(M) #블랙맨 창 함수
        hn = hd * wn    #유한 임펄스 응답
        nf,H = signal.freqz(hn) #주파수축, 주파수 응답
        H_dB = 20*np.log10(abs(H))  #주파수 응답(dB)

        plt.subplot(3,1,1); plt.stem(nt,hn,'b');plt.grid()
        plt.ylabel('h(n)');plt.xlabel('n');plt.xlim(0,M-1)
        plt.title('Impulse response, Frequency response, Freqeuency filtering result')

        plt.subplot(3,1,2);plt.plot(nf/np.pi,H_dB,'b');plt.grid();plt.xlim(0,1)
        plt.xlabel('frequency in pi radians'); plt.ylabel('Magnitude(dB)')

        t = np.linspace(0,1,5000)
        xn = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method = 'linear')   #처프 신호 생성
        yn = np.convolve(hn,xn) #컨볼루션으로 출력 생성
        
        plt.subplot(3,1,3);plt.plot(yn,'b');plt.xlim(0,5000)
        plt.xlabel('Samples(frequency(0~500[Hz]))'); plt.grid()
        plt.tight_layout()        

    def Kaiser_Bandstop(self):
        M  = 45 #창 길이
        As = 50 #저지대역 감쇠
        beta  = 0.1102 * (As - 8.7) #베타 값 계산
        nt = np.arange(0,M) #시퀀스 축

        Omega_c1=np.pi/3; Omega_c2 = np.pi*2/3  #하위 및 상위 차단 주파수
        hd = self.ideal_lp(Omega_c1, M) + (self.ideal_lp(np.pi, M)- self.ideal_lp(Omega_c2, M))     #임펄스 응답
        wn = signal.kaiser(M, beta) # 카이저 창 함수
        hn = hd * wn    # 유한 임펄스 응답

        nf,H = signal.freqz(hn) #주파수축, 주파수 응답
        H_dB = 20*np.log10(abs(H))  #주파수 응답(dB)

        plt.subplot(3,1,1); plt.stem(nt,hn,'b');plt.grid()
        plt.ylabel('h(n)');plt.xlabel('n');plt.xlim(0,M-1)
        plt.title('Impulse response, Frequency response, Freqeuency filtering result')

        plt.subplot(3,1,2);plt.plot(nf/np.pi,H_dB,'b');plt.grid();plt.xlim(0,1)
        plt.xlabel('frequency in pi radians'); plt.ylabel('Magnitude(dB)')

        t = np.linspace(0,1,5000)
        xn = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method = 'linear')   #처프 신호 생성
        yn = np.convolve(hn,xn) #컨볼루션으로 출력 생성
        
        plt.subplot(3,1,3);plt.plot(yn,'b');plt.xlim(0,5000)
        plt.xlabel('Samples(frequency(0~500[Hz]))'); plt.grid()
        plt.tight_layout()           

    def main(self):
        # self.hanning_lowpass()
        # self.hanning_highpass()
        # self.Blackmann_bandpass()
        self.Kaiser_Bandstop() 

if __name__ == "__main__":
    plt.close()
    result = window_study()
    result.main()
    plt.show() 