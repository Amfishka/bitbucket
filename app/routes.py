from app import app, db
from .models import Request_payment, Requisites
from flask import render_template, request
from sqlalchemy import cast, String

@app.route('/')
@app.route('/index')
def index():
    title_for_html = "Список заявок на оплату"
    return render_template("index.html", title=title_for_html)

@app.route('/requisites')
def requisites():
    title_for_html = "Реквизиты"
    return render_template("requisites.html", title=title_for_html)


@app.route('/api/data/request_payment')
def data_request_payment():

    query = Request_payment.query

    # search filter

    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            cast(Request_payment.summ, String).like(f'%{search}%'),
            cast(Request_payment.requisites, String).like(search),
            Request_payment.status.like(f'%{search}%'),
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['summ', 'requisites', 'status']:
            col_name = 'id'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(Request_payment, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)
    
    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    return {
        'data': [rp.to_dict() for rp in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Request_payment.query.count(),
        'draw': request.args.get('draw', type=int),       
        }

@app.route('/api/data/requisites')
def data_requisites():

    query = Requisites.query

    # search filter

    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            cast(Requisites.limit, String).like(f'%{search}%'),
            Requisites.full_name.like(f'%{search}%'),
            Requisites.type_payment.like(f'%{search}%'),
            Requisites.type_card_or_account.like(f'%{search}%'),
            Requisites.number_phone.like(f'%{search}%'),
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['full_name', 'type_payment', 'type_card_or_account', 'number_phone', 'limit']:
            col_name = 'id'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(Requisites, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)
    
    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    return {
        'data': [rp.to_dict() for rp in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Requisites.query.count(),
        'draw': request.args.get('draw', type=int),       
        }
    
