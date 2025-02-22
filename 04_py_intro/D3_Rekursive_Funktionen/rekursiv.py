from time import time


def M(n: int) -> int:
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10

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