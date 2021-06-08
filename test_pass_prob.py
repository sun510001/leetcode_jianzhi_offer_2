# -*- coding:utf-8 -*-
"""
一份试卷共100题, 每题1分, 小明答对每一题的概率均为0.8且相互独立, 为使小明答该试卷的及格率至少为0.8, 该试卷的及格分数线最高可以设多少分(整数)?
二项分布
"""
from __future__ import division
from scipy.special import comb


def comb_1(n, m):
    """
    从n个不同元素中取出m(m≤n）个元素的所有组合的个数
    :param m:
    :param n:
    :return:
    """
    perm = 1
    for i in range(n-m+1, n+1):
        perm *= i
    m_fac = 1
    for j in range(1, m+1):
        m_fac *= j
    return perm / m_fac


def pass_line(n, p, a):
    k = 0
    exp = 0
    while True:
        i = k
        print(f'n: {n}; i: {i}; comb: {comb(n,i)}; comb_1: {comb_1(n,i)}')
        exp += comb_1(n, i) * (a ** i) * ((1 - a) ** (n - i))
        print(exp)
        if exp > p:
            return k - 1
        k += 1


if __name__ == '__main__':
    problems = 100
    property = 0.8
    auc = 0.8
    result = pass_line(problems, 1 - property, auc)
    print(result)
