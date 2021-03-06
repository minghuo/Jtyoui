#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/3/11 11:43
# @Author: Jtyoui@qq.com
import functools
import re

"""
装饰器模式
"""


def replace_regular(re_, replace_):
    """
    根据正则来修改参数
    :param re_: 匹配的正则
    :param replace_: 替换正则的数据
    :return: 被替换完毕的参数
    """
    r = re.compile(re_)

    def remove_replace(fun):

        @functools.wraps(fun)
        def wraps(*args, **kwargs):
            args_, kwargs_ = list(args), {}
            for i in range(len(args)):
                if isinstance(args[i], str):
                    args_[i] = r.sub(replace_, args[i])
                else:
                    args_[i] = args[i]
            for k, v in kwargs.items():
                if isinstance(v, str):
                    kwargs_.setdefault(k, r.sub(replace_, v))
                else:
                    kwargs_.setdefault(k, v)

            return fun(*args_, **kwargs_)

        return wraps

    return remove_replace


if __name__ == '__main__':
    from jtyoui.regular import Non_Chinese


    @replace_regular(' ', '')
    def remove_blank(a, b):
        print(a, b)


    @replace_regular(Non_Chinese, '')
    def remove_non_chinese(a, b):
        print(a, b)


    remove_blank('你好  吗?', b='我  很好!')
    remove_non_chinese('你好#$%76#%吗wore?', b='我$%787word很好!')
