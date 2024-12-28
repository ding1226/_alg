def my_permutations(elements, r=None):
    """
    自定義排列函數，返回所有長度為 r 的排列。
    
    :param elements: 可迭代對象，例如列表或字符串
    :param r: 排列的長度，默認為與 elements 的長度相同
    :return: 包含排列的列表
    """
    if r is None:
        r = len(elements)
    
    if r == 0:
        return [[]]
  
    if len(elements) == 0 or r > len(elements):
        return []
    
    result = []
    
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        for perm in my_permutations(remaining, r - 1):
            result.append([current] + perm)
    
    return result


if __name__ == "__main__":
    data = [1, 2, 3]
    r = 2
    permutations = my_permutations(data, r)
    
    print(f"元素: {data}, 排列長度: {r}")
    print("排列結果:")
    for perm in permutations:
        print(perm)
