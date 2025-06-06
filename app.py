from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient
client = MongoClient('mongodb+srv://PW.7ut4dib.mongodb.net/')
db = client.dbhomework

app = Flask(__name__)

## HTML
@app.route('/')
def homework():
    return render_template('index.html')


# POST API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.homework.insert_one(doc)
    return jsonify({'result': 'success'})


# Read API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.homework.find({},{'_id':0}).sort('_id',-1))
    # print(orders)
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
