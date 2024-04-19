from MonteCarlo import MonteCarlo
import pandas as pd

if __name__ == '__main__':
    mc = MonteCarlo(pd.read_excel('dados_brutos.xlsx'))
    mc.run()