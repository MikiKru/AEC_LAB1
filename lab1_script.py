from math import sin


class SignalAnalysis:
    def signals_generator(self):
        self.sinus_signal = []
        i = 0
        while (len(self.sinus_signal) < 1000):
            self.sinus_signal.append(sin(i/120))
            i += 1


