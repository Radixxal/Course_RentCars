from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from UserInterface import Ui_MainWindow
import sys
import psycopg2
from config import host, user, password, db_name, port
from add_branches import Ui_Dialog_add_branches
from add_cars import Ui_Dialog_add_cars
from add_clients import Ui_Dialog_add_clients
from add_employees import Ui_Dialog_add_employees
from add_repairs import Ui_Dialog_add_repairs
from add_rents import Ui_Dialog_add_rents

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Разметка при клике
        self.ui.bt_showBranches.clicked.connect(self.mark_table_Branches)
        self.ui.bt_showCars.clicked.connect(self.mark_table_Cars)
        self.ui.bt_showClients.clicked.connect(self.mark_table_Clients)
        self.ui.bt_showEmployees.clicked.connect(self.mark_table_Employees)
        self.ui.bt_showRepairs.clicked.connect(self.mark_table_Repairs)
        self.ui.bt_showRents.clicked.connect(self.mark_table_Rents)

        # Отображение таблицы при клике
        self.ui.bt_showBranches.clicked.connect(lambda: self.show_table("Branches"))
        self.ui.bt_showCars.clicked.connect(lambda: self.show_table("Cars"))
        self.ui.bt_showClients.clicked.connect(lambda: self.show_table("Clients"))
        self.ui.bt_showEmployees.clicked.connect(lambda: self.show_table("Employees"))
        self.ui.bt_showRepairs.clicked.connect(lambda: self.show_table("Repairs"))
        self.ui.bt_showRents.clicked.connect(lambda: self.show_table("Rents"))
        self.ui.bt_addRow.clicked.connect(self.add_row)
        self.ui.bt_editRow.clicked.connect(self.dialog_editRents)
        self.ui.bt_delRow.clicked.connect(self.del_row)


    # Глобальные переменные
    sqlquery = ""
    connection = ""
    selectedTable = ""

    # Добавление записи в текущую таблицу.
    def add_row(self):

        match self.selectedTable:
            case "Branches":
                self.dialog_addBranches()
            case "Cars":
                self.dialog_addCars()
            case "Clients":
                self.dialog_addClients()
            case "Employees":
                self.dialog_addEmployees()
            case "Repairs":
                self.dialog_addRepairs()
            case "Rents":
                self.dialog_addRents()
            case _:
                print("The table not selected")

    # Подключение к базе данных
    def connect_pg1(self):
        try:
            self.connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port
            )
            cur = self.connection.cursor()
            return cur
        except psycopg2.OperationalError:
            self.show_errorMessage("обращения к базе данных.")
            sys.exit()

    # Разметка TableWidget
    def mark_clear(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)

    def mark_table_Branches(self):
        self.mark_clear()
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(["br_id", "br_numb", "br_region", "br_city", "br_deistrict", "br_addr"])
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
    def mark_table_Cars(self):
        self.mark_clear()
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setHorizontalHeaderLabels(["car_id", "car_numb", "car_branch", "car_status", "car_brand",
                                                       "car_model", "car_class", "car_type", "car_license", "car_datareg", "car_rent"])
    def mark_table_Clients(self):
        self.mark_clear()
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(["cl_id", "cl_name", "cl_license", "cl_experience", "cl_pass",
                                                       "cl_phone", "cl_mail", "cl_language", "cl_citizenship"])

    def mark_table_Employees(self):
        self.mark_clear()
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(["emp_id", "emp_numb", "emp_pos", "emp_name", "emp_mail", "emp_phone"])

    def mark_table_Repairs(self):
        self.mark_clear()
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(["rep_id", "rep_car", "rep_start", "rep_finish", "rep_purpose", "rep_details", "rep_status"])

    def mark_table_Rents(self):
        self.mark_clear()
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setHorizontalHeaderLabels(["rent_id", "rent_car", "rent_client", "rent_employee", "rent_branch_take",
                                                       "rent_branch_give", "rent_start", "rent_finish", "rent_deposite", "rent_totalp", "rent_status"])


    def show_table(self, table):
        self.selectedTable = table
        #####
        cur = self.connect_pg1()

        self.sqlquery = F"SELECT * FROM {table}"

        cur.execute(self.sqlquery)
        result = cur.fetchall()

        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))

    def add_row_branches(self, br_numb, br_region, br_city, br_district, br_addr):

        if br_numb.__len__() == 0 or br_city.__len__() == 0 or br_addr.__len__() == 0 or br_region.__len__() == 0 or br_district.__len__() == 0:
            self.show_warningMessage("Входные данные имеют пустые значения. Проверьте правильность ввода.")
            return

        cur = self.connect_pg1()

        self.sqlquery = F"INSERT INTO Branches(br_numb, br_region, br_city, br_district, br_addr) VALUES('{br_numb}', '{br_region}', '{br_city}', '{br_district}', '{br_addr}')"

        cur.execute(self.sqlquery)

        self.connection.commit()

    def add_row_cars(self, car_numb, car_branch, car_status, car_brand, car_model, car_class, car_type, car_license, car_datareg, car_rent):

        if car_numb.__len__() == 0 or car_branch.__len__() == 0 or car_status.__len__() == 0 or car_brand.__len__() == 0 or car_model.__len__() == 0 or car_class.__len__() == 0 or car_type.__len__() == 0 or car_license.__len__() == 0 or car_datareg.__len__() == 0 or car_rent.__len__() == 0:
            self.show_warningMessage("Входные данные имеют пустые значения. Проверьте правильность ввода.")
            return

        cur = self.connect_pg1()

        self.sqlquery = F"INSERT INTO Cars(car_numb, car_branch, car_status, car_brand, car_model, car_class, car_type, car_license, car_datareg, car_rent) VALUES('{car_numb}', {car_branch}, '{car_status}', '{car_brand}', '{car_model}', '{car_class}', '{car_type}', '{car_license}', '{car_datareg}', {car_rent})"

        cur.execute(self.sqlquery)

        self.connection.commit()

    def add_row_clients(self, cl_name, cl_license, cl_experience, cl_pass, cl_phone, cl_mail, cl_language, cl_citizenship):

        if cl_name.__len__() == 0 or cl_license.__len__() == 0 or cl_experience.__len__() == 0 or cl_pass.__len__() == 0 or cl_phone.__len__() == 0 or cl_mail.__len__() == 0 or cl_language.__len__() == 0 or cl_citizenship.__len__() == 0:
            self.show_warningMessage("Входные данные имеют пустые значения. Проверьте правильность ввода.")
            return

        cur = self.connect_pg1()

        self.sqlquery = F"INSERT INTO Clients(cl_name, cl_license, cl_experience, cl_pass, cl_phone, cl_mail, cl_language, cl_citizenship) VALUES('{cl_name}', '{cl_license}', {cl_experience}, '{cl_pass}', '{cl_phone}', '{cl_mail}', '{cl_language}', '{cl_citizenship}')"

        cur.execute(self.sqlquery)

        self.connection.commit()

    def add_row_employees(self, emp_numb, emp_pos, emp_name, emp_mail, emp_phone):

        if emp_numb.__len__() == 0 or emp_pos.__len__() == 0 or emp_name.__len__() == 0 or emp_mail.__len__() == 0 or emp_phone.__len__() == 0:
            self.show_warningMessage("Входные данные имеют пустые значения. Проверьте правильность ввода.")
            return

        cur = self.connect_pg1()

        self.sqlquery = F"INSERT INTO Employees(emp_numb, emp_pos, emp_name, emp_mail, emp_phone) VALUES('{emp_numb}', '{emp_pos}', '{emp_name}', '{emp_mail}', '{emp_phone}')"

        cur.execute(self.sqlquery)

        self.connection.commit()

    def add_row_repairs(self, rep_car, rep_start, rep_finish, rep_purpose, rep_details, rep_status):

        if rep_car.__len__() == 0 or rep_start.__len__() == 0 or rep_finish.__len__() == 0 or rep_purpose.__len__() == 0 or rep_details.__len__() == 0 or rep_status.__len__() == 0:
            self.show_warningMessage("Входные данные имеют пустые значения. Проверьте правильность ввода.")
            return

        cur = self.connect_pg1()

        self.sqlquery = F"INSERT INTO Repairs(rep_car, rep_start, rep_finish, rep_purpose, rep_details, rep_status) VALUES({rep_car}, '{rep_start}', '{rep_finish}', '{rep_purpose}', '{rep_details}', '{rep_status}')"

        cur.execute(self.sqlquery)

        self.connection.commit()

    def add_row_rents(self, rent_car, rent_client, rent_employee, rent_branch_take, rent_branch_give, rent_start, rent_finish, rent_deposite, rent_totalp, rent_status):

        if rent_car.__len__() == 0 or rent_client.__len__() == 0 or rent_employee.__len__() == 0 or rent_branch_take.__len__() == 0 or rent_branch_give.__len__() == 0 or rent_start.__len__() == 0 or rent_finish.__len__() == 0 or rent_deposite.__len__() == 0 or rent_totalp.__len__() == 0 or rent_status.__len__() == 0:
            self.show_warningMessage("Входные данные имеют пустые значения. Проверьте правильность ввода.")
            return

        cur = self.connect_pg1()

        self.sqlquery = F"INSERT INTO Rents(rent_car, rent_client, rent_employee, rent_branch_take, rent_branch_give, rent_start, rent_finish, rent_deposite, rent_totalp, rent_status) VALUES({rent_car}, {rent_client}, {rent_employee}, {rent_branch_take}, {rent_branch_give}, '{rent_start}', '{rent_finish}', {rent_deposite}, {rent_totalp}, '{rent_status}')"

        cur.execute(self.sqlquery)

        self.connection.commit()


    def dialog_addBranches(self):

        app = QtWidgets.QDialog()
        application = Ui_Dialog_add_branches()
        application.setupUi(app)
        app.show()

        rsp = app.exec()

        if rsp:
            br_numb_in = application.te_br_numb.toPlainText()
            br_region_in = application.te_br_region.toPlainText()
            br_city_in = application.te_br_city.toPlainText()
            br_district_in = application.te_br_district.toPlainText()
            br_addr_in = application.te_br_addr.toPlainText()

            self.add_row_branches(br_numb_in, br_region_in, br_city_in, br_district_in, br_addr_in)
        else:
            print("Adding row to the Branches has canceled.")

    def dialog_addCars(self):

        app = QtWidgets.QDialog()
        application = Ui_Dialog_add_cars()
        application.setupUi(app)
        app.show()

        rsp = app.exec()

        if rsp:
            car_numb = application.te_car_numb.toPlainText()
            car_branch = application.te_car_branch.toPlainText()
            car_status = application.te_car_status.toPlainText()
            car_brand = application.te_car_brand.toPlainText()
            car_model = application.te_car_model.toPlainText()
            car_class = application.te_car_class.toPlainText()
            car_type = application.te_car_type.toPlainText()
            car_license = application.te_car_license.toPlainText()
            car_datareg = application.de_datareg.text()
            car_rent = application.te_car_rent.toPlainText()

            self.add_row_cars(car_numb, car_branch, car_status, car_brand, car_model, car_class, car_type, car_license, car_datareg, car_rent)
        else:
            print("Adding row to the Cars has canceled.")

    def dialog_addClients(self):
        app = QtWidgets.QDialog()
        application = Ui_Dialog_add_clients()
        application.setupUi(app)
        app.show()

        rsp = app.exec()
        if rsp:
            cl_name = application.te_cl_name.toPlainText()
            cl_license = application.te_cl_license.toPlainText()
            cl_experience = application.sb_cl_experience.text()
            cl_pass = application.te_cl_pass.toPlainText()
            cl_phone = application.te_cl_phone.toPlainText()
            cl_mail = application.te_cl_mail.toPlainText()
            cl_language = application.te_cl_language.toPlainText()
            cl_citizenship = application.te_cl_citizenship.toPlainText()


            self.add_row_clients(cl_name, cl_license, cl_experience, cl_pass, cl_phone, cl_mail, cl_language, cl_citizenship)
        else:
            print("Adding row to the Clients has canceled.")

    def dialog_addEmployees(self):
        app = QtWidgets.QDialog()
        application = Ui_Dialog_add_employees()
        application.setupUi(app)
        app.show()

        rsp = app.exec()
        if rsp:
            emp_numb = application.te_emp_numb.toPlainText()
            emp_pos = application.te_emp_pos.toPlainText()
            emp_name = application.te_emp_name.toPlainText()
            emp_phone = application.te_emp_phone.toPlainText()
            emp_mail = application.te_emp_mail.toPlainText()

            self.add_row_employees(emp_numb, emp_pos, emp_name, emp_mail, emp_phone)
        else:
            print("Adding row to the Employees has canceled.")

    def dialog_addRepairs(self):
        app = QtWidgets.QDialog()
        application = Ui_Dialog_add_repairs()
        application.setupUi(app)
        app.show()

        rsp = app.exec()
        if rsp:
            rep_car = application.te_rep_car.toPlainText()
            rep_start = application.de_rep_start.text()
            rep_finish = application.de_rep_finish.text()
            rep_purpose = application.te_rep_purpose.toPlainText()
            rep_details = application.te_rep_details.toPlainText()
            rep_status = application.te_rep_status.toPlainText()

            self.add_row_repairs(rep_car, rep_start, rep_finish, rep_purpose, rep_details, rep_status)
        else:
            print("Adding row to the Repairs has canceled.")

    def dialog_addRents(self):
        app = QtWidgets.QDialog()
        application = Ui_Dialog_add_rents()
        application.setupUi(app)
        app.show()

        rsp = app.exec()
        if rsp:
            rent_car = application.te_rent_car.toPlainText()
            rent_client = application.te_rent_client.toPlainText()
            rent_employee = application.te_rent_employee.toPlainText()
            rent_branch_take = application.te_rent_branch_take.toPlainText()
            rent_branch_give = application.rent_branch_give.toPlainText()
            rent_start = application.de_rent_start.text()
            rent_finish = application.de_rent_finish.text()
            rent_deposite = application.te_rent_deposite.toPlainText()
            rent_totalp = application.te_rent_totalp.toPlainText()
            rent_status = application.te_rent_status.toPlainText()

            self.add_row_rents(rent_car, rent_client, rent_employee, rent_branch_take, rent_branch_give, rent_start, rent_finish, rent_deposite, rent_totalp, rent_status)
        else:
            print("Adding row to the Rents has canceled.")

    def editRents(self, rent_id, rent_car, rent_client, rent_employee, rent_branch_take, rent_branch_give, rent_deposite, rent_totalp, rent_status):
        if rent_car.__len__() == 0 or rent_client.__len__() == 0 or rent_employee.__len__() == 0 or rent_branch_take.__len__() == 0 or rent_branch_give.__len__() == 0 or rent_deposite.__len__() == 0 or rent_totalp.__len__() == 0 or rent_status.__len__() == 0:
            self.show_warningMessage("Входные данные имеют пустые значения. Проверьте правильность ввода.")
            return

        cur = self.connect_pg1()

        self.sqlquery = F"UPDATE Rents SET rent_car = {rent_car}, rent_client = {rent_client}, rent_employee = {rent_employee}, rent_branch_take = {rent_branch_take}, rent_branch_give = {rent_branch_give} , rent_deposite = {rent_deposite}, rent_totalp = {rent_totalp}, rent_status = '{rent_status}' WHERE rent_id = {rent_id}"

        cur.execute(self.sqlquery)

        self.connection.commit()

    def dialog_editRents(self):
        app = QtWidgets.QDialog()
        application = Ui_Dialog_add_rents()
        application.setupUi(app)
        app.show()

        cur_row = self.ui.tableWidget.currentRow()
        rent_id = self.getIdOfRow()

        application.te_rent_car.setPlainText(self.ui.tableWidget.item(cur_row, 1).text())
        application.te_rent_client.setPlainText(self.ui.tableWidget.item(cur_row, 2).text())
        application.te_rent_employee.setPlainText(self.ui.tableWidget.item(cur_row, 3).text())
        application.te_rent_branch_take.setPlainText(self.ui.tableWidget.item(cur_row, 4).text())
        application.rent_branch_give.setPlainText(self.ui.tableWidget.item(cur_row, 5).text())
        application.te_rent_deposite.setPlainText(self.ui.tableWidget.item(cur_row, 8).text())
        application.te_rent_totalp.setPlainText(self.ui.tableWidget.item(cur_row, 9).text())
        application.te_rent_status.setPlainText(self.ui.tableWidget.item(cur_row, 10).text())


        rsp = app.exec()
        if rsp:
            rent_car = application.te_rent_car.toPlainText()
            rent_client = application.te_rent_client.toPlainText()
            rent_employee = application.te_rent_employee.toPlainText()
            rent_branch_take = application.te_rent_branch_take.toPlainText()
            rent_branch_give = application.rent_branch_give.toPlainText()
            rent_deposite = application.te_rent_deposite.toPlainText()
            rent_totalp = application.te_rent_totalp.toPlainText()
            rent_status = application.te_rent_status.toPlainText()

            self.editRents(rent_id, rent_car, rent_client, rent_employee, rent_branch_take, rent_branch_give, rent_deposite, rent_totalp, rent_status)
        else:
            print("Adding row to the Rents has canceled.")


    def del_row(self):
        id = self.getIdOfRow()

        cur = self.connect_pg1()

        self.sqlquery = F"DELETE FROM {self.selectedTable} WHERE {self.ui.tableWidget.horizontalHeaderItem(0).text()} = {id}"

        cur.execute(self.sqlquery)

        self.connection.commit()

    def show_errorMessage(self, typeOfError):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(F"{typeOfError}")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def show_warningMessage(self, typeOfError):
        msg = QMessageBox()
        msg.setWindowTitle("Предупреждение")
        msg.setText(F"{typeOfError}")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def getIdOfRow(self):
        cur_row = self.ui.tableWidget.currentRow()

        cur_idofRow = self.ui.tableWidget.item(cur_row, 0).text()

        return cur_idofRow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

