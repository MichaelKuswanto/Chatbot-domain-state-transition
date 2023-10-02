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
            return (2, "sate, seblak, cireng, dsb")
        elif state == 1 and inp == 'apakah akan turun hujan?':
            return (1.1, "Perkiraan cuaca 1 jam kedepan tidak turun hujan")
        elif state == 1 and inp == 'apakah cuaca akan cerah?':
            return (1.2, "Perkiraan cuaca 1 jam kedepan cerah")
        elif state == 2 and inp == 'warung seblak terdekat':
            return (2.1, "warung seblak terdekat ada di jalan babakan jeruk")
        elif state == 2 and inp == 'penjual sate terdekat':
            return (2.2, "penjual sate terdekat ada di surya sumantri")
        elif state == 2 and inp == 'penjual cireng terdekat':
            return (2.3, "penjual cireng terdekat ada di jalan cibogo atas")
        elif (state == 1.1 or state == 1.2 or state == 2.1 or state == 2.2 or state == 2.3) and inp == 'saya mau bertanya yang lain':
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


