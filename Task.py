import random
import math

def cüt_rəqəmləri_kvadrata_yüksəlt():
    rəqəmlər = []
    for _ in range(20):
        rəqəm = random.randint(20, 50)
        rəqəmlər.append(rəqəm)

    cüt_rəqəmlər = [rəqəm for rəqəm in rəqəmlər if rəqəm % 2 == 0]

    cüt_rəqəmlər_kvadrat = [math.pow(rəqəm, 2) for rəqəm in cüt_rəqəmlər]

    return cüt_rəqəmlər_kvadrat

print(cüt_rəqəmləri_kvadrata_yüksəlt())
