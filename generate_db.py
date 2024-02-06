from app import db, app
from app.models import Request_payment, Requisites
import json

# Таблица 1
def table_Requisites_add_data():
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


def table_Request_payment_add_data():
    with open("app/tmp/table_Request_payment.json", "r") as f:
        data = json.load(f)
    with app.app_context(): 
        for d in data:
            r = Request_payment(summ = float(d["summ"]),
                    requisites = int(d["requisites"]),
                    status = d["status"])
            db.session.add(r)
        db.session.commit()

if __name__ == "__main__":
    table_Requisites_add_data()
    table_Request_payment_add_data()

