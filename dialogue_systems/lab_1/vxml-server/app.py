from flask import Flask, render_template, make_response, Response
app = Flask(__name__)

temp = '13'

@app.route('/weather')
def hello():
    vxml = render_template('weather.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1')
def lab1():
    vxml = render_template('lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route("/metal.wav")
def streamwav():
    def generate():
        with open("templates/metal.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


@app.route('/delayed_flights')
def delayed_flights():
    vxml = render_template('delayed_flights.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/flight_booking')
def flight_booking():
    vxml = render_template('flight_booking.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return 
    
@app.route('/life_advice')
def life_advice():
    vxml = render_template('life_advice.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response