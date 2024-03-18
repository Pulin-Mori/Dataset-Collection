from flask import Flask,request,redirect,url_for
import csv

app = Flask(__name__)
i=0
j=0

@app.route('/',method=['GET','POST'])
def  home():
    a = request.args.get("Activity")
    if a=="Laying":
        return redirect(url_for('Laying'))
    elif a=="Walking":
        return redirect(url_for('Laying'))
    else:
        return "Error in Activity selection"

@app.route('/Laying')
def add_data_laying():
    acc_x = request.args.get('Acc_x')
    acc_y = request.args.get('Acc_y')
    acc_z = request.args.get('Acc_z')
    gyr_x = request.args.get('Gyr_x')
    gyr_y = request.args.get('Gyr_y')
    gyr_z = request.args.get('Gyr_z')
    gra_x = request.args.get('Gra_x')
    gra_y = request.args.get('Gra_y')
    gra_z = request.args.get('Gra_z')
    a = "Laying"

    with open("data_laying.csv",'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z,gra_x,gra_y,gra_z,a])
        i+=1
        return "Laying Data added in dataset:"+i

@app.route('/Walking')
def add_data_walking():
    acc_x = request.args.get('Acc_x')
    acc_y = request.args.get('Acc_y')
    acc_z = request.args.get('Acc_z')
    gyr_x = request.args.get('Gyr_x')
    gyr_y = request.args.get('Gyr_y')
    gyr_z = request.args.get('Gyr_z')
    gra_x = request.args.get('Gra_x')
    gra_y = request.args.get('Gra_y')
    gra_z = request.args.get('Gra_z')
    a = "Walking"

    with open("data_walking.csv",'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z,gra_x,gra_y,gra_z,a])
        j+=1
        return "Walking Data added in dataset:"+j
    
if __name__ == '__main__':
    app.run(debug=True)