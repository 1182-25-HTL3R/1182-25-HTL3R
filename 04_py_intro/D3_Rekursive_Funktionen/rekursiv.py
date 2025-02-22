from time import time
from typing import Tuple


def M(n: int, tiefe: int = 0) -> Tuple[int, int]:
    if n <= 100:
        m1 = M(n + 11, tiefe + 1)
        return M(m1[0], m1[1] + 1)
    else:
        return n - 10, tiefe

if __name__ == '__main__':
    t0 = time()

    m_list = []
    for i in range(200):
        m_list.append(M(i))


    m_dict = dict()
    for i in range(200):
        m_dict[i] = M(i)

    print(str(time()-t0) + "sek")
    print(m_list)
    print(m_dict)

    # bemerkenswert ist, dass alle Werte zwischen 0-101 in der Funktion M den Wert 91 zurückliefern
    # braucht ca 0.001 sek
    # für n = 1 war die Rekursionstiefe maximal und zwar 202
