# Form implementation generated from reading ui file 'c:\Users\Arango\Mi unidad\PROGRAMACION\POSICIONES DEPOSITO\CONSOLIDADO\MOVIMIENTOS\modules\views\main_window\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 798)
        MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);\n"
"background-color: rgb(244, 247, 249);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_only_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_only_widget.setMinimumSize(QtCore.QSize(65, 0))
        self.icon_only_widget.setMaximumSize(QtCore.QSize(65, 16777215))
        self.icon_only_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(170, 30, 25);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
" border: none;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(211, 0, 0);\n"
"    font-size: 16px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(194, 70, 49);\n"
"}\n"
"")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.icon_only_layout_1 = QtWidgets.QHBoxLayout()
        self.icon_only_layout_1.setObjectName("icon_only_layout_1")
        self.icono_perfil_1 = QtWidgets.QLabel(parent=self.icon_only_widget)
        self.icono_perfil_1.setMinimumSize(QtCore.QSize(40, 40))
        self.icono_perfil_1.setMaximumSize(QtCore.QSize(40, 40))
        self.icono_perfil_1.setStyleSheet("background-color: rgb(131, 25, 27);\n"
"border-radius: 50%;")
        self.icono_perfil_1.setText("")
        self.icono_perfil_1.setPixmap(QtGui.QPixmap(":/Users/modules/views/gestion_usuarios/images/user_1.png"))
        self.icono_perfil_1.setScaledContents(True)
        self.icono_perfil_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.icono_perfil_1.setObjectName("icono_perfil_1")
        self.icon_only_layout_1.addWidget(self.icono_perfil_1)
        self.verticalLayout_3.addLayout(self.icon_only_layout_1)
        self.botones_layout_1 = QtWidgets.QVBoxLayout()
        self.botones_layout_1.setObjectName("botones_layout_1")
        self.ingresos_egresos_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.ingresos_egresos_1.setMinimumSize(QtCore.QSize(0, 40))
        self.ingresos_egresos_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ingresos_egresos_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ingresos_egresos_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/icono_ingresos.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ingresos_egresos_1.setIcon(icon)
        self.ingresos_egresos_1.setIconSize(QtCore.QSize(30, 30))
        self.ingresos_egresos_1.setCheckable(True)
        self.ingresos_egresos_1.setAutoExclusive(True)
        self.ingresos_egresos_1.setObjectName("ingresos_egresos_1")
        self.botones_layout_1.addWidget(self.ingresos_egresos_1)
        self.gestion_stock_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.gestion_stock_1.setMinimumSize(QtCore.QSize(0, 40))
        self.gestion_stock_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.gestion_stock_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.gestion_stock_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/icono_gestion.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.gestion_stock_1.setIcon(icon1)
        self.gestion_stock_1.setIconSize(QtCore.QSize(30, 30))
        self.gestion_stock_1.setCheckable(True)
        self.gestion_stock_1.setAutoExclusive(True)
        self.gestion_stock_1.setObjectName("gestion_stock_1")
        self.botones_layout_1.addWidget(self.gestion_stock_1)
        self.notas_pedido_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.notas_pedido_1.setMinimumSize(QtCore.QSize(0, 40))
        self.notas_pedido_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.notas_pedido_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.notas_pedido_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/icono_nota_pedido.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.notas_pedido_1.setIcon(icon2)
        self.notas_pedido_1.setIconSize(QtCore.QSize(30, 30))
        self.notas_pedido_1.setCheckable(True)
        self.notas_pedido_1.setAutoExclusive(True)
        self.notas_pedido_1.setObjectName("notas_pedido_1")
        self.botones_layout_1.addWidget(self.notas_pedido_1)
        self.productos_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.productos_1.setMinimumSize(QtCore.QSize(0, 40))
        self.productos_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.productos_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.productos_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/icono_admin.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.productos_1.setIcon(icon3)
        self.productos_1.setIconSize(QtCore.QSize(30, 30))
        self.productos_1.setCheckable(True)
        self.productos_1.setAutoExclusive(True)
        self.productos_1.setObjectName("productos_1")
        self.botones_layout_1.addWidget(self.productos_1)
        self.movimientos_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.movimientos_1.setMinimumSize(QtCore.QSize(0, 40))
        self.movimientos_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.movimientos_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.movimientos_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/icono_registros.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.movimientos_1.setIcon(icon4)
        self.movimientos_1.setIconSize(QtCore.QSize(30, 30))
        self.movimientos_1.setCheckable(True)
        self.movimientos_1.setAutoExclusive(True)
        self.movimientos_1.setObjectName("movimientos_1")
        self.botones_layout_1.addWidget(self.movimientos_1)
        self.usuarios_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.usuarios_1.setMinimumSize(QtCore.QSize(0, 40))
        self.usuarios_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.usuarios_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.usuarios_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/icono_usuarios.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.usuarios_1.setIcon(icon5)
        self.usuarios_1.setIconSize(QtCore.QSize(30, 30))
        self.usuarios_1.setCheckable(True)
        self.usuarios_1.setAutoExclusive(True)
        self.usuarios_1.setObjectName("usuarios_1")
        self.botones_layout_1.addWidget(self.usuarios_1)
        self.verticalLayout_3.addLayout(self.botones_layout_1)
        spacerItem = QtWidgets.QSpacerItem(20, 363, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.salir_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.salir_1.setMinimumSize(QtCore.QSize(0, 40))
        self.salir_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.salir_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.salir_1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/cerrar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.salir_1.setIcon(icon6)
        self.salir_1.setIconSize(QtCore.QSize(35, 35))
        self.salir_1.setCheckable(True)
        self.salir_1.setAutoExclusive(True)
        self.salir_1.setObjectName("salir_1")
        self.verticalLayout_3.addWidget(self.salir_1)
        self.horizontalLayout.addWidget(self.icon_only_widget)
        self.icon_name_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_name_widget.setMinimumSize(QtCore.QSize(200, 0))
        self.icon_name_widget.setMaximumSize(QtCore.QSize(230, 16777215))
        self.icon_name_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(170, 30, 25);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    text-align: left;\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"    height: 30px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(194, 70, 49);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(211, 0, 0);\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"")
        self.icon_name_widget.setObjectName("icon_name_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setContentsMargins(5, 15, 0, 0)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icono_perfil_2 = QtWidgets.QLabel(parent=self.icon_name_widget)
        self.icono_perfil_2.setMinimumSize(QtCore.QSize(40, 40))
        self.icono_perfil_2.setMaximumSize(QtCore.QSize(40, 40))
        self.icono_perfil_2.setStyleSheet("background-color: rgb(131, 25, 27);")
        self.icono_perfil_2.setText("")
        self.icono_perfil_2.setPixmap(QtGui.QPixmap(":/Users/modules/views/gestion_usuarios/images/user_1.png"))
        self.icono_perfil_2.setScaledContents(True)
        self.icono_perfil_2.setObjectName("icono_perfil_2")
        self.horizontalLayout_2.addWidget(self.icono_perfil_2)
        self.titulo_perfil_2 = QtWidgets.QLabel(parent=self.icon_name_widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.titulo_perfil_2.setFont(font)
        self.titulo_perfil_2.setStyleSheet("border-bottom-color: rgb(170, 0, 0);\n"
"border-bottom: 8px;")
        self.titulo_perfil_2.setObjectName("titulo_perfil_2")
        self.horizontalLayout_2.addWidget(self.titulo_perfil_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.botones_layout_2 = QtWidgets.QVBoxLayout()
        self.botones_layout_2.setObjectName("botones_layout_2")
        self.ingresos_egresos_2 = QtWidgets.QPushButton(parent=self.icon_name_widget)
        self.ingresos_egresos_2.setMinimumSize(QtCore.QSize(0, 40))
        self.ingresos_egresos_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.ingresos_egresos_2.setFont(font)
        self.ingresos_egresos_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ingresos_egresos_2.setIcon(icon)
        self.ingresos_egresos_2.setIconSize(QtCore.QSize(25, 25))
        self.ingresos_egresos_2.setCheckable(True)
        self.ingresos_egresos_2.setAutoExclusive(True)
        self.ingresos_egresos_2.setObjectName("ingresos_egresos_2")
        self.botones_layout_2.addWidget(self.ingresos_egresos_2)
        self.gestion_stock_2 = QtWidgets.QPushButton(parent=self.icon_name_widget)
        self.gestion_stock_2.setMinimumSize(QtCore.QSize(0, 40))
        self.gestion_stock_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.gestion_stock_2.setFont(font)
        self.gestion_stock_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.gestion_stock_2.setIcon(icon1)
        self.gestion_stock_2.setIconSize(QtCore.QSize(25, 25))
        self.gestion_stock_2.setCheckable(True)
        self.gestion_stock_2.setAutoExclusive(True)
        self.gestion_stock_2.setObjectName("gestion_stock_2")
        self.botones_layout_2.addWidget(self.gestion_stock_2)
        self.notas_pedido_2 = QtWidgets.QPushButton(parent=self.icon_name_widget)
        self.notas_pedido_2.setMinimumSize(QtCore.QSize(0, 40))
        self.notas_pedido_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.notas_pedido_2.setFont(font)
        self.notas_pedido_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.notas_pedido_2.setIcon(icon2)
        self.notas_pedido_2.setIconSize(QtCore.QSize(25, 25))
        self.notas_pedido_2.setCheckable(True)
        self.notas_pedido_2.setAutoExclusive(True)
        self.notas_pedido_2.setObjectName("notas_pedido_2")
        self.botones_layout_2.addWidget(self.notas_pedido_2)
        self.productos_2 = QtWidgets.QPushButton(parent=self.icon_name_widget)
        self.productos_2.setMinimumSize(QtCore.QSize(0, 40))
        self.productos_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.productos_2.setFont(font)
        self.productos_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.productos_2.setIcon(icon3)
        self.productos_2.setIconSize(QtCore.QSize(25, 25))
        self.productos_2.setCheckable(True)
        self.productos_2.setAutoExclusive(True)
        self.productos_2.setObjectName("productos_2")
        self.botones_layout_2.addWidget(self.productos_2)
        self.movimientos_2 = QtWidgets.QPushButton(parent=self.icon_name_widget)
        self.movimientos_2.setMinimumSize(QtCore.QSize(0, 40))
        self.movimientos_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.movimientos_2.setFont(font)
        self.movimientos_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.movimientos_2.setIcon(icon4)
        self.movimientos_2.setIconSize(QtCore.QSize(25, 25))
        self.movimientos_2.setCheckable(True)
        self.movimientos_2.setAutoExclusive(True)
        self.movimientos_2.setObjectName("movimientos_2")
        self.botones_layout_2.addWidget(self.movimientos_2)
        self.usuarios_2 = QtWidgets.QPushButton(parent=self.icon_name_widget)
        self.usuarios_2.setMinimumSize(QtCore.QSize(0, 40))
        self.usuarios_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.usuarios_2.setFont(font)
        self.usuarios_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.usuarios_2.setIcon(icon5)
        self.usuarios_2.setIconSize(QtCore.QSize(25, 25))
        self.usuarios_2.setCheckable(True)
        self.usuarios_2.setAutoExclusive(True)
        self.usuarios_2.setObjectName("usuarios_2")
        self.botones_layout_2.addWidget(self.usuarios_2)
        self.verticalLayout_4.addLayout(self.botones_layout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 358, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.salir_button = QtWidgets.QPushButton(parent=self.icon_name_widget)
        self.salir_button.setMinimumSize(QtCore.QSize(0, 40))
        self.salir_button.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.salir_button.setFont(font)
        self.salir_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.salir_button.setIcon(icon6)
        self.salir_button.setIconSize(QtCore.QSize(25, 25))
        self.salir_button.setCheckable(True)
        self.salir_button.setAutoExclusive(True)
        self.salir_button.setObjectName("salir_button")
        self.verticalLayout_4.addWidget(self.salir_button)
        self.horizontalLayout.addWidget(self.icon_name_widget)
        self.main_menu_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_menu_widget.setStyleSheet("background-color: rgb(244, 247, 249);")
        self.main_menu_widget.setObjectName("main_menu_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_menu_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.navbar_widget = QtWidgets.QWidget(parent=self.main_menu_widget)
        self.navbar_widget.setMinimumSize(QtCore.QSize(0, 60))
        self.navbar_widget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  rgb(212, 131, 131), stop:1 rgb(225, 186, 187));\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.navbar_widget.setObjectName("navbar_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.navbar_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.navbar_layout = QtWidgets.QHBoxLayout()
        self.navbar_layout.setContentsMargins(4, 4, 4, 4)
        self.navbar_layout.setSpacing(4)
        self.navbar_layout.setObjectName("navbar_layout")
        self.menu_button = QtWidgets.QPushButton(parent=self.navbar_widget)
        self.menu_button.setMinimumSize(QtCore.QSize(0, 30))
        self.menu_button.setMaximumSize(QtCore.QSize(30, 30))
        self.menu_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menu_button.setStyleSheet("color: rgb(117, 25, 25);\n"
"background-color: rgb(212, 131, 131);\n"
"border: none;")
        self.menu_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Sidebar/modules/views/main_window/images/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menu_button.setIcon(icon7)
        self.menu_button.setIconSize(QtCore.QSize(30, 30))
        self.menu_button.setCheckable(True)
        self.menu_button.setObjectName("menu_button")
        self.navbar_layout.addWidget(self.menu_button)
        spacerItem2 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.navbar_layout.addItem(spacerItem2)
        self.header_title = QtWidgets.QLabel(parent=self.navbar_widget)
        self.header_title.setStyleSheet("background-color: none;")
        self.header_title.setObjectName("header_title")
        self.navbar_layout.addWidget(self.header_title)
        spacerItem3 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.navbar_layout.addItem(spacerItem3)
        self.search_input = QtWidgets.QLineEdit(parent=self.navbar_widget)
        self.search_input.setMinimumSize(QtCore.QSize(190, 35))
        self.search_input.setMaximumSize(QtCore.QSize(190, 35))
        self.search_input.setStyleSheet("background-color: rgb(255, 251, 212);")
        self.search_input.setObjectName("search_input")
        self.navbar_layout.addWidget(self.search_input)
        self.search_button = QtWidgets.QPushButton(parent=self.navbar_widget)
        self.search_button.setMinimumSize(QtCore.QSize(65, 35))
        self.search_button.setMaximumSize(QtCore.QSize(65, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.search_button.setStyleSheet("background-color: rgb(131, 25, 27);\n"
"font: 700 italic 10pt \"Segoe UI\";\n"
"border-radius: 8px;")
        self.search_button.setObjectName("search_button")
        self.navbar_layout.addWidget(self.search_button)
        self.horizontalLayout_3.addLayout(self.navbar_layout)
        self.verticalLayout_5.addWidget(self.navbar_widget)
        self.main_widget = QtWidgets.QStackedWidget(parent=self.main_menu_widget)
        self.main_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_widget.setObjectName("main_widget")
        self.ingresos_egresos_page = QtWidgets.QWidget()
        self.ingresos_egresos_page.setObjectName("ingresos_egresos_page")
        self.main_widget.addWidget(self.ingresos_egresos_page)
        self.gestion_stock_page = QtWidgets.QWidget()
        self.gestion_stock_page.setObjectName("gestion_stock_page")
        self.main_widget.addWidget(self.gestion_stock_page)
        self.notas_pedido_page = QtWidgets.QWidget()
        self.notas_pedido_page.setObjectName("notas_pedido_page")
        self.main_widget.addWidget(self.notas_pedido_page)
        self.productos_page = QtWidgets.QWidget()
        self.productos_page.setObjectName("productos_page")
        self.main_widget.addWidget(self.productos_page)
        self.movimientos_page = QtWidgets.QWidget()
        self.movimientos_page.setObjectName("movimientos_page")
        self.main_widget.addWidget(self.movimientos_page)
        self.usuarios_page = QtWidgets.QWidget()
        self.usuarios_page.setObjectName("usuarios_page")
        self.main_widget.addWidget(self.usuarios_page)
        self.verticalLayout_5.addWidget(self.main_widget)
        self.bottombar_widget = QtWidgets.QWidget(parent=self.main_menu_widget)
        self.bottombar_widget.setMinimumSize(QtCore.QSize(0, 60))
        self.bottombar_widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.bottombar_widget.setStyleSheet("QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  rgb(212, 131, 131), stop:1 rgb(225, 186, 187));\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"border-radius: 5px;")
        self.bottombar_widget.setObjectName("bottombar_widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.bottombar_widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bottombar_layout = QtWidgets.QHBoxLayout()
        self.bottombar_layout.setObjectName("bottombar_layout")
        self.horizontalLayout_6.addLayout(self.bottombar_layout)
        self.verticalLayout_5.addWidget(self.bottombar_widget)
        self.horizontalLayout.addWidget(self.main_menu_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_button.toggled['bool'].connect(self.icon_only_widget.setHidden) # type: ignore
        self.menu_button.toggled['bool'].connect(self.icon_name_widget.setVisible) # type: ignore
        self.usuarios_1.toggled['bool'].connect(self.usuarios_2.setChecked) # type: ignore
        self.movimientos_1.toggled['bool'].connect(self.movimientos_2.setChecked) # type: ignore
        self.productos_1.toggled['bool'].connect(self.productos_2.setChecked) # type: ignore
        self.notas_pedido_1.toggled['bool'].connect(self.notas_pedido_2.setChecked) # type: ignore
        self.gestion_stock_1.toggled['bool'].connect(self.gestion_stock_2.setChecked) # type: ignore
        self.ingresos_egresos_1.toggled['bool'].connect(self.ingresos_egresos_2.setChecked) # type: ignore
        self.ingresos_egresos_2.toggled['bool'].connect(self.ingresos_egresos_1.setChecked) # type: ignore
        self.gestion_stock_2.toggled['bool'].connect(self.gestion_stock_1.setChecked) # type: ignore
        self.notas_pedido_2.toggled['bool'].connect(self.notas_pedido_1.setChecked) # type: ignore
        self.productos_2.toggled['bool'].connect(self.productos_1.setChecked) # type: ignore
        self.movimientos_2.toggled['bool'].connect(self.movimientos_1.setChecked) # type: ignore
        self.usuarios_2.toggled['bool'].connect(self.usuarios_1.setChecked) # type: ignore
        self.salir_1.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.salir_button.toggled['bool'].connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo_perfil_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Menu</p></body></html>"))
        self.ingresos_egresos_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.ingresos_egresos_2.setText(_translate("MainWindow", "Ingresos / Egresos"))
        self.gestion_stock_2.setText(_translate("MainWindow", "Gestión de Stock"))
        self.notas_pedido_2.setText(_translate("MainWindow", "Notas de Pedido"))
        self.productos_2.setText(_translate("MainWindow", "Productos"))
        self.movimientos_2.setText(_translate("MainWindow", "Movimientos"))
        self.usuarios_2.setText(_translate("MainWindow", "Usuarios"))
        self.salir_button.setText(_translate("MainWindow", "Salir"))
        self.header_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">TextLabel</span></p></body></html>"))
        self.search_button.setText(_translate("MainWindow", "Buscar"))
