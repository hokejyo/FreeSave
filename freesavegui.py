# -*- coding: utf-8 -*-

from utils import *
from qtcore import *
from envpaths import EnvPaths


class FreeSaveGUI(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.resize(720, 480)
        self.setup_layouts()
        self.setup_connections()

    def setup_layouts(self):
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.mainlayout = QVBoxLayout()
        self.centralwidget.setLayout(self.mainlayout)

        self.setup_default_path()

        self.setup_choose_path_mode()

        self.setup_env_repath()

        self.setup_create_custom_area()

    def setup_connections(self):
        self.default_path_btn.clicked.connect(self.choose_default_path)
        self.default_path_ledt.textChanged.connect(self.regenerate_env_repaths)
        self.custom_path_btn.clicked.connect(self.choose_custom_path)
        self.migrate_btn.clicked.connect(self.migrate_it)

    def setup_default_path(self):
        _layout = QHBoxLayout()
        self.mainlayout.addLayout(_layout)
        self.default_path_btn = QPushButton('初始路径')
        self.default_path_ledt = QLineEdit()
        self.default_path_ledt.setPlaceholderText('这里输入游戏(软件)的存档(配置文件)的默认路径')
        _layout.addWidget(self.default_path_btn)
        _layout.addWidget(self.default_path_ledt)

    def choose_default_path(self):
        path_text = QFileDialog.getExistingDirectory()
        if path_text:
            # 转换为操作系统支持的路径格式
            format_path_text = Path(path_text)
            self.default_path_ledt.setText(str(format_path_text))

    def setup_choose_path_mode(self):
        self.abs_path_mode_btn = QRadioButton('绝对路径')
        self.env_repath_mode_btn = QRadioButton('环境路径')
        self.path_mode_group = QButtonGroup()
        self.path_mode_group.addButton(self.abs_path_mode_btn)
        self.path_mode_group.addButton(self.env_repath_mode_btn)
        self.mainlayout.addWidget(self.abs_path_mode_btn)
        self.mainlayout.addWidget(self.env_repath_mode_btn)

    def setup_env_repath(self):
        self.env_repath_frame = QFrame()
        self.mainlayout.addWidget(self.env_repath_frame)
        self.env_repath_form_layout = QFormLayout(self.env_repath_frame)

    def regenerate_env_repaths(self):
        _defalult_path = Path(self.default_path_ledt.text().strip())
        if _defalult_path.exists():
            env_paths = EnvPaths(_defalult_path)
            self.env_repath_layout_clear()
            if env_paths.env_repaths:
                # 默认为相对路径模式
                self.env_repath_mode_btn.setDisabled(False)
                self.env_repath_mode_btn.setChecked(True)
                self._env_repath_btn_group = QButtonGroup()
                _first_row = True
                for _ENV, _repath in env_paths.env_repaths.items():
                    _btn = QRadioButton(f'%{_ENV}%')
                    self._env_repath_btn_group.addButton(_btn)
                    _lbl = QLabel(f'{env_to_path(_ENV)} >>> {_repath}')
                    self.env_repath_form_layout.addRow(_btn, _lbl)
                    # 按下切换为环境路径模式
                    _btn.toggled.connect(self.env_repath_mode_btn.setChecked)
                    if _first_row:
                        _btn.setChecked(True)
                        _first_row = False
            else:
                self.abs_path_mode_btn.setChecked(True)
                self.env_repath_mode_btn.setDisabled(True)

    def env_repath_layout_clear(self):
        for _row in range(self.env_repath_form_layout.rowCount()-1, -1, -1):
            self.env_repath_form_layout.removeRow(_row)

    def setup_create_custom_area(self):
        _layout = QHBoxLayout()
        self.mainlayout.addLayout(_layout)
        self.custom_path_btn = QPushButton('目标路径')
        self.custom_path_ledt = QLineEdit()
        self.custom_path_ledt.setPlaceholderText('这里输入要迁移到的路径')
        self.migrate_btn = QPushButton('迁移！')
        _layout.addWidget(self.custom_path_btn)
        _layout.addWidget(self.custom_path_ledt)
        _layout.addWidget(self.migrate_btn)

    def choose_custom_path(self):
        path_text = QFileDialog.getExistingDirectory()
        if path_text:
            # 转换为操作系统支持的路径格式
            format_path_text = Path(path_text)
            self.custom_path_ledt.setText(str(format_path_text))

    def migrate_it(self):
        if self.path_pass():
            if self.abs_path_mode_btn:
                print(self._default_path, self._custom_path)
            elif self.env_repath_mode_btn.isChecked():
                for _btn in self.env_repath_frame.findChildren(QRadioButton):
                    if _btn.isChecked():
                        _ENV = _btn.text()[1:-1]
                        _repath = str(self._default_path.relative_to(env_to_path(_ENV)))
                        print(_ENV, _repath)

    def path_pass(self):
        self._default_path = Path(self.default_path_ledt.text().strip())
        self._custom_path = Path(self.custom_path_ledt.text().strip())
        if self._custom_path == Path('./'):
            print('error')
        return True
