'''
Date: 1) 2021.12.21 , 2) 2022.02.15
Title: 제 1형 선형 FIR 필터 Study
By: Kang Jin Seong
'''

import numpy as np
from scipy import signal

import matplotlib.pyplot as plt
from matplotlib import patches, rcParams

class linear_FIR_filter_study:
    def zplane(self,b,a):
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

    def Type1(self):
        hn = np.array([-4,1,-1,-2,5,6,5,-2,-1,1,-4])    #임펄스 응답
        M = 11; n = np.arange(0,M)  # 필터길이, 시퀀스 축
        Omega = np.linspace(0, np.pi, 1000) #0에서 3.14까지 1000등분

        H = np.arange(1000); H = np.float64(H)  #주파수 응답
        for x in range(1000):
            H[x] = hn[5]*np.cos(Omega[x]*0) + 2*hn[4]*np.cos(Omega[x]*1)\
                    +2*hn[3]*np.cos(Omega[x]*2)+2*hn[2]*np.cos(Omega[x]*3)\
                    +2*hn[1]*np.cos(Omega[x]*4)+2*hn[0]*np.cos(Omega[x]*5)

        amplitude = H   #진폭응답
        magnitude = abs(H)  #크기응답
        phase = np.angle(H)*180/np.pi   #위상응답

        plt.figure()
        plt.subplot(2,2,1); plt.stem(n,hn,'b');plt.grid()
        plt.title('Impulse REsponse')
        plt.subplot(2,2,2); plt.plot(Omega/np.pi, magnitude, 'g'); plt.grid()
        plt.ylabel('Magnitude');plt.title('magnitude Response')
        plt.subplot(2,2,4); plt.plot(Omega/np.pi, phase, 'b'); plt.grid()
        plt.ylabel('phsae');plt.xlabel('Frequency in pi radians')
        plt.title('Phsae Response')
        plt.tight_layout()

        plt.figure()
        plt.subplot(2,2,2); an = np.array([1,0]); self.zplane(hn,an); plt.grid()
        plt.title('Pole - Zero Diagram')
        plt.tight_layout()

    def Type2(self):
        hn = np.array([-4,1,-1,-2,5,6,6,5,-2,-1,1,-4])    #임펄스 응답
        M = 12; n = np.arange(0,M)  # 필터길이, 시퀀스 축
        Omega = np.linspace(0, np.pi, 1000) #0에서 3.14까지 1000등분       
        
        H = np.arange(1000); H = np.float64(H)  #주파수 응답
        for x in range(1000):
            H[x] = 2*hn[5]*np.cos(Omega[x]*(1-1/2)) + 2*hn[4]*np.cos(Omega[x]*(2-1/2))\
                    +2*hn[3]*np.cos(Omega[x]*(3-1/2))+2*hn[2]*np.cos(Omega[x]*(4-1/2))\
                    +2*hn[1]*np.cos(Omega[x]*(5-1/2))+2*hn[0]*np.cos(Omega[x]*(6-1/2))

        amplitude = H   #진폭응답
        magnitude = abs(H)  #크기응답
        phase = np.angle(H)*180/np.pi   #위상응답

        plt.figure()
        plt.subplot(2,2,1); plt.stem(n,hn,'b');plt.grid()
        plt.title('Impulse REsponse')
        plt.subplot(2,2,2); plt.plot(Omega/np.pi, magnitude, 'g'); plt.grid()
        plt.ylabel('Magnitude');plt.title('magnitude Response')
        plt.subplot(2,2,4); plt.plot(Omega/np.pi, phase, 'b'); plt.grid()
        plt.ylabel('phsae');plt.xlabel('Frequency in pi radians')
        plt.title('Phsae Response')
        plt.tight_layout()

        plt.figure()
        plt.subplot(2,2,2); an = np.array([1,0]); self.zplane(hn,an); plt.grid()
        plt.title('Pole - Zero Diagram')
        plt.tight_layout()      
                    
    def Type3(self):
        hn = np.array([-4,1,-1,-2,5,0,-5,2,1,-1,+4])    #임펄스 응답
        M = 11; n = np.arange(0,M)  # 필터길이, 시퀀스 축
        Omega = np.linspace(0, np.pi, 1000) #0에서 3.14까지 1000등분       
        
        H = np.arange(1000); H = np.float64(H)  #주파수 응답
        for x in range(1000):
            H[x] = 2*hn[4]*np.sin(Omega[x]) + 2*hn[3]*np.sin(2*Omega[x])\
                    +2*hn[2]*np.sin(3*Omega[x])+2*hn[1]*np.sin(4*Omega[x])\
                    +2*hn[0]*np.sin(5*Omega[x])

        amplitude = H   #진폭응답
        magnitude = abs(H)  #크기응답
        phase = np.angle(H)*180/np.pi   #위상응답

        plt.figure()
        plt.subplot(2,2,1); plt.stem(n,hn,'b');plt.grid()
        plt.title('Impulse REsponse')
        plt.subplot(2,2,2); plt.plot(Omega/np.pi, magnitude, 'g'); plt.grid()
        plt.ylabel('Magnitude');plt.title('magnitude Response')
        plt.subplot(2,2,4); plt.plot(Omega/np.pi, phase, 'b'); plt.grid()
        plt.ylabel('phsae');plt.xlabel('Frequency in pi radians')
        plt.title('Phsae Response')
        plt.tight_layout()

        plt.figure()
        plt.subplot(2,2,2); an = np.array([1,0]); self.zplane(hn,an); plt.grid()
        plt.title('Pole - Zero Diagram')
        plt.tight_layout()  

    def Type4(self):
        hn = np.array([-4,1,-1,-2,5,6,-6,-5,2,1,-1,4])    #임펄스 응답
        M = 12; n = np.arange(0,M)  # 필터길이, 시퀀스 축
        Omega = np.linspace(0, np.pi, 1000) #0에서 3.14까지 1000등분       
        
        H = np.arange(1000); H = np.float64(H)  #주파수 응답
        for x in range(1000):
            H[x] = 2*hn[5]*np.sin(Omega[x]*(1-1/2)) + 2*hn[4]*np.sin(Omega[x]*(2-1/2))\
                    +2*hn[3]*np.sin(Omega[x]*(3-1/2))+2*hn[2]*np.sin(Omega[x]*(4-1/2))\
                    +2*hn[1]*np.sin(Omega[x]*(5-1/2))+2*hn[0]*np.sin(Omega[x]*(6-1/2))

        amplitude = H   #진폭응답
        magnitude = abs(H)  #크기응답
        phase = np.angle(H)*180/np.pi   #위상응답

        plt.figure()
        plt.subplot(2,2,1); plt.stem(n,hn,'b');plt.grid()
        plt.title('Impulse REsponse')
        plt.subplot(2,2,2); plt.plot(Omega/np.pi, magnitude, 'g'); plt.grid()
        plt.ylabel('Magnitude');plt.title('magnitude Response')
        plt.subplot(2,2,4); plt.plot(Omega/np.pi, phase, 'b'); plt.grid()
        plt.ylabel('phsae');plt.xlabel('Frequency in pi radians')
        plt.title('Phsae Response')
        plt.tight_layout()

        plt.figure()
        plt.subplot(2,2,2); an = np.array([1,0]); self.zplane(hn,an); plt.grid()
        plt.title('Pole - Zero Diagram')
        plt.tight_layout() 

    def main(self):
        # self.Type1()
        # self.Type2()
        self.Type3()
        self.Type4()


if __name__ == "__main__":
    plt.close()
    result = linear_FIR_filter_study()
    result.main()
    plt.show()
      