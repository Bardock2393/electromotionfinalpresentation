import json
import time
from flask import Flask, render_template, make_response
from urllib.request import urlopen

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    url = "https://sbucket2393.s3.amazonaws.com/mykey"
    response = urlopen(url)
    variable = json.loads(response.read())
     
      

    voltage =  variable['voltage']
    current = variable['current']
    power =  variable['power']
    motor_speed=  variable['motor_speed']
    controller_temperature = variable['controller_temperature']
    motor_temperature = variable['motor_temperature']
    throttle = variable['throttle']
    soc = variable['soc']
    distance_travelled = variable['distancetravelled']
    gearstatus = variable['gearstatus']
    vehicledirection = variable['vehicledirection']
    fault = variable['fault']
    cdstate = variable['cdstate']
    x = time.time() + 19800

    

    

    data = [x * 1000,voltage,current,power,motor_speed,controller_temperature,motor_temperature,throttle,soc,distance_travelled,gearstatus,vehicledirection,fault,cdstate]

   
    time.sleep(1)
  
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
