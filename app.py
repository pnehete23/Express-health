from flask import Flask, render_template, request
import requests
import json
from requests import get
import pandas as pd
import math
from panda import calculate_distances


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home_page():
    ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    print('IP Address is in first part: ',ip_address)
    return render_template('index.html')

@app.route('/submit', methods=['POST','GET'])
def signup_page():
    if request.method == 'POST':

        name = request.form.get("Name")
        phone = request.form.get("Phone")
        one = request.form.get("Question_1")
        two = request.form.get("Question_2")
        three = request.form.get("Question_3")
        four = request.form.get("Question_4")
        five = request.form.get("Question_5")
        six = request.form.get("Question_6")
        seven = request.form.get("Question_7")
        eight = request.form.get("Question_8")
        nine = request.form.get("Question_9")

    List = [name, phone, one, two, three, four, five, six, seven, eight, nine]

    contact = 0
    if nine == 'yes' or nine == 'Yes':
        contact = 1

    score = 0
    for i in range(len(List)):
        if List[i] == 'YES' or List[i]=='Yes' or List[i] == 'yes':
            score += 1

    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

    print('IP Address in second part: ', ip)


    def ipaddressfinder(ip_address):
        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result = json.loads(result)

        print(result)
        return result

    location = ipaddressfinder(ip)
    
    lat = location['latitude']
    lng = location['longitude']

    data = calculate_distances(lat, lng, score, contact)

    return render_template('submit.html', interpretation = data[0], items = data[1], words = data[2])


if __name__=='__main__':
    app.run(debug=True)
