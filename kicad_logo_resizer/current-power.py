v = 5
def calculate(r):
    I = 5 / r
    P = v * I
    print(f'current: {I}\tpower: {P}')

while True:
    try:
        r = float(input())
        calculate(r)
    except:
        pass
