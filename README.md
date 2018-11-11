# Renegade

A telegram bot that auto upload received file to cdn

## Install & Running

```shell
git clone git@github.com:zhengrenzhe/Renegade.git
cd Renegade

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

cp config.tmpl.yaml config.yaml

# then edit config.yaml

python bot.py
```

## Config

```yaml
bot:
  debug: #true or false, default if false
  token: # bot token

services:
  - name: # service name, any string, unique
    mode: upyun # support upyun, qiniu
    domain: # cdn domain
    auth:
      service_name: # upyun service name
      username: # service username
      password: # service password

  - name: # service name, any string, unique
    mode: qiniu # support upyun, qiniu
    domain: # cdn domain
    auth:
      bucket_name: # qiniu bucket_name
      access_key: # qiniu access_key
      secret_key: # qiniu secret_key
```
