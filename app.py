from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from slack_sdk import WebClient
import os
import fileinput
import subprocess
from healper import slackNotification
app = Flask(__name__)
#socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update", methods=["POST"])
def update():
    apihub = request.form.get("api_path")
    cxr = request.form.get("cxr_path")
    tkt = request.form.get("ticketno")
    installation_mode = request.form.get('installation_mode')
    print(apihub, cxr, tkt, installation_mode)
    
    if installation_mode =='online':
        slackNotification('upgradation starting for ticker number : '+tkt)
        print('online mode')
        if subprocess.run(['bash', 'pull-image.sh']).returncode == 0:
            print("pulling dockers completed")
            subprocess.run(['bash', './misc/psqlupgrade.sh'])
            slackNotification('pulling dockers completed')
            #subprocess.run(['python3', 'notification.py', 'pulling dockers completed'])
        else:
            slackNotification('docker pull failed and stopped')
            # subprocess.run(['python3', 'notification.py',
            #             'docker pull failed and stopped'])
            exit()
    else:
        print('offline mode')
    replacepath(apihub, cxr)
    #subprocess.run(['python3', 'deploy.py'])

    socketio.start_background_task(target=deploy_task)
    return "Update request received."

            
@socketio.on('connect', namespace='/deploy')
def deploy_connect():
    print('Client connected to /deploy')


def deploy_task():
    with open("output.log", "w") as log:
        process = subprocess.Popen(
            ['bash', 'full-deploy.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in process.stdout:
            print("Sending line:", line.strip())  # Add this line
            log.write(line)
            socketio.emit("deploy_output", {"message": line.strip()})

        return_code = process.wait()
        if return_code == 0:
            socketio.emit("deploy_output", {
                          "status": "success", "message": "Deployment completed."})
        else:
            socketio.emit("deploy_output", {
                          "status": "failure", "message": "Deployment failed."})


def replacepath(apihub, cxr):
    apienv = f"'{apihub.strip()}/apihub.env'"
    psqlenv = f"'{apihub.strip()}/psql.env'"
    cxrenv = f"'{cxr.strip()}/cxr.env'"

    apiyml = f"'{apihub.strip()}/apihub.yml'"
    cxryml = f"'{cxr.strip()}/cxr.yml'"
    workeryml = f"'{cxr.strip()}/workers.yml'"

    file_path = '/qureupdate/misc/var.py'
    replacement_values = {
        'apienv': apienv,
        'psqlenv': psqlenv,
        'cxrenv': cxrenv,
        'apiyml': apiyml,
        'cxryml': cxryml,
        'workeryml': workeryml,
    }
# Loop through the file and replace the values
    for line in fileinput.input(file_path, inplace=True):
        for key, value in replacement_values.items():
            if key in line:
                line = f'{key}={value}\n'
                break
        print(line, end='')
        

if __name__ == "__main__":
    socketio.run(app)
