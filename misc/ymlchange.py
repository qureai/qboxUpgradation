import yaml
from var import apiyml,workeryml,cxryml
oldpath=[apiyml,cxryml,workeryml]
#oldpath=['/home/qure/qure/apihub/apihub.yml','/home/qure/qure/cxr/cxr.yml','/home/qure/qure/cxr/workers.yml']
#oldpath=['/qure/workspace/QxrQbox/apihub/apihub.yml','/qure/workspace/QxrQbox/cxr/cxr.yml','/qure/workspace/QxrQbox/cxr/workers.yml']
newpath=['/qureupdate/apihub/apihub.yml','/qureupdate/cxr/cxr.yml','/qureupdate/cxr/workers.yml']
# read the first YAML file and parse the content
for i in range(len(oldpath)):
    with open(oldpath[i], 'r') as f:
        oldData = yaml.safe_load(f)

# read the second YAML file and parse the content
    with open(newpath[i], 'r') as f:
        newData = yaml.safe_load(f)

# update the volumes in the first file with those from the second file
    newData['volumes'] = oldData['volumes']
    print(newData['volumes'])
    if 'psql-data' in newData['volumes']:
        newData['volumes'].pop('psql-data')
        newData['volumes']['psql-data1']={'external': True}
    if 'apihub_sync' not in oldData['services'].keys():
        try:
            newData['services'].pop('apihub_sync')
        except:
            pass
    if 'cxrapi_sync' not in oldData['services'].keys():
        try:
            newData['services'].pop('cxrapi_sync')
        except:
            pass
    for service_name, service_data in oldData['services'].items():
        try:
            newData['services'][service_name]['volumes'] = oldData['services'][service_name]['volumes']
            if service_name=='postgres':
                newData['services']['postgres']['volumes']=['psql-data1:/var/lib/postgresql/data']
        except:
            pass
        
# write the updated data to a new file
    with open(newpath[i], 'w') as f:
        yaml.dump(newData, f)
    print("completed", newpath[i])
    