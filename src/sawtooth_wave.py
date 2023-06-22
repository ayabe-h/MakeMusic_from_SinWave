import matplotlib.pylab as plt
import numpy as np
import os

Fs = 22100.0                                            # サンプリング周波数
Fc = 262                                                # 周波数
dur = 1                                                 # 生成時間
n = 100                                                 # 次数
Amp = 0.6                                               # 振幅
delta = 1.0 / Fs                                        # サンプリング間隔
Nmax = Fs * dur                                         # サンプル点の数
t = np.arange(Nmax) * delta                             # t軸の生成点
sawtooth_wave = np.zeros_like(t)                        # 鋸波を初期化
for i in range(1, n+1):
    harmonic = i
    sawtooth_wave += Amp * (1 / harmonic) * np.sin(2.0 * np.pi * Fc * harmonic * t)
    
current_path = os.path.dirname(__file__)                # ファイルのパス
plt.figure()
plt.plot(t[-512:], sawtooth_wave[-512:])
plt.savefig(current_path+"\\..\\img\\sawtooth_wave.png")
