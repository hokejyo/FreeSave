# -*- coding: utf-8 -*-


import os
import sys
import shutil
import construct
from pathlib import Path
from functools import partial


def env_to_path(_ENV) -> Path:
    """
    @brief      得到当前用户下该环境路径的绝对路径

    @param      _ENV  环境路径

    @return     绝对路径
    """
    true_path = os.getenv(_ENV)
    if true_path.endswith(':'):
        true_path += '\\'
    return Path(true_path)


def env_join_path(_ENV, repath) -> Path:
    """
    @brief      连接环境路径和相对路径

    @param      _ENV    环境路径值
    @param      repath  相对路径

    @return     连接后的绝对路径
    """
    abs_path = env_to_path(_ENV)/repath
    return abs_path
