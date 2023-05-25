import pandas as pd
import numpy as np
from classify import classifier, init


if __name__ == '__main__':
    df1 = init()
    classifier(df1)