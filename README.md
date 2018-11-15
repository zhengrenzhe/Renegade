# Renegade

A telegram bot that auto upload received file to cdn.
the bot is running on [heroku](https://www.heroku.com/) platform, it is a PaaS service, by default you don't have to spend money.
 

## how to deploy?

* step 1: sign in or sing up your [Heroku](https://dashboard.heroku.com/) Account.
* step 2: click the button [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/zhengrenzhe/Renegade) to deploy bot App to your heroku account, after deployed, the App default is shutdown status.
* step 3: in App **Settings tab** - **Config Vars**, click **Reveal Config Vars**, add three Config Vars:
    * **BOT_TOKEN** : the telegram bot token, detail see: [BotFather](https://core.telegram.org/bots#6-botfather)
    * **DB_NAME** : the **MONGODB_URI** last few strings after '/'
    * **UPLOAD_SERVICE** : yaml format, declare your upload services, example
        ```yaml
        services:
        - name: # upload service name, unique
          mode: upyun # upyun mode, support upyun or qiniu 
          domain: # your cdn domain url
          auth:
            service_name: # service name
            username: # amdin username
            password: # admin password
        
        - name: # upload service name, unique
          mode: # upyun mode, support upyun or qiniu
          domain: # your cdn domain url
          auth:
            bucket_name: # bucket name
            access_key: # access_key 
            secret_key: # secret_key
        ```

* step 4: in App **Resource tab**, open the Free Dyno
* step 5: in **More** - **View logs**, if you seen `app[worker.1]: bot is running...`, it indicate the bot App is working! 🥳
* step 6: in your telegram app, chosen your telegram bot, send `/start` command to start.
