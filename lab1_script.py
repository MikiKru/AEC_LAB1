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


object = SignalAnalysis()
# plot first returned value
object.signal_plot(object.signals_generator()[0])
# plot scond returned value
object.signal_plot(object.signals_generator()[1])


