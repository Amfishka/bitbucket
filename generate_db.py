from app import db, app
from app.models import Request_payment, Requisites, Role_user, User
import json

'''
Для того, чтобы добавить данные в базу данных запустите данный файл.

'''

def table_Requisites_add_data():
    '''Заполнение таблицы с реквизитами'''
    try:
        with open("app/tmp/table_Requisites.json", "r") as f:
            data = json.load(f)
        with app.app_context():
            for d in data:
                r = Requisites(full_name = d["full_name"],
                        type_payment = d["type_payment"],
                        type_card_or_account = d["type_card_or_account"],
                        number_phone = d["number_phone"],
                        limit = int(d["numberrange"]))
                db.session.add(r)  
            db.session.commit()
        print("Заполнение таблицы с реквизитами завершено")
    except Exception as e:
        print("Ощипка при Заполнении таблицы с реквизитами : ", e)


def table_Request_payment_add_data():
    '''Заполнение таблицы с заявками на оплату'''
    try:
        with open("app/tmp/table_Request_payment.json", "r") as f:
            data = json.load(f)
        with app.app_context(): 
            for d in data:
                r = Request_payment(summ = float(d["summ"]),
                        requisites = int(d["requisites"]),
                        status = d["status"])
                db.session.add(r)
            db.session.commit()
        print("Заполнение таблицы с заявками на оплату завершено")
    except Exception as e:
        print("Ощипка при Заполнении таблицы с заявками на оплату : ", e)


def table_User_role():
    '''Заполнение таблицы ролей'''
    try:
        with app.app_context():
            role_admin = Role_user(name="admin")
            role_user = Role_user(name="user")
            db.session.add(role_admin)
            db.session.add(role_user)
            db.session.commit()
        print("Заполнение таблицы ролей завершено")
    except Exception as e:
        print("Ощипка при Заполнении таблицы ролей : ", e)


def table_User():
    '''Заполнение таблицы пользователей'''
    try:
        with app.app_context():
            # Создание админа
            u_admin = User(name="admin")
            u_admin.set_password('password')
            u_admin.set_admin()
            db.session.add(u_admin)

            # Создание пользователя
            u_user = User(name="andry")
            u_user.set_password('password')
            db.session.add(u_user)

            db.session.commit()
        print("Заполнение таблицы пользователей завершено")
    except Exception as e:
        print("Ощипка при Заполнении таблицы пользователей : ", e)

if __name__ == "__main__":
    print("Заполняем таблицы")
    table_Requisites_add_data()
    table_Request_payment_add_data()
    table_User_role()
    table_User()
