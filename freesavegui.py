# -*- coding: utf-8 -*-

from utils import *
from qtcore import *
from syspaths import SysPaths


class FreeSaveGUI(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()
        # 默认为相对路径模式
        self.env_repath_mode_btn.setChecked(True)

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

        self.setup_custom_path()

    def setup_connections(self):
        self.default_path_btn.clicked.connect(self.choose_default_path)
        self.default_path_ledt.textChanged.connect(self.generate_env_repaths)

    def setup_default_path(self):
        _layout = QHBoxLayout()
        self.mainlayout.addLayout(_layout)
        self.default_path_btn = QPushButton('初始路径')
        self.default_path_ledt = QLineEdit()
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
        self.env_repath_mode_btn = QRadioButton('相对路径')
        self.path_mode_group = QButtonGroup()
        self.path_mode_group.addButton(self.abs_path_mode_btn)
        self.path_mode_group.addButton(self.env_repath_mode_btn)
        self.mainlayout.addWidget(self.abs_path_mode_btn)
        self.mainlayout.addWidget(self.env_repath_mode_btn)

    def setup_env_repath(self):
        # self.env_repath_list_widget = QListWidget()
        # self.mainlayout.addWidget(self.env_repath_list_widget)
        self.env_repath_form_layout = QFormLayout()

    def show_env_repaths(self):
        pass


    def generate_env_repaths(self):
        _defalult_path = Path(self.default_path_ledt.text().strip())
        sys_paths = SysPaths(_defalult_path)
        for _ENV, repath in sys_paths.env_repaths.items():
            print(f'(%{_ENV}%){env_to_path(_ENV)} >>> {repath}')

    def setup_custom_path(self):
        pass
