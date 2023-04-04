import shutil
from var import apienv,psqlenv,cxrenv

def file_update(filePath, env):
    with open(filePath, 'w') as f:
        for tag_name, tag_value in env.items():
            f.write(f"{tag_name}={tag_value}\n")
def show_env(env):
    for tag_name, tag_value in env.items():
            print('{} : {}'.format(tag_name, tag_value))
def read_file(filePath):
    memo = {}
    with open(filePath, 'r') as f:
        for line in f:
            if "=" in line:
                tag_name, tag_value = line.strip().split('=')
                memo[tag_name] = tag_value
    return memo
def updateSomeFixedValues(dictValues):
    if "SETUP_CXR_DB" in dictValues.keys():
        tag_dict_new['SETUP_CXR_DB']=False
    if 'SETUP_APIHUB_DB' in dictValues.keys():
        tag_dict_new['SETUP_APIHUB_DB']=False
    if "CXR_API_HOST_URL" in dictValues.keys():
        tag_dict_new['CXR_API_HOST_URL']='http://172.17.0.1:3000/'
    if 'APIHUB_URL' in dictValues.keys():
        tag_dict_new['APIHUB_URL']='http://172.17.0.1:2000/'
    if 'SERVER_ENDPOINT' in dictValues.keys():
        tag_dict_new['SERVER_ENDPOINT']='http://0.0.0.0:2000/'
    if 'FS_SERVER_PATH' in dictValues.keys():
        tag_dict_new['FS_SERVER_PATH']='http://172.17.0.1:2000/static/'
    if "CXR_API_DATABASE_PASSWORD" in dictValues.keys():
        tag_dict_new['CXR_API_DATABASE_PASSWORD']="4a5Lry5LYGRj"
    if "CXR_API_DATABASE_NAME" in dictValues.keys():
        tag_dict_new['CXR_API_DATABASE_NAME']="cxr_api"
    if "AUTH_DATABASE_PASSWORD" in dictValues.keys():
        tag_dict_new['AUTH_DATABASE_PASSWORD']="4a5Lry5LYGRj"
    if "QDB_PASSWORD" in dictValues.keys():
        tag_dict_new['QDB_PASSWORD']="4a5Lry5LYGRj"
    return tag_dict_new

def updateNewFile(tag_dict_new,tag_dict_old,valuesInNew):
    for tag_name, tag_value in tag_dict_new.items():
        try:
            if tag_dict_old[tag_name]!= tag_value:
                valuesToBeReplaced.append(tag_name)
                tag_dict_new[tag_name] = tag_dict_old[tag_name]
        except:
            valuesInNew.append(tag_name)
    tag_dict_new=updateSomeFixedValues(tag_dict_new)
    return tag_dict_new,valuesInNew
oldpath=[apienv,cxrenv]
#oldpath=[apienv,psqlenv,cxrenv]
#oldpath=['/home/qure/qure/apihub/apihub.env','/home/qure/qure/apihub/psql.env','/home/qure/qure/cxr/cxr.env']
#oldpath=['/qure/workspace/QxrQbox/apihub/apihub.env','/qure/workspace/QxrQbox/apihub/psql.env','/qure/workspace/QxrQbox/cxr/cxr.env']
#newpath=['/qureupdate/newupdate/apihub/apihub.env','/qureupdate/newupdate/apihub/psql.env','/qureupdate/newupdate/cxr/cxr.env']
newpath=['/qureupdate/apihub/apihub.env','/qureupdate/cxr/cxr.env']
# newpath=['/qureupdate/apihub/apihub.env','/qureupdate/apihub/psql.env','/qureupdate/cxr/cxr.env']
for i in range(len(newpath)):
    tag_dict_old=read_file(oldpath[i])
    tag_dict_new=read_file(newpath[i])
    valuesToBeReplaced=[]
    valuesInOld=[]
    valuesInNew=[]
    tag_dict_new,valuesInNew= updateNewFile(tag_dict_new,tag_dict_old,valuesInNew)
    # print("new env will look like this\n\n")
    # show_env(tag_dict_new)
    # print('\n\nthese tags are transfered from', oldpath[i] ,'to', newpath[i],'\n',*valuesToBeReplaced)
    # print('these are new',valuesInNew)
    # change=input("do you want to make any changes y/n\n")
    # tagName=''
    # more=''
    # while change=='y'and tagName!='exit' and more!='n':
    #     while True:
    #         tagName=input('enter the tag which you want to change or `exit` if you dont want to change anything')
    #         print(tagName=='exit')
    #         if tagName=='exit':
    #             break
    #         elif tagName in tag_dict_new.keys():
    #             tagValue=input("enter tag value ")
    #             tag_dict_new[tagName]=tagValue
    #             more=input("do you want to make more changes y/n ")
    #             if more=='y':
    #                 continue
    #             elif more=='n':
    #                 break
    #             print('something diff selected, pelase select correct option')
    #             continue
    #         print('wrong tag given')
    #         continue
    # else:
    #     change=input("asking 1 more time, you want to make any changes y/n\n")
    # print("final env will look like this\n\n")
    show_env(tag_dict_new)
    file_update(newpath[i], tag_dict_new)
    print("changed", newpath[i])