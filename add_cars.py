# Form implementation generated from reading ui file 'add_cars.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_add_cars(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 432)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 181, 18))
        self.label.setObjectName("label")
        self.te_car_numb = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_numb.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.te_car_numb.setObjectName("te_car_numb")
        self.te_car_brand = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_brand.setGeometry(QtCore.QRect(10, 110, 201, 31))
        self.te_car_brand.setObjectName("te_car_brand")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 181, 18))
        self.label_3.setObjectName("label_3")
        self.te_car_branch = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_branch.setGeometry(QtCore.QRect(140, 40, 71, 31))
        self.te_car_branch.setObjectName("te_car_branch")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(140, 20, 181, 18))
        self.label_4.setObjectName("label_4")
        self.te_car_model = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_model.setGeometry(QtCore.QRect(240, 110, 181, 31))
        self.te_car_model.setObjectName("te_car_model")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(240, 90, 181, 18))
        self.label_7.setObjectName("label_7")
        self.te_car_status = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_status.setGeometry(QtCore.QRect(240, 40, 181, 31))
        self.te_car_status.setObjectName("te_car_status")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(240, 20, 181, 18))
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 160, 181, 18))
        self.label_11.setObjectName("label_11")
        self.te_car_class = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_class.setGeometry(QtCore.QRect(10, 180, 201, 31))
        self.te_car_class.setObjectName("te_car_class")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(240, 160, 91, 18))
        self.label_12.setObjectName("label_12")
        self.te_car_type = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_type.setGeometry(QtCore.QRect(240, 180, 181, 31))
        self.te_car_type.setObjectName("te_car_type")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(240, 230, 111, 18))
        self.label_13.setObjectName("label_13")
        self.te_car_license = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_license.setGeometry(QtCore.QRect(240, 250, 121, 31))
        self.te_car_license.setObjectName("te_car_license")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 230, 181, 18))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 300, 121, 18))
        self.label_15.setObjectName("label_15")
        self.te_car_rent = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.te_car_rent.setGeometry(QtCore.QRect(10, 320, 101, 31))
        self.te_car_rent.setObjectName("te_car_rent")
        self.de_datareg = QtWidgets.QDateEdit(parent=self.groupBox)
        self.de_datareg.setGeometry(QtCore.QRect(10, 250, 111, 32))
        self.de_datareg.setObjectName("de_datareg")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить запись (Cars)"))
        self.label.setText(_translate("Dialog", "car_numb"))
        self.label_3.setText(_translate("Dialog", "car_brand"))
        self.label_4.setText(_translate("Dialog", "car_branch"))
        self.label_7.setText(_translate("Dialog", "car_model"))
        self.label_5.setText(_translate("Dialog", "car_status"))
        self.label_11.setText(_translate("Dialog", "car_class"))
        self.label_12.setText(_translate("Dialog", "car_type"))
        self.label_13.setText(_translate("Dialog", "car_license"))
        self.label_14.setText(_translate("Dialog", "car_datareg"))
        self.label_15.setText(_translate("Dialog", "car_rent"))
        self.de_datareg.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
