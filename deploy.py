import os
import subprocess

# Login to Docker registry
subprocess.run(['docker', 'login', '-u', 'ajayrajqure', '-p', 'zpsbS8BR2Q'])

# Pull Docker images
if subprocess.run(['bash', 'pull-image.sh']).returncode == 0:
    print("pulling dockers completed")
    subprocess.run(['python3', 'notification.py', 'pulling dockers completed'])
else:
    subprocess.run(['python3', 'notification.py',
                   'docker pull failed and stopped'])
    exit()

# Upgrade PostgreSQL database
os.chdir('/qureupdate/misc')
subprocess.run(['bash', 'psqlupgrade.sh'])

# Backup PostgreSQL databases
print("taking backups of cxr and apihub")
subprocess.run(['bash', 'pgbackup.sh'])

# Change YAML and ENV files
print("changing yml and env files")
os.chdir('/qureupdate/misc')
subprocess.run(['python3', 'envchange.py'])
subprocess.run(['python3', 'ymlchange.py'])

# Remove previous Docker containers
print("removing previous dockers")
ps_output = subprocess.run(['docker', 'ps', '-a'], stdout=subprocess.PIPE)
for container_id in ps_output.stdout.decode().split('\n')[1:-1]:
    subprocess.run(['docker', 'rm', '-f', container_id.split()[0]])

# Deploy Docker containers
os.chdir('/qureupdate')
print("deploying containers")
subprocess.run(['bash', 'deploy-cxr.sh'])
subprocess.run(['bash', 'deploy-gateway.sh'])
subprocess.run(['bash', 'deploy-monitoring.sh'])

# Restore PostgreSQL databases
print("restoring database")
os.chdir('/qureupdate/misc')
subprocess.run(['bash', 'pgrestore.sh'])

os.chdir('/qureupdate')
subprocess.run(['bash', 'migrations-commit.sh'])

subprocess.run(['docker', 'logout'])

# Send notification about installation completion
os.chdir('/qureupdate')
subprocess.run(['python3', 'notification.py', 'installation completed'])
