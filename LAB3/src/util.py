import numpy as np

def ThreeDIM(x,y,z):
    return np.sqrt(pow(x,2)+pow(y,2)+pow(z,2))

if __name__ == "__main__":
    print(ThreeDIM(4,0,0))