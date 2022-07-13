import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp


def IIR_direct_1(x):    # 제1형 직접형 IIR 필터
    y = [0] * tn
    v = [0] * tn
    for n in range(4, len(x)):
        v[n] = 1/16*x[n] - 3/16*x[n-1] + 11/16*x[n-2] -27/16*x[n-3] + 18/16*x[n-4]
        y[n] = v[n] -12/16*y[n-1] -2/16*y[n-2] + 4/16*y[n-3] + 1/16*y[n-4]

    return y

def IIR_direct_2(x):
    pass

def main():
    # # IIR 필터 제1 직접형 구현
    # tn = 5000   # 총 데이터 샘플수
    # t = np.linspace(0,1,tn) # x축 설정
    # input = chirp(t, f0 = 10, t1 = 0.2, f1 = 500, method = 'linear')    #처프신호 발생
    # IIR_direct_1_output = [0]*tn    #필터 출력 어레이 설정
    # IIR_direct_1_output = IIR_direct_1(input)    #필터 출력 계산
    # plt.plot(IIR_direct_1_output, "b"); plt.xlim(0,5000)
    # plt.xlabel("samples, frequency[0~500Hz]");plt.grid()
    # plt.title("frequency filtering result of IIR Direct-1 filter")
    # plt.show() 
    pass

if __name__ == "__main__":
    print("START")
    main()
      