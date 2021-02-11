import numpy as np

def r4beta(shape1, shape2, a, b, size):
    x = np.random.beta(shape1, shape2, size)
    return (b - a) * x + a

def get_log_beta_pdf(slip, guess):
    # beta分布的对数概率密度函数
    return np.log(0.6 - guess) + np.log(0.6 - slip)

def get_log_normal_pdf(x):
    # 正态分布的对数概率密度函数
    return x ** 2 * -0.5

def get_log_lognormal_pdf(x):
    # 对数正态分布的对数概率密度函数
    return np.log(1.0 / x) + get_log_normal_pd(np.log(x))
