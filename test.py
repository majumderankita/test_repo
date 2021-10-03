import numpy as np
import pandas as pd

def print_hi(name,a):
    print(f'Hi, {name} {a}')

if __name__ == '__main__':
    a = np.random.randint(10)
    print_hi('PyCharm',a)

    mydataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
    }
    myvar = pd.DataFrame(mydataset)
    print(myvar)