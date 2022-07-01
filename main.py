from flask import Flask, render_template, request, redirect, url_for
import pyodbc as sql
from models import MedicalList,MedicineRoute,MedicineType

server = sql.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-A9SV17P\SQLEXPRESS;"
    "Database=MasterMedicosFK;"
    "Trusted_Connection=yes;"
)

cursor = server.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/admin')
def index():
    return render_template('medicine_list.html', data=MedicalList(server).read())


@app.route("/medicine/create",methods=["GET","POST"])
def medicine_create():
    if request.method == "POST":
        data = (request.form['GenericName'], request.form['MedicineType'], request.form['MarketName'], request.form["Route"], request.form['Potency'], request.form['Status'])
        MedicalList(server).insert(data)
        return redirect(url_for('index'))
    return render_template('medicine_create.html')

@app.route('/medicine/edit/<id>', methods=['GET', 'POST'])
def medicine_edit(id):
    if request.method == 'POST':
        data = (request.form['GenericName'], request.form['MedicineType'], request.form['MarketName'],request.form["Route"], request.form['Potency'], request.form['Status'])
        MedicalList(server).update(data, id)
        return redirect(url_for('index'))
    print(MedicalList(server).fetch(id))
    return render_template('medicine_edit.html', data=MedicalList(server).fetch(id))

@app.route('/medicine/delete/<id>', methods=['GET', 'POST'])
def medicine_delete(id):
    if request.method == 'GET':
        MedicalList(server).delete(id)
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/medicine-route')
def route():
    return render_template('routes.html',data=MedicineRoute(server).read())

@app.route('/custom-query',methods=['GET','POST'])
def custom_query():
    if request.method == 'POST':
        try:
            query = request.form['query']
            data = MedicalList(server).customQuery(query)[1]
            columns = MedicalList(server).customQuery(query)[0]
            return render_template('result.html', data=data,columns=columns)
        except sql.ProgrammingError:
            return render_template('result.html')
    return render_template('custom_query.html')


@app.route('/medicine-route/create', methods=['GET', 'POST'])
def route_create():
    if request.method == 'POST':
        data = (request.form['RouteType'], request.form['status'])
        MedicineRoute(server).insert(data)
        return redirect(url_for('route'))
    return render_template('routes_create.html')

@app.route('/medicine-route/edit/<id>', methods=['GET', 'POST'])
def route_edit(id):
    if request.method == 'POST':
        data = (request.form['RouteType'], request.form['status'])
        MedicineRoute(server).update(data, id)
        return redirect(url_for('route'))
    return render_template('routes_edit.html', data=MedicineRoute(server).fetch(id))

@app.route('/medicine-route/delete/<id>', methods=['GET', 'POST'])
def route_delete(id):
    if request.method == 'GET':
        MedicineRoute(server).delete(id)
        return redirect(url_for('route'))
    return redirect(url_for('route'))

@app.route('/medicine-type')
def medicine_type():
    return render_template('medicine_types.html',data=MedicineType(server).read())

@app.route('/medicine-type/create', methods=['GET', 'POST'])
def medicine_type_create():
    if request.method == 'POST':
        data = (request.form['MedicineName'], request.form['status'])
        MedicineType(server).insert(data)
        return redirect(url_for('medicine_type'))
    return render_template('medicine_types_create.html')

@app.route('/medicine-type/edit/<id>', methods=['GET', 'POST'])
def medicine_type_edit(id):
    if request.method == 'POST':
        data = (request.form['MedicineName'], request.form['status'])
        MedicineType(server).update(data, id)
        return redirect(url_for('medicine_type'))
    return render_template('medicine_types_edit.html', data=MedicineType(server).fetch(id))

@app.route('/medicine-type/delete/<id>', methods=['GET', 'POST'])
def medicine_type_delete(id):
    if request.method == 'GET':
        MedicineType(server).delete(id)
        return redirect(url_for('medicine_type'))
    return redirect(url_for('medicine_type'))


app.run(debug=True)

