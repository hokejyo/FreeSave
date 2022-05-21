# -*- coding: utf-8 -*-

from utils import *


class SysPaths(object):

    ENV_LS = [
        'ALLUSERSPROFILE',
        'APPDATA',
        'COMMONPROGRAMFILES',
        'COMMONPROGRAMFILES(x86)',
        'LOCALAPPDATA',
        'PROGRAMDATA',
        'PROGRAMFILES',
        'PROGRAMFILES(X86)',
        'PUBLIC',
        'TEMP',
        'TMP',
        'USERPROFILE',
        # 'COMSPEC',
        'HOMEDRIVE',
        'SystemDrive',
        # 'HOMEPATH',
        'SystemRoot',
        'WINDIR'
    ]

    def __init__(self, _path):
        self._path = Path(_path)

    @property
    def env_repaths(self) -> dict:
        """
        @brief      分割路径为环境路径和相对路径

        @return     可能的 系统路径：相对路径 字典
        """
        _parents = [str(_parent) for _parent in self._path.parents]
        env_repaths_dict_ = {}
        for _ENV, true_path in self.env_truepaths.items():
            if str(true_path) in _parents:
                repath = self._path.relative_to(true_path)
                env_repaths_dict_[_ENV] = repath
        return env_repaths_dict_

    @property
    def env_truepaths(self) -> dict:
        """
        @brief      获取环境路径在当前用户下的绝对路径

        @return     环境路径->绝对路径 字典
        """
        env_paths_dict_ = {}
        for _ENV in self.ENV_LS:
            env_paths_dict_[_ENV] = env_to_path(_ENV)
        return env_paths_dict_
