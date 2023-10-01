class StateMachine:

    # Initialize 
    def start(self):
        self.state = self.startState

    # Step through the input
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    # Loop through the input 
    def feeder(self, inputs):
        self.start()
        outputs = [self.step(inp) for inp in inputs]
        return outputs[-1]
    
class TextSeq(StateMachine):
    
    startState = 0
    
    def getNextValues(self, state, inp):
        if state == 0 and inp == 'bagaimana cuaca di bandung?':
            return (1, "Cuaca di bandung sekarang sedang berawan")
        elif state == 0 and inp == 'rekomendasi makanan di bandung':
            return (1, "sate, seblak, cireng, dsb")
        elif state == 1 and inp == 'apakah akan turun hujan?':
            return (2, "Perkiraan cuaca 1 jam kedepan tidak turun hujan")
        elif state == 1 and inp == 'warung seblak terdekat':
            return (2, "warung seblak terdekat ada di jalan babakan jeruk")
        elif state == 2 and inp == 'saya mau bertanya yang lain':
            return (0, "Oke silahkan bertanya lagi")
        else:
            return (3, "Terimakasih")


InSeq = TextSeq()

print()
A = []
Q = str(input("Apa pertanyaan anda: ").lower())
A.append(Q)
while (Q != "terimakasih"):
    x = InSeq.feeder(A)
    print(x)
    print()
    Q = str(input("Apa pertanyaan anda: ").lower())
    A.append(Q)
    print()


