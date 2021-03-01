from flask_sqlalchemy import SQLAlchemy  # add
from datetime import datetime  # add

from flask import Flask, render_template, request, redirect 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application_dev.db'  # add
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # add


# add
class Server(db.Model):
    name = "Server"
    _id = db.Column(db.Integer, primary_key=True)
    server_type = db.Column(db.String(255))
    server_brand = db.Column(db.String(255))
    server_model = db.Column(db.String(255))
    server_specs = db.Column(db.String(255))
    business_type = db.Column(db.String(255))
    current_server_wattage = db.Column(db.String(255))
    cloud_server_wattage = db.Column(db.String(255))
    in_premise_cost_server = db.Column(db.String(255))
    cloud_cost_server = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
#    def __repr__(self):
#        return '<Server %r>' % self.name



class Network(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    network_type = db.Column(db.String(255))
    network_brand = db.Column(db.String(255))
    network_model = db.Column(db.String(255))
    network_specs = db.Column(db.String(255))
    business_type = db.Column(db.String(255))
    current_network_wattage = db.Column(db.String(255))
    cloud_network_wattage = db.Column(db.String(255))
    in_premise_cost_network = db.Column(db.String(255))
    cloud_cost_network = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    def __repr__(self):
        return '<Network %r>' % self.name

class Storage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    storage_type = db.Column(db.String(255))
    storage_brand = db.Column(db.String(255))
    storage_model = db.Column(db.String(255))
    storage_specs = db.Column(db.String(255))
    business_type = db.Column(db.String(255))
    current_storage_wattage = db.Column(db.String(255))
    cloud_storage_wattage = db.Column(db.String(255))
    in_premise_cost_storage = db.Column(db.String(255))
    cloud_cost_storage = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    def __repr__(self):
        return '<Storage %r>' % self.name


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        server_type = request.form['server_type']
        server_brand = request.form['server_brand']
        server_model = request.form['server_model']
        server_specs = request.form['server_specs']
        business_type = request.form['business_type']
        current_server_wattage = request.form['current_server_wattage']

        new_server_entry = Server(server_type=server_type,server_brand=server_brand,server_model=server_model,
                server_specs = server_specs,business_type = business_type,current_server_wattage=current_server_wattage)

        try:
            db.session.add(new_server_entry)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new stuff."

    else:
        servers= Server.query.order_by(Server.created_at).all()
        return render_template('index.html', servers=servers)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
