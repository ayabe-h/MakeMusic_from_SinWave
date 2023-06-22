import matplotlib.pylab as plt
import numpy as np
import os

Fs = 22100.0                                            # サンプリング周波数
Fc = 262                                                # 周波数
dur = 1                                                 # 生成時間
Amp = 1.0                                               # 振幅 
delta = 1.0 / Fs                                        # サンプリング間隔
Nmax = Fs * dur                                         # サンプル点の数
t = np.arange(Nmax) * delta                             # t軸の生成点
sin_wave = Amp * np.sin(2.0 * np.pi * Fc * t)           # 正弦波の生成点
current_path = os.path.dirname(__file__)                # ファイルのパス
plt.figure()
plt.plot(t[-512:], sin_wave[-512:])
plt.savefig(current_path+"\\..\\img\\sin_wave.png")
