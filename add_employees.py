# Form implementation generated from reading ui file 'add_employees.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_add_employees(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 308)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.te_emp_numb = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_emp_numb.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.te_emp_numb.setObjectName("te_emp_numb")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 71, 18))
        self.label_4.setObjectName("label_4")
        self.te_emp_pos = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_emp_pos.setGeometry(QtCore.QRect(150, 40, 181, 31))
        self.te_emp_pos.setObjectName("te_emp_pos")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(150, 20, 61, 18))
        self.label_7.setObjectName("label_7")
        self.te_emp_name = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_emp_name.setGeometry(QtCore.QRect(10, 110, 261, 31))
        self.te_emp_name.setObjectName("te_emp_name")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 71, 18))
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 160, 71, 18))
        self.label_11.setObjectName("label_11")
        self.te_emp_phone = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_emp_phone.setGeometry(QtCore.QRect(10, 180, 161, 31))
        self.te_emp_phone.setObjectName("te_emp_phone")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(190, 160, 61, 18))
        self.label_12.setObjectName("label_12")
        self.te_emp_mail = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_emp_mail.setGeometry(QtCore.QRect(190, 180, 221, 31))
        self.te_emp_mail.setObjectName("te_emp_mail")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить запись (Employees)"))
        self.label_4.setText(_translate("Dialog", "emp_numb"))
        self.label_7.setText(_translate("Dialog", "emp_pos"))
        self.label_5.setText(_translate("Dialog", "emp_name"))
        self.label_11.setText(_translate("Dialog", "emp_phone"))
        self.label_12.setText(_translate("Dialog", "emp_mail"))