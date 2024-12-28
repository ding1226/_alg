import numpy as np

def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

def riemann_integration(n=100):
    dx = 1 / n
    dy = 1 / n
    dz = 1 / n
    
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = (i + 0.5) * dx
                y = (j + 0.5) * dy
                z = (k + 0.5) * dz
                total += f(x, y, z) * dx * dy * dz
    return total

def monte_carlo_integration(num_samples=100000):
    samples_x = np.random.uniform(0, 1, num_samples)
    samples_y = np.random.uniform(0, 1, num_samples)
    samples_z = np.random.uniform(0, 1, num_samples)
    
    function_values = f(samples_x, samples_y, samples_z)
    volume = 1 
    integral = np.mean(function_values) * volume
    return integral

if __name__ == "__main__":

    n = 100  
    result_riemann = riemann_integration(n)
    print(f"用黎曼積分法計算結果 (n={n}): {result_riemann}")
    
    # 用蒙地卡羅法
    num_samples = 100000  # 隨機樣本數
    result_monte_carlo = monte_carlo_integration(num_samples)
    print(f"用蒙地卡羅法計算結果 (樣本數={num_samples}): {result_monte_carlo}")
