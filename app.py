from flask import Flask, request, redirect, url_for
import csv
import os

# Specify the path to the directory
directory_path = '/data_laying.csv'
directory_path2 = '/data_walking.csv'

# Define the new permissions (in octal notation)
new_permissions = 0o777  # Example: Read, Write, Execute for User, Group, and Others

# Change the permissions of the directory
os.chmod(directory_path, new_permissions)
os.chmod(directory_path2, new_permissions)


app = Flask(__name__)
i = 0
j = 0

@app.route('/')
def home():
    a = request.args.get("Activity")
    if a == "Laying":
        return redirect(url_for('add_data_laying'))
    elif a == "Walking":
        return redirect(url_for('add_data_walking'))
    else:
        return "Error in Activity selection"

@app.route('/Laying')
def add_data_laying():
    global i
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

    with open("/data_laying.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, gra_x, gra_y, gra_z, a])
        i += 1
        return "Laying Data added in dataset: " + str(i)

@app.route('/Walking')
def add_data_walking():
    global j
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

    with open("/data_walking.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, gra_x, gra_y, gra_z, a])
        j += 1
        return "Walking Data added in dataset: " + str(j)

if __name__ == '__main__':
    app.run(debug=True)
