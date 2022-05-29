# -*- coding: utf-8 -*-

from utils import *
from qtcore import *
from freesavegui import FreeSaveGUI


class FreeSave(object):

    def __init__(self):
        self.ui = FreeSaveGUI()

    def default_migrate_to_custom(_default, _custom):
        """
        @brief      迁移并创建软链接

        @param      _default   源路径
        @param      _custom   目标路径
        """
        _default = Path(_default)
        _custom = Path(_custom)
        if _default.exists():
            if _custom.exists():
                self.emit_msg('备份文件')
            _default.move_as(_custom)
            os.symlink(_custom, _default)
        else:
            self.emit_msg('源文件/文件夹不存在')

    def custom_relink_to_default(_custom, _default):
        """
        @brief      创建软链接

        @param      _custom   源路径
        @param      _default   目标路径
        """
        _custom = Path(_custom)
        _default = Path(_default)
        if _custom.exists():
            if _default.exists():
                self.emit_msg('备份文件')
            os.symlink(_custom, _default)
        else:
            self.emit_msg('源文件/文件夹不存在')

    def emit_msg(self, _str, level='info'):
        print(_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    freesave = FreeSave()
    apply_stylesheet(app, theme='light_teal.xml')
    freesave.ui.show()
    sys.exit(app.exec())
