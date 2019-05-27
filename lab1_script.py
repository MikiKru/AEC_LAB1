from math import sin
import matplotlib.pyplot as plt
import random


class SignalAnalysis:
    def signals_generator(self):
        # sinus generation
        self.sinus_signal = []
        # random generation
        self.random_signal = []
        i = 0
        while (len(self.sinus_signal) < 1000):
            self.sinus_signal.append(sin(i/120))
            self.random_signal.append(random.random())
            i += 1
        return self.sinus_signal, self.random_signal
    def signal_plot(self, signal):
        plt.plot(range(0,1000,1), signal)
        plt.show()
    def addSignals(self, signal1, signal2):
        resultSignal = []
        i = 0
        while (len(resultSignal) < 1000):
            resultSignal.append(signal1[i] + signal2[i])
            i += 1
        return resultSignal


object = SignalAnalysis()
# plot first returned value
# object.signal_plot(object.signals_generator()[0])
# plot second returned value
# object.signal_plot(object.signals_generator()[1])
# adding two sinus
sinus = object.signals_generator()[0]
random = object.signals_generator()[1]
object.signal_plot(object.addSignals(sinus,sinus))
# adding sinus and random
object.signal_plot(object.addSignals(sinus,random))
