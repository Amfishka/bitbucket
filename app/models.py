from app import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100))
    #role = db.Column(db.String(50), default="user")

    def __repr__(self):
        return f"{self.name}"

class Requisites(db.Model):
    __tablename__ = "requisites"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    type_payment = db.Column(db.String(100), nullable=False) 
    type_card_or_account = db.Column(db.String(100), nullable=False)
    number_phone = db.Column(db.String, nullable=False)
    limit = db.Column(db.Integer, nullable=False)

    rs_request_payment= db.relationship("Request_payment", backref="requisite")

    def __repr__(self):
        return f"Реквизиты № {self.id}"

    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'type_payment': self.type_payment,
            'type_card_or_account': self.type_card_or_account,
            'number_phone': self.number_phone,
            'limit': self.limit,
        }


class Request_payment(db.Model):
    __tablename__ = "request_payment"
    id = db.Column(db.Integer, primary_key=True)
    summ = db.Column(db.Float, nullable=False)
    requisites = db.Column(db.Integer, db.ForeignKey(Requisites.id))
    status = db.Column(db.String(100), nullable=False)

    # tmp
    def to_dict(self):
        return {
            'id': self.id,
            'summ': self.summ,
            'requisites': self.requisites,
            'status': self.status,
        }

    