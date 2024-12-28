MIN_N = -100  # 最小的 n 值
MAX_N = 100   # 最大的 n 值

power2_table = {n: 2**n for n in range(MIN_N, MAX_N + 1)}

def power2n_d(n):
    """
    使用查表法計算 2^n
    :param n: 指數值 (整數)
    :return: 2^n 的結果
    """
    if n in power2_table:
        return power2_table[n]
    else:
        return 2**n
      
print(power2n_d(10))  
print(power2n_d(-5)) 
print(power2n_d(150))  
