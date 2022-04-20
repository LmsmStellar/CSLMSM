from abc import ABC, abstractmethod

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QHeaderView, QAbstractItemView
import cleansky_LMSM.ui_to_py_by_qtdesigner.Login
import cleansky_LMSM.ui_to_py_by_qtdesigner.Management
import cleansky_LMSM.ui_to_py_by_qtdesigner.Menu
import cleansky_LMSM.ui_to_py_by_qtdesigner.Items_to_be_tested


# class TableModel(QtCore.QAbstractTableModel):
#     """
#     https://www.pythonguis.com/tutorials/modelview-architecture/
#     """
#     def __init__(self, data):
#         super(TableModel, self).__init__()
#         self._data = data
#
#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             # See below for the nested-list data structure.
#             # .row() indexes into the outer list,
#             # .column() indexes into the sub-list
#             return self._data[index.row()][index.column()]
#
#     def rowCount(self, index):
#         # The length of the outer list.
#         return len(self._data)
#
#     def columnCount(self, index):
#         # The following takes the first sub-list, and returns
#         # the length (only works if all rows are an equal length)
#         return len(self._data[0])

class MyMainWindow(QMainWindow):
    def __init__(self, my_view):
        super().__init__()
        self.view = my_view

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.view.get_controller().action_close_window()


class View(ABC):
    def __init__(self, controller_obj=None):
        super().__init__()
        self.ui = self.get_ui()
        # View classes must have droit to access his controller by architecture MVC, otherwise we create a view object
        # without controller object just for doing an unittest
        self.__controller = controller_obj
        self.main_window = None

    def set_controller(self, controller_obj):
        """View classes must have droit to access his controller by architecture MVC"""
        self.__controller = controller_obj

    def get_controller(self):
        return self.__controller

    def run_view(self):
        """
        template method for setup and display a GUI
        模板方法
        """
        self.main_window = MyMainWindow(self)
        self.ui.setupUi(self.main_window)
        self.setup_ui()
        self.main_window.show()

    @abstractmethod
    def get_ui(self):
        """从指定目录下调取ui对象的方法"""
        pass

    @abstractmethod
    def setup_ui(self):
        pass

    def main_window_close(self):
        self.main_window.close()

    def permission_denied(self):
        # QMessageBox.warning(self.ui.pushButton, 'Warning', 'permission denied', QMessageBox.Yes)
        pass

    @staticmethod
    def tools_setup_combobox(combobox_obj, items_init=None, func=None):
        """初始化combobox"""
        combobox_obj.clear()
        combobox_obj.setEditable(True)
        if items_init is not None:
            combobox_obj.addItems(items_init)
        combobox_obj.setCurrentIndex(-1)
        if func is not None:
            combobox_obj.currentTextChanged.connect(func)

    @staticmethod
    def tools_setup_table(table_widget_obj, mat=None, title=None, clicked_fun=None, double_clicked_fun=None,
                          strategy=None):
        """初始化表格"""
        table_widget_obj.horizontalHeader().setStretchLastSection(True)
        table_widget_obj.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget_obj.setSelectionBehavior(1)
        if mat is not None:
            if title is not None:
                table_widget_obj.setColumnCount(len(mat[0]))
            table_widget_obj.setRowCount(len(mat))
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    # QTableWidgetItem必须传入string类型的数据，当传入浮点型数据的时候无法显示
                    if mat[i][j] is None:
                        table_widget_obj.setItem(i, j, QTableWidgetItem(mat[i][j]))
                    elif mat[i][j] is not str:
                        table_widget_obj.setItem(i, j, QTableWidgetItem(str(mat[i][j])))
                    else:
                        table_widget_obj.setItem(i, j, QTableWidgetItem(mat[i][j]))
        else:
            table_widget_obj.clear()
            table_widget_obj.setRowCount(0)
        if clicked_fun is not None:
            table_widget_obj.cellClicked[int, int].connect(clicked_fun)
        if double_clicked_fun is not None:
            table_widget_obj.cellDoubleClicked[int, int].connect(double_clicked_fun)
        if title is not None:
            # 这俩函数必须同时使用否则无法完成初始化
            table_widget_obj.setColumnCount(len(title))
            table_widget_obj.setHorizontalHeaderLabels(title)

    @staticmethod
    def tools_set_table_color(table_object, i_index=None, j_index=None, color=QtGui.QColor(100, 100, 150)):
        try:
            if i_index is None and j_index is None:
                row_num = table_object.rowCount()
                col_num = table_object.columnCount()
                for i in range(row_num):
                    for j in range(col_num):
                        table_object.item(i, j).setBackground(color)
        except TypeError:
            pass

    @staticmethod
    def tools_add_row_to_table(table_object, lis):
        """向表格中追加一行"""
        row_position = table_object.rowCount()
        table_object.insertRow(row_position)
        for x in range(len(lis)):
            table_object.setItem(row_position, x, QTableWidgetItem(lis[x]))

    @staticmethod
    def tools_setup_list(list_object, lis=None, current_row_changed_fun=None):
        list_object.clear()
        if lis is not None:
            list_object.addItems(lis)
        if current_row_changed_fun is not None:
            list_object.currentRowChanged.connect(current_row_changed_fun)

    @abstractmethod
    def refresh(self):
        """用于页面初始化"""
        pass

    @staticmethod
    def tools_op_object(opacity, obj):
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(opacity)
        obj.setGraphicsEffect(op)

    def button_clicked_db_transfer(self):
        """调用controller中的commit接口"""
        self.get_controller().action_submit()

    def button_clicked_cancel(self):
        """调用controller中的rollback接口"""
        self.get_controller().action_roll_back()

    @abstractmethod
    def handle_tab_bar_clicked(self, index):
        """该函数用于管理tab标签页切换"""
        pass


class LoginView(View):
    def handle_tab_bar_clicked(self, index):
        pass

    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Login.Ui_MainWindow()

    def setup_ui(self):
        self.ui.pushButton.clicked.connect(self.button_login_clicked)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)

    def button_login_clicked(self):
        self.get_controller().action_login()

    def get_username(self):
        return self.ui.lineEdit_2.text()

    def get_password(self):
        return self.ui.lineEdit.text()

    def login_fail(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        if QMessageBox.warning(self.ui.pushButton,
                               'login fail', 'wanna retry?',
                               QMessageBox.Yes | QMessageBox.No) == 65536:
            self.main_window.close()


class MenuView(View):
    def handle_tab_bar_clicked(self, index):
        pass

    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Menu.Ui_MainWindow()

    def setup_ui(self):
        self.ui.pushButton.clicked.connect(self.open_management)
        self.ui.pushButton_3.clicked.connect(self.open_items_to_be_tested)

    def open_management(self):
        self.get_controller().action_open_management()

    def open_items_to_be_tested(self):
        self.get_controller().action_open_items_to_be_tested()


class ManagementView(View):
    # 这个变量是用来保存当前选中的用户的名称的
    # 修改权限的条件是：知道元素的类型，元素的id，用户的id，权限的大小
    # 在修改mean的时候，必须确保元素id查找成功
    def __init__(self):
        super().__init__()
        # 存储当前编辑的多选框对象，用于配合setup_combobox_allocation函数使用
        self.combobox_object_set = None
        # 被点击选择的角色的姓名
        self.choose_person_name = None
        # 当前元素的类型
        self.choose_element_type = None
        # 当前点击的是左侧表格的成员，则state为0，右侧表格的成员，则state为1
        self.state = None

    def setup_combobox_allocation(self, *args):
        """
        很有意思的BUG
        当我在调用这个函数初始化其他combobox的时候，其他combobox的edited函数也会被调用，从而清除当前combobox中的内容
        传入不需要被初始化的多选框对象，作差集以初始化其他多选框

        解决方法，使用setCurrentText，将txt参数重新填到combobox中
        """
        others = self.combobox_object_set - set(args)
        print(args)
        for item in others:
            print(item)
            item.setCurrentIndex(-1)

    def refresh(self):
        pass

    def handle_tab_bar_clicked(self, index):
        if index == 0:
            self.setup_tab_user_management()
        elif index == 1:
            self.setup_tab_user_allocation()

    def setup_tab_user_allocation(self):
        self.tools_setup_combobox(self.ui.comboBox_6,
                                  items_init=self.get_controller().action_fill_simple_element('type_coating'))
        self.tools_setup_combobox(self.ui.comboBox_7,
                                  items_init=self.get_controller().action_fill_simple_element('type_detergent'))
        self.tools_setup_combobox(self.ui.comboBox_8,
                                  items_init=['Yes', 'No'])
        self.tools_setup_combobox(self.ui.comboBox_9,
                                  items_init=self.get_controller().action_fill_means())
        self.tools_setup_combobox(self.ui.comboBox_10)
        self.tools_setup_combobox(self.ui.comboBox_11)
        self.tools_setup_combobox(self.ui.comboBox_12,
                                  items_init=self.get_controller().action_fill_simple_element('type_tank'))
        self.tools_setup_combobox(self.ui.comboBox_13,
                                  items_init=self.get_controller().action_fill_simple_element('type_sensor'))
        self.tools_setup_combobox(self.ui.comboBox_14,
                                  items_init=self.get_controller().action_fill_simple_element('type_ejector'))
        self.tools_setup_combobox(self.ui.comboBox_15,
                                  items_init=self.get_controller().action_fill_simple_element('type_camera'))
        self.tools_setup_combobox(self.ui.comboBox_16,
                                  items_init=['Yes', 'No'])
        self.tools_setup_combobox(self.ui.comboBox_17,
                                  items_init=self.get_controller().action_fill_simple_element('test_team'))
        self.tools_setup_combobox(self.ui.comboBox_18,
                                  items_init=self.get_controller().action_fill_simple_element('type_test_point'))
        self.tools_setup_combobox(self.ui.comboBox_19,
                                  items_init=self.get_controller().action_fill_simple_element('type_intrinsic_value'))

        # 初始化表格列名
        self.tools_setup_table(self.ui.tableWidget_2, title=['username', 'role'])

    def setup_tab_user_management(self):
        self.tools_setup_combobox(self.ui.comboBox, items_init=self.get_controller().action_fill_organisation())
        self.tools_setup_combobox(self.ui.comboBox_2)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.tools_setup_combobox(self.ui.comboBox_3)
        self.tools_setup_combobox(self.ui.comboBox_4)
        self.ui.lineEdit_3.clear()

        # 填充用户表格
        data = self.get_controller().action_fill_user_table()
        self.tools_setup_table(self.ui.tableWidget, mat=data, title=['orga', 'uname', 'email', 'fname', 'lname', 'tel'],
                               clicked_fun=self.clicked_user_table)
        """
        https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
        If you want a table that uses your own data model you should use QTableView rather than this class.
        """

        # 填充管理员表格
        data = self.get_controller().action_fill_administrator_table()
        View.tools_setup_table(self.ui.tableWidget_4, mat=data, title=['element_type', 'element_info', 'admi_name'])

        # user crud
        self.tools_setup_table(self.ui.tableWidget_6, title=['username', 'state'])

        # user right
        self.tools_setup_table(self.ui.tableWidget_3, title=['element_type', 'element_info', 'role'])

    def clicked_user_table(self, i, j):
        organisation = self.ui.tableWidget.item(i, 0).text()
        user_name = self.ui.tableWidget.item(i, 1).text()
        email = self.ui.tableWidget.item(i, 2).text()
        first_name = self.ui.tableWidget.item(i, 3).text()
        last_name = self.ui.tableWidget.item(i, 4).text()
        tele = self.ui.tableWidget.item(i, 5).text()
        self.ui.comboBox.setCurrentText(organisation)
        self.ui.comboBox_2.setCurrentText(user_name)
        self.ui.comboBox_3.setCurrentText(first_name)
        self.ui.comboBox_4.setCurrentText(last_name)
        self.ui.lineEdit.setText(email)
        self.ui.lineEdit_3.setText(tele)

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Management.Ui_MainWindow()

    def button_db_transfer_tab1(self):
        self.button_clicked_db_transfer()
        self.setup_tab_user_management()

    def button_cancel_tab1(self):
        self.button_clicked_cancel()
        self.setup_tab_user_management()

    def button_db_transfer_tab2(self):
        self.button_clicked_db_transfer()
        self.setup_tab_user_allocation()

    def button_cancel_tab2(self):
        self.button_clicked_cancel()
        self.setup_tab_user_allocation()

    def setup_ui(self):
        self.combobox_object_set = {self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9,
                                    self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_12, self.ui.comboBox_13,
                                    self.ui.comboBox_14, self.ui.comboBox_15, self.ui.comboBox_16, self.ui.comboBox_17,
                                    self.ui.comboBox_18, self.ui.comboBox_19}
        # 初始化tab
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)

        # 初始化user management
        self.ui.comboBox.currentTextChanged.connect(self.edited_organisation)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_username)
        self.ui.pushButton.clicked.connect(self.button_clicked_password)
        self.ui.pushButton_2.clicked.connect(self.button_clicked_validate)
        self.ui.pushButton_3.clicked.connect(self.button_clicked_remove)
        self.ui.pushButton_5.clicked.connect(self.button_db_transfer_tab1)
        self.ui.pushButton_4.clicked.connect(self.button_cancel_tab1)

        self.setup_tab_user_management()

        # 初始化user allocation
        self.ui.comboBox_6.currentTextChanged.connect(self.edited_coating)
        self.ui.comboBox_7.currentTextChanged.connect(self.edited_detergent)
        self.ui.comboBox_8.currentTextChanged.connect(self.edited_insect)
        self.ui.comboBox_9.currentTextChanged.connect(self.edited_means_type)
        self.ui.comboBox_10.currentTextChanged.connect(self.edited_means_name)
        self.ui.comboBox_11.currentTextChanged.connect(self.edited_serial_number)
        self.ui.comboBox_12.currentTextChanged.connect(self.edited_tank)
        self.ui.comboBox_13.currentTextChanged.connect(self.edited_sensor)
        self.ui.comboBox_14.currentTextChanged.connect(self.edited_ejector)
        self.ui.comboBox_15.currentTextChanged.connect(self.edited_camera)
        self.ui.comboBox_16.currentTextChanged.connect(self.edited_acqui)
        self.ui.comboBox_17.currentTextChanged.connect(self.edited_teams)
        self.ui.comboBox_18.currentTextChanged.connect(self.edited_points)
        self.ui.comboBox_19.currentTextChanged.connect(self.edited_intrinsic)

        View.tools_setup_combobox(self.ui.comboBox_5,
                                  self.get_controller().action_fill_rights(),
                                  self.edited_rights)
        self.ui.comboBox_5.setEditable(False)

        # validate 按钮初始化
        self.ui.pushButton_8.clicked.connect(self.button_rights_validate_clicked)
        # db_transfer和cancel初始化
        self.ui.pushButton_6.clicked.connect(self.button_db_transfer_tab2)
        self.ui.pushButton_7.clicked.connect(self.button_cancel_tab2)
        # 权限表格初始化
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2,
                               clicked_fun=self.user_right_row_left_clicked)
        # others表格初始化
        self.tools_setup_list(list_object=self.ui.listWidget,
                              current_row_changed_fun=self.user_right_row_right_clicked)

    """
    https://www.geeksforgeeks.org/pyqt5-how-to-add-multiple-items-to-the-combobox/
    """
    """
    https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/
    If you want a table that uses your own data model you should use QTableView rather than this class.
    """

    def add_table_user_modify(self, lis):
        """向增删改查用户的表格中添加一行记录"""
        self.tools_add_row_to_table(self.ui.tableWidget_6, lis)

    def edited_organisation(self, txt):
        user_list = self.get_controller().action_fill_user_list(txt)
        self.ui.comboBox_2.currentTextChanged.disconnect(self.edited_username)
        self.ui.comboBox_2.clear()
        View.tools_setup_combobox(self.ui.comboBox_2, items_init=user_list)
        self.ui.comboBox_2.currentTextChanged.connect(self.edited_username)

    def edited_username(self, txt):
        if txt != '':
            mat = self.get_controller().action_fill_user_right_table(txt)
            self.update_user_rights_table(mat)

            # 填充firstname和lastname
            first_name, last_name = self.get_controller().action_fill_fname_lname(txt)
            self.ui.comboBox_3.clear()
            View.tools_setup_combobox(self.ui.comboBox_3, items_init=first_name)
            self.ui.comboBox_4.clear()
            View.tools_setup_combobox(self.ui.comboBox_4, items_init=last_name)

            # 填充个人信息
            lis = self.get_controller().action_fill_user_info(txt)
            if lis is not None:
                self.ui.comboBox.setCurrentText(lis[0])
                self.ui.comboBox_2.setCurrentText(lis[1])
                self.ui.comboBox_3.setCurrentText(lis[3])
                self.ui.comboBox_4.setCurrentText(lis[4])
                self.ui.lineEdit.setText(lis[2])
                self.ui.lineEdit_3.setText(lis[5])

    def edited_coating(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_6)
        self.ui.comboBox_6.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(1, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 1

    def edited_detergent(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_7)
        self.ui.comboBox_7.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(2, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 2

    def edited_insect(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_8)
        self.ui.comboBox_8.setCurrentText(txt)

        if txt != '':
            if txt == 'Yes':
                txt = True
            if txt == 'No':
                txt = False
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(10, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 10

    def edited_means_type(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11)
        self.ui.comboBox_9.setCurrentText(txt)

        means_type = self.get_controller().action_fill_combobox_test_mean(txt)
        self.ui.comboBox_10.currentTextChanged.disconnect(self.edited_means_name)
        self.ui.comboBox_10.clear()
        View.tools_setup_combobox(self.ui.comboBox_10, items_init=means_type)
        self.ui.comboBox_10.currentTextChanged.connect(self.edited_means_name)
        self.choose_element_type = 0

        self.ui.comboBox_11.clear()

        self.tools_setup_table(self.ui.tableWidget_2, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget)

    def edited_means_name(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11)

        mean_type = self.ui.comboBox_9.currentText()
        # if mean_type == '':
        #     self.setup_tab_user_allocation()
        #     self.ui.comboBox_10.setCurrentText(txt)

        means_serial = self.get_controller().action_fill_serial(mean_type, txt)
        self.ui.comboBox_11.currentTextChanged.disconnect(self.edited_serial_number)
        self.ui.comboBox_11.clear()
        View.tools_setup_combobox(self.ui.comboBox_11, items_init=means_serial, func=self.edited_serial_number)
        self.choose_element_type = 0

        self.tools_setup_table(self.ui.tableWidget_2, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget)

    def edited_serial_number(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11)

        test_mean_type = self.ui.comboBox_9.currentText()
        test_mean_name = self.ui.comboBox_10.currentText()

        if test_mean_name == '' or test_mean_type == '':
            # 输入不合法就会重置页面，但是依然会将当前输入的内容保留
            self.setup_tab_user_allocation()
            self.ui.comboBox_9.setCurrentText(test_mean_type)
            self.ui.comboBox_10.setCurrentText(test_mean_name)

        if test_mean_type != '' and test_mean_name != '':
            print(test_mean_type + ' ' + test_mean_name + ' ' + txt)
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(0, (test_mean_type, test_mean_name, txt))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 0

    def edited_tank(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_12)
        self.ui.comboBox_12.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(3, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 3

    def edited_sensor(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_13)
        self.ui.comboBox_13.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(4, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 4

    def edited_acqui(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_16)
        self.ui.comboBox_16.setCurrentText(txt)

        if txt != '':
            if txt == 'Yes':
                txt = True
            if txt == 'No':
                txt = False
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(11, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 11

    def edited_ejector(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_14)
        self.ui.comboBox_14.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(5, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 5

    def edited_camera(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_15)
        self.ui.comboBox_15.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(6, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 6

    def edited_teams(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_17)
        self.ui.comboBox_17.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(9, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 9

    def edited_points(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_18)
        self.ui.comboBox_18.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(7, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 7

    def edited_intrinsic(self, txt):
        self.setup_combobox_allocation(self.ui.comboBox_19)
        self.ui.comboBox_19.setCurrentText(txt)

        if txt != '':
            owner_mat, other_list = self.get_controller().action_fill_user_right_list(8, (txt,))
            self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
            self.tools_setup_list(self.ui.listWidget, other_list)
            self.choose_element_type = 8

    def edited_rights(self, txt):
        pass

    def button_clicked_validate(self):
        # 生成能满足要求的数据格式
        lis = []
        username = self.ui.comboBox_2.currentText()
        if username != '':
            orga = self.ui.comboBox.currentText()
            mail = self.ui.lineEdit.text()
            fname = self.ui.comboBox_3.currentText()
            lname = self.ui.comboBox_4.currentText()
            tel = self.ui.lineEdit_3.text()
            new_pd = self.ui.lineEdit_2.text()
            lis = [username, orga, fname, lname, tel, mail, new_pd]
            self.get_controller().action_validate_user(lis)
            self.setup_tab_user_management()

    def button_clicked_remove(self):
        username = self.ui.comboBox_2.currentText()
        self.get_controller().action_delete_user(username)
        self.setup_tab_user_management()

    def button_clicked_password(self):
        pass

    def update_user_rights_table(self, mat):
        View.tools_setup_table(self.ui.tableWidget_3, mat)

    def user_right_row_left_clicked(self, i, j):
        # if self.ui.tableWidget_2.item(i, 0) is not None:
        self.choose_person_name = self.ui.tableWidget_2.item(i, 0).text()
        self.state = 0

    def user_right_row_right_clicked(self, i):
        if self.ui.listWidget.currentItem() is not None:
            self.choose_person_name = self.ui.listWidget.currentItem().text()
            self.state = 1
        else:
            self.choose_person_name = None
            self.state = None

    def button_rights_validate_clicked(self):
        """权限分配validate按钮"""
        if self.choose_element_type is None or self.choose_person_name is None:
            # 不知道元素类型，直接返回
            return

        element_info = {
            # means_type
            0: (self.ui.comboBox_9.currentText(), self.ui.comboBox_10.currentText(), self.ui.comboBox_11.currentText()),
            1: (self.ui.comboBox_6.currentText(),),
            2: (self.ui.comboBox_7.currentText(),),
            3: (self.ui.comboBox_6.currentText(),),
            4: (self.ui.comboBox_13.currentText(),),
            5: (self.ui.comboBox_14.currentText(),),
            6: (self.ui.comboBox_15.currentText(),),
            7: (self.ui.comboBox_18.currentText(),),
            8: (self.ui.comboBox_19.currentText(),),
            9: (self.ui.comboBox_17.currentText(),),
            10: (self.ui.comboBox_8.currentText(),),
            11: (self.ui.comboBox_16.currentText(),)
        }[self.choose_element_type]

        # 获取权限
        role_str = self.ui.comboBox_5.currentText()
        if role_str == '':
            return

        self.get_controller().action_change_role(self.choose_element_type, ref_tup=element_info,
                                                 person_name=self.choose_person_name,
                                                 role_str=role_str, state=self.state)

        owner_mat, other_list = self.get_controller().action_fill_user_right_list(self.choose_element_type,
                                                                                  element_info)
        self.tools_setup_table(self.ui.tableWidget_2, mat=owner_mat, title=['username', 'role'])
        self.tools_setup_list(self.ui.listWidget, other_list)


class ItemsToBeTestedView(View):
    coating_validate_token = None
    detergent_validate_token = None

    def __init__(self, controller_obj=None):
        super().__init__(controller_obj)

        # 初始化用来验证validate的窗口
        self.message = QMessageBox()
        self.message.setText("Validate or not?")
        self.message.setWindowTitle("Warning!")
        self.message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # self.message.buttonClicked.connect(self.ans)

    def refresh(self):
        pass

    def get_ui(self):
        return cleansky_LMSM.ui_to_py_by_qtdesigner.Items_to_be_tested.Ui_MainWindow()

    def setup_ui(self):
        """
        因为使用了策略模式，所以在初始化的时候就把coating和detergent的信号和槽函数配置好，
        这样在切换页面的时候不用重复设置信号与槽函数
        """
        self.setup_tab_widget()
        # element_type_name和number初始化
        self.tools_setup_combobox(self.ui.comboBox_11, func=self.edited_combobox_element_type)
        self.ui.comboBox_11.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_5, func=self.edited_combobox_element_type)
        self.ui.comboBox_5.setEditable(False)
        self.tools_setup_combobox(self.ui.comboBox_12, func=self.edited_combobox_number)
        self.tools_setup_combobox(self.ui.comboBox_6, func=self.edited_combobox_number)

        # create
        self.ui.pushButton_15.clicked.connect(self.button_clicked_create_element)
        self.ui.pushButton_8.clicked.connect(self.button_clicked_create_element)

        # search
        self.ui.pushButton_14.clicked.connect(self.button_clicked_search)
        self.ui.pushButton_7.clicked.connect(self.button_clicked_search)

        # table
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_4, title=['attribute', 'value', 'unity'],
                               clicked_fun=self.clicked_row, double_clicked_fun=self.double_clicked_row)
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, title=['attribute', 'value', 'unity'],
                               clicked_fun=self.clicked_row, double_clicked_fun=self.double_clicked_row)

        # db_transfer
        self.ui.pushButton_12.clicked.connect(self.button_clicked_db_transfer)
        self.ui.pushButton_5.clicked.connect(self.button_clicked_db_transfer)

        # insect 界面信号槽初始化
        self.ui.pushButton_11.clicked.connect(self.click_add_insect)
        self.ui.pushButton_9.clicked.connect(self.click_insect_cancel)
        self.ui.pushButton_10.clicked.connect(self.click_insect_db_transfer)

        self.setup_tab_coating_and_detergent()
        self.get_controller().disable_modify()

        self.setup_tab_insects()

    def setup_tab_coating_and_detergent(self):
        """
        关键函数，在切换页面的时候用于初始化页面的信息
        """
        if self.get_controller().is_coating:
            self.tools_setup_combobox(self.ui.comboBox_12)
            self.tools_setup_combobox(self.ui.comboBox_14)
            self.tools_setup_combobox(self.ui.comboBox_13)
            self.ui.lineEdit_8.clear()
            self.tools_setup_table(self.ui.tableWidget_4, title=['attribute', 'value', 'unity'])
        elif self.get_controller().is_coating is False:
            self.tools_setup_combobox(self.ui.comboBox_6)
            self.tools_setup_combobox(self.ui.comboBox_8)
            self.tools_setup_combobox(self.ui.comboBox_7)
            self.ui.lineEdit_9.clear()
            self.tools_setup_table(self.ui.tableWidget_2, title=['attribute', 'value', 'unity'])
        self.setup_combobox_element_type()
        self.disable_modify()
        print("setup_tab_called")
        self.get_controller().print_state()

    def setup_tab_widget(self):
        self.ui.tabWidget.tabBarClicked.connect(self.handle_tab_bar_clicked)

    def handle_tab_bar_clicked(self, index):
        if index == 1:
            # change to tab detergent
            self.get_controller().is_coating = False
            self.setup_tab_coating_and_detergent()
        elif index == 2:
            # change to tab insect
            self.get_controller().insect_state.refresh()
            self.get_controller().is_coating = None
            self.setup_tab_insects()
        elif index == 0:
            # change to tab coating
            self.get_controller().is_coating = True
            self.setup_tab_coating_and_detergent()

    def setup_tab_insects(self):
        """负责insect的页面初始化"""
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()

        name, hemolymphe = self.get_controller().action_get_names_hemolymphe()
        self.tools_setup_combobox(self.ui.comboBox_9, items_init=name, func=self.edited_insect_name)
        self.tools_setup_combobox(self.ui.comboBox_10, items_init=hemolymphe, func=self.edited_insect_hemo)

        mat = self.get_controller().action_get_insect_table()
        self.tools_setup_table(table_widget_obj=self.ui.tableWidget_3,
                               title=['names', 'mass', 'altitude min', 'altitude max', 'length', 'width', 'thickness',
                                      'hemo', 'state'],
                               clicked_fun=self.click_one_insect,
                               double_clicked_fun=self.double_click_insect,
                               mat=mat)

    def click_insect_cancel(self):
        self.get_controller().insect_state.refresh()
        self.button_clicked_cancel()
        self.setup_tab_insects()

    def click_insect_db_transfer(self):
        self.get_controller().insect_state.refresh()
        self.button_clicked_db_transfer()
        self.setup_tab_insects()

    def click_add_insect(self):
        """和manager里创建新用户一致"""
        name = self.ui.comboBox_9.currentText()
        if name == '':
            return
        mass = self.ui.lineEdit.text()
        at_min = self.ui.lineEdit_2.text()
        at_max = self.ui.lineEdit_3.text()
        length = self.ui.lineEdit_5.text()
        width = self.ui.lineEdit_6.text()
        thick = self.ui.lineEdit_7.text()
        hemo = self.ui.comboBox_10.currentText()
        self.get_controller().action_add_insect(name=name, masse=mass, alt_min=at_min, alt_max=at_max, length=length,
                                                width=width, thickness=thick, hemolymphe=hemo,
                                                str_type=['name', 'hemolymphe'])
        self.setup_tab_insects()

    def click_one_insect(self, i):
        name = self.ui.tableWidget_3.item(i, 0).text()
        mass = self.ui.tableWidget_3.item(i, 1).text()
        at_min = self.ui.tableWidget_3.item(i, 2).text()
        at_max = self.ui.tableWidget_3.item(i, 3).text()
        length = self.ui.tableWidget_3.item(i, 4).text()
        width = self.ui.tableWidget_3.item(i, 5).text()
        thick = self.ui.tableWidget_3.item(i, 6).text()
        hemo = self.ui.tableWidget_3.item(i, 7).text()
        self.ui.comboBox_9.setCurrentText(name)
        self.ui.comboBox_10.setCurrentText(hemo)
        self.ui.lineEdit.setText(mass)
        self.ui.lineEdit_2.setText(at_min)
        self.ui.lineEdit_3.setText(at_max)
        self.ui.lineEdit_5.setText(length)
        self.ui.lineEdit_6.setText(width)
        self.ui.lineEdit_7.setText(thick)

    def double_click_insect(self, i, j):
        pass

    def edited_insect_name(self, txt):
        pass

    def edited_insect_hemo(self, txt):
        pass

    def refresh_table(self, mat, strategy=True):
        if strategy:
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_4, mat=mat)
        elif strategy is False:
            self.tools_setup_table(table_widget_obj=self.ui.tableWidget_2, mat=mat)

    def clicked_row(self, i, j):
        """
        点击表格的某一行，将数据填入attribute，value和unity
        """
        if self.get_controller().is_coating:
            attribute_name = self.ui.tableWidget_4.item(i, 0).text()
            value = self.ui.tableWidget_4.item(i, 1).text()
            unity = self.ui.tableWidget_4.item(i, 2).text()
            self.ui.comboBox_14.setCurrentText(attribute_name)
            self.ui.comboBox_13.setCurrentText(unity)
            self.ui.lineEdit_8.setText(value)
        elif self.get_controller().is_coating is False:
            attribute_name = self.ui.tableWidget_2.item(i, 0).text()
            value = self.ui.tableWidget_2.item(i, 1).text()
            unity = self.ui.tableWidget_2.item(i, 2).text()
            self.ui.comboBox_8.setCurrentText(attribute_name)
            self.ui.comboBox_7.setCurrentText(unity)
            self.ui.lineEdit_9.setText(value)

    def double_clicked_row(self, i, j):
        """
        双击表格的某一行，将attribute删除
        """
        element_type_name, number, attribute_name, value, unity = '', '', '', '', ''
        if self.get_controller().is_coating:
            element_type_name = self.ui.comboBox_11.currentText()
            number = self.ui.comboBox_12.currentText()
            attribute_name = self.ui.tableWidget_4.item(i, 0).text()
            value = self.ui.tableWidget_4.item(i, 1).text()
            unity = self.ui.tableWidget_4.item(i, 2).text()
        elif self.get_controller().is_coating is False:
            element_type_name = self.ui.comboBox_5.currentText()
            number = self.ui.comboBox_6.currentText()
            attribute_name = self.ui.tableWidget_2.item(i, 0).text()
            value = self.ui.tableWidget_2.item(i, 1).text()
            unity = self.ui.tableWidget_2.item(i, 2).text()

        self.get_controller().action_delete_element_attribute(element_type_name, number,
                                                              attribute_name, value, unity)

    def setup_combobox_element_type(self):
        data = self.get_controller().action_get_element_type()
        if self.get_controller().is_coating:
            self.tools_setup_combobox(self.ui.comboBox_11, items_init=data)
            self.ui.comboBox_11.setEditable(False)
        elif self.get_controller().is_coating is False:
            self.tools_setup_combobox(self.ui.comboBox_5, items_init=data)
            self.ui.comboBox_5.setEditable(False)

    def fill_combobox_position(self, items=None):
        if self.get_controller().is_coating:
            self.tools_setup_combobox(self.ui.comboBox_12, items_init=items)
        elif self.get_controller().is_coating is False:
            self.tools_setup_combobox(self.ui.comboBox_6, items_init=items)

    def setup_combobox_unity(self, items=None, strategy=True):
        if strategy:
            self.tools_setup_combobox(self.ui.comboBox_13, items_init=items)
        elif strategy is False:
            self.tools_setup_combobox(self.ui.comboBox_7, items_init=items)

    def edited_combobox_element_type(self, txt):
        if txt != '':
            data = self.get_controller().action_get_element_position(element_type=txt)
            if self.get_controller().is_coating:
                self.ui.comboBox_12.currentTextChanged.disconnect(self.edited_combobox_number)
                self.ui.comboBox_12.clear()
                View.tools_setup_combobox(self.ui.comboBox_12, items_init=data)
                self.ui.comboBox_12.currentTextChanged.connect(self.edited_combobox_number)
            elif self.get_controller().is_coating is False:
                self.ui.comboBox_6.currentTextChanged.disconnect(self.edited_combobox_number)
                self.ui.comboBox_6.clear()
                View.tools_setup_combobox(self.ui.comboBox_6, items_init=data)
                self.ui.comboBox_6.currentTextChanged.connect(self.edited_combobox_number)

    def edited_combobox_number(self, txt):
        if txt != '':
            element_type = ''
            if self.get_controller().is_coating:
                element_type = self.ui.comboBox_11.currentText()
            elif self.get_controller().is_coating is False:
                element_type = self.ui.comboBox_5.currentText()
            number = txt
            chara, unity, mat = self.get_controller().action_config_by_type_number(element_type, number)
            if self.get_controller().is_coating:
                self.tools_setup_combobox(self.ui.comboBox_14, items_init=chara)
                self.tools_setup_combobox(self.ui.comboBox_13, items_init=unity)
                self.tools_setup_table(self.ui.tableWidget_4, mat=mat, title=['attribute', 'value', 'unity'])
            elif self.get_controller().is_coating is False:
                self.tools_setup_combobox(self.ui.comboBox_8, items_init=chara)
                self.tools_setup_combobox(self.ui.comboBox_7, items_init=unity)
                self.tools_setup_table(self.ui.tableWidget_2, mat=mat, title=['attribute', 'value', 'unity'])

    def button_clicked_search(self):
        pass

    def button_clicked_create_element(self):
        element_type, number, attribute_name, unity, value = None, None, None, None, None
        if self.get_controller().is_coating:
            element_type = self.ui.comboBox_11.currentText()
            number = self.ui.comboBox_12.currentText()
            attribute_name = self.ui.comboBox_14.currentText()
            unity = self.ui.comboBox_13.currentText()
            value = self.ui.lineEdit_8.text()
        elif self.get_controller().is_coating is False:
            element_type = self.ui.comboBox_5.currentText()
            number = self.ui.comboBox_6.currentText()
            attribute_name = self.ui.comboBox_8.currentText()
            unity = self.ui.comboBox_7.currentText()
            value = self.ui.lineEdit_9.text()

        self.get_controller().action_create_element(element_type, number, attribute_name, unity, value)

    def disable_modify(self):
        strategy = self.get_controller().is_coating
        try:
            if strategy:
                self.tools_op_object(obj=self.ui.pushButton_14, opacity=0)
                self.ui.pushButton_14.clicked.disconnect(self.button_clicked_search)
                self.tools_op_object(obj=self.ui.pushButton_15, opacity=0)
                self.ui.pushButton_15.clicked.disconnect()
                self.tools_op_object(obj=self.ui.pushButton_12, opacity=0)
                self.ui.pushButton_12.clicked.disconnect()
                self.get_controller().flag_coating_enabled = False
            elif strategy is False:
                self.tools_op_object(obj=self.ui.pushButton_7, opacity=0)
                self.ui.pushButton_7.clicked.disconnect()
                self.tools_op_object(obj=self.ui.pushButton_8, opacity=0)
                self.ui.pushButton_8.clicked.disconnect()
                self.tools_op_object(obj=self.ui.pushButton_5, opacity=0)
                self.ui.pushButton_5.clicked.disconnect()
                self.get_controller().flag_detergent_enabled = False
        except TypeError:
            pass

    def enable_modify(self):
        strategy = self.get_controller().is_coating
        try:
            if strategy:
                self.tools_op_object(obj=self.ui.pushButton_14, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_15, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_12, opacity=1)
                self.ui.pushButton_14.clicked.connect(self.button_clicked_search)
                self.ui.pushButton_15.clicked.connect(self.button_clicked_create_element)
                self.ui.pushButton_12.clicked.connect(self.button_clicked_db_transfer)
                self.get_controller().flag_coating_enabled = True
            elif strategy is False:
                self.tools_op_object(obj=self.ui.pushButton_7, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_8, opacity=1)
                self.tools_op_object(obj=self.ui.pushButton_5, opacity=1)
                self.ui.pushButton_7.clicked.connect(self.button_clicked_search)
                self.ui.pushButton_8.clicked.connect(self.button_clicked_create_element)
                self.ui.pushButton_5.clicked.connect(self.button_clicked_db_transfer)
                self.get_controller().flag_detergent_enabled = True
        except TypeError:
            pass

    def one_click(self, strategy=None):
        if strategy:
            self.coating_validate_token = False
        elif strategy is False:
            self.detergent_validate_token = False

    def question_for_validate(self, strategy=None):
        if strategy:
            self.coating_validate_token = True
        elif strategy is False:
            self.detergent_validate_token = True

    def button_clicked_db_transfer(self):
        """
        validate与否
        """
        if self.get_controller().is_coating:
            if self.coating_validate_token:
                res = self.message.exec_()
                if res == 1024:
                    coating_name = self.ui.comboBox_11.currentText()
                    coating_number = self.ui.comboBox_12.currentText()
                    self.get_controller().action_validate_element(coating_name, coating_number)
            # 对coating界面清空
        elif self.get_controller().is_coating is False:
            if self.detergent_validate_token:
                res = self.message.exec_()
                if res == 1024:
                    detergent_name = self.ui.comboBox_5.currentText()
                    detergent_number = self.ui.comboBox_6.currentText()
                    self.get_controller().action_validate_element(detergent_name, detergent_number)
            # 对detergent界面清空
        self.get_controller().action_submit()

    def refresh_value(self, strategy=True):
        if strategy:
            self.ui.lineEdit_8.clear()
        elif strategy is False:
            self.ui.lineEdit_9.clear()
