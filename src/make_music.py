from scipy.io.wavfile import write
import numpy as np
import os


class GenFreq:

    def __init__(self, Fsample=44100.0, duration=1.0, sound = "normal"):
        # Fs はサンプリング周波数(Hz)，dur は持続時間(秒)
        self.Fcs = {
            "C": 262.0,#ド
            "C#":277.0,
            "D": 294.0,#レ
            "D#":311.0,
            "E": 330.0,#ミ
            "F": 349.0,#ファ
            "F#":370.0,
            "G": 392.0,#ソ
            "G#":415.0,
            "A": 440.0,#ラ
            "A#":466.0,
            "B": 494.0,#シ
            "C5":523.0,#ド
            "C5#":554.0,
            "D5":587.0,#レ
            "D5#":622.0,
        }
        self.Fs = Fsample                                   # サンプリング周波数
        delta = 1.0 / Fsample                               # 間隔
        self.dur = duration                                 # 時間
        self.N = int(duration * Fsample)                    # 音の長さ
        self.t = np.arange(self.N) * delta                  # 時間刻み
        self.x = np.zeros(self.N)                           # 音信号
        self.sound = sound                                  # 音の種類

    def getSound(self):
        # 波形データ配列を返す
        return self.x

    def getLen(self):
        # データ配列長を返す
        return self.N

    def setTone(self, code="C", Amp=1.0):
        # 音を設定する
        if(code != ""):
            if(self.sound == "normal"):
              # 正弦波
                f = self.Fcs[code]
                self.x = Amp * np.sin(2.0 * np.pi * f * self.t)
            elif(self.sound == "triangle"):
              # 三角波
                n = 100
                f = self.Fcs[code]
                for i in range(1, n+1):
                    harmonic = (2*i - 1)**2
                    self.x += Amp  /harmonic * np.sin(2.0 * np.pi * f * harmonic * self.t)
            elif(self.sound == "square"):
              # 矩形波
                n = 100
                f = self.Fcs[code]
                for i in range(1, n+1):
                    harmonic = 2*i - 1
                    self.x += Amp * (1 / harmonic) * np.sin(2.0 * np.pi * f * harmonic * self.t)
            elif(self.sound =="sawtooth"):
              # 鋸波
                n = 100
                f = self.Fcs[code]
                for i in range(1, n+1):
                    harmonic = i
                    self.x += Amp * (1 / harmonic) * np.sin(2.0 * np.pi * f * harmonic * self.t)
                    
    def normalize(self):
        # 音の振幅範囲を [-1, 1] に設定
        xmax = np.abs(self.x).max()
        self.x /= xmax

    def __add__(self, other):
        # 音をつなげる
        if isinstance(other, self.__class__) and self.Fs == other.Fs:
            tmp = GenFreq(self.Fs, self.dur + other.dur)
            tmp.x = np.hstack((self.x, other.x))
            return tmp
        else:  # サンプリング周波数違うときは足せないのでエラーを発出
            raise NotImplementedError()
        
    def __mul__(self, code="C", Amp=1.0):
        # 音を重ねて和音にする
        f = self.Fcs[code]
        self.x += Amp * np.sin(2.0 * np.pi * f * self.t)



if __name__ == "__main__":
    ########################################################
    # 音のパターンを定義するリスト（「ビッグブリッヂの死闘」）
    pattern = [
        ("F", 0.2),
        ("F", 0.2),
        ("", 0.2),
        ("F", 0.2),
        ("G#", 0.2),
        ("F", 0.2),
        ("",0.2),
        ("F", 0.2),
        ("G#",0.2),
        ("F",0.2),
        ("A#",0.2),
        ("B", 0.2),
        ("A#",0.2),
        ("G#", 0.2),
        ("F", 0.2),
        ("D#", 0.2),
        ("F", 0.2),
        ("F", 0.2),
        ("", 0.2),
        ("F", 0.2),
        ("G#", 0.2),
        ("G",0.2),
        ("F", 0.5),
        ("", 1.5),
        
        ("F",0.2),
        ("G",0.2),
        ("G#",0.2),
        ("F",0.2),
        ("A#",0.2),
        ("G#",0.2),
        ("G",0.2),
        ("F",0.2),
        ("C5",0.2),
        ("F",0.2),
        ("C5#",0.2),
        ("F",0.2),
        ("C5",0.2),
        ("G#",0.4),
        ("",0.01),
        ("G#",0.2),
        ("A#",0.2),
        ("D#",0.2),
        ("C5",0.2),
        ("D#",0.2),
        ("A#",0.2),
        ("G",0.4),
        ("",0.01),
        ("G",0.2),
        ("G#",0.2),
        ("G",0.2),
        ("F",0.2),
        ("G",0.2),
        ("G#",0.2),
        ("A#",0.2),
        ("G#",0.2),
        ("G",0.2),
        
        ("F",0.2),
        ("G",0.2),
        ("G#",0.2),
        ("F",0.2),
        ("A#",0.2),
        ("G#",0.2),
        ("G",0.2),
        ("F",0.2),
        ("C5",0.2),
        ("F",0.2),
        ("C5#",0.2),
        ("F",0.2),
        ("C5",0.2),
        ("G#",0.4),
        ("",0.01),
        ("G#",0.2),
        ("A#",0.2),
        ("D#",0.2),
        ("C5",0.2),
        ("D#",0.2),
        ("A#",0.2),
        ("G",0.4),
        ("",0.01),
        ("G",0.2),
        ("G#",0.2),
        ("A#",0.2),
        ("C5",0.2),
        ("C5#",0.2),
        ("D5#",0.2),
        ("C5#",0.2),
        ("C5",0.2),
        ("C5#",0.2),
        ("D5#",1.5)
    ]
    ########################################################
    Fs = 44100.0  # サンプリング周波数
    v = GenFreq(Fs, duration=0)  # 空の音インスタンスを作る

    for tone, duration in pattern:
        t = GenFreq(Fs, duration=duration, sound= "square")  # 矩形波で音を生成
        t.setTone(code=tone)
        v += t  # 音を加算していく
    current_path = os.path.dirname(__file__)
    fname2 = current_path+"\\..\\wav\\bigbridge.wav"
    v.normalize()
    write(fname2, int(Fs), v.getSound().astype("float32"))
