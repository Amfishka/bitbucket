from flask_restful import Resource, reqparse
from .models import Request_payment, Requisites 
from flask import jsonify
from sqlalchemy import cast, Float


class Invoice(Resource):
    def post(self):
        """
        Получение id заявки и реквизитов
        ---
        tags:
          - Invoice
        parameters:
          - in: body
            name: body
            description: Invoice data
            required: true
            schema:
              type: object
              properties:
                requisites:
                  type: string
                  description: Requisites data
                amount:
                  type: number
                  description: Invoice amount
        responses:
          200:
            description: Invoice created successfully
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: Invoice ID
                  requisites:
                    type: object
                    properties:
                      full_name:
                        type: string
                        description: Full name
                      type_payment:
                        type: string
                        description: Payment type
                      type_card_or_account:
                        type: string
                        description: Card or account type
                      number_phone:
                        type: string
                        description: Phone number
                      limit:
                        type: number
                        description: Limit
       
        """           
        
        parser = reqparse.RequestParser()
        parser.add_argument("requisites",  help = 'This field cannot be blank', required = True)
        parser.add_argument("amount",  help = 'This field cannot be blank', required = True)

        req_data = parser.parse_args()
        requisites_data = req_data['requisites']
            
        amount = req_data['amount']

        query = Requisites.query.join(Requisites.rs_request_payment).filter(cast(Request_payment.summ, Float) == amount, Requisites.type_card_or_account == requisites_data).all()

        l = []
        for q in query:
            l.append(
                {
                    "id" : q.id,
                    "requisites" : {
                        'full_name': q.full_name,
                        'type_payment': q.type_payment,
                        'type_card_or_account': q.type_card_or_account,
                        'number_phone': q.number_phone,
                        'limit': q.limit
                    }
                }
            )
        return jsonify(l)
       
    
class Invoice_status(Resource):
    
    def post(self):
        """
        Получение статуса заявки
        ---
        tags:
          - InvoiceStatus
        parameters:
          - in: body
            name: body
            description: Invoice status data
            required: true
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: Invoice ID
        responses:
          200:
            description: Invoice status retrieved successfully
            schema:
              type: array
              items:
                type: object
                properties:
                  status:
                    type: string
                    description: Invoice status
        """
        parser = reqparse.RequestParser()
        parser.add_argument("id",  help = 'This field cannot be blank', required = True)
        

        req_data = parser.parse_args()
        id = req_data['id']

        query = Request_payment.query.filter(Request_payment.id == id).first()

        return [{"status" : query.status}]
