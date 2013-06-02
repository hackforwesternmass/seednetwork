seednetwork
===========
The distributed seed library for the Hilltown Seed Saving Network

This is a Django site. To make it easier to deploy without changing settings.py, use the following environment variables

```shell
SEEDNETWORK_SECRETKEY
SEEDNETWORK_EMAIL_HOST
SEEDNETWORK_EMAIL_PORT
SEEDNETWORK_EMAIL_HOST_USER
SEEDNETWORK_EMAIL_HOST_PASSWORD
SEEDNETWORK_DEFAULT_FROM_EMAIL
```

This site uses dj_database_url for DB configuration, so set DATABASE_URL using its syntax. A sample mysql URL is

```shell
export DATABASE_URL='mysql://user:pwd@host:port/database'
```

Heroku Deploy Instructions
--------------------------
1. Follow the normal Heroku Django procedure
2. Set the environment

```shell
heroku config:set DATABASE_URL='mysql://user:pwd@host:port/database'
heroku config:set SEEDNETWORK_SECRETKEY='xxxxxxxxxxxxxxxxxxxxxxxxx'
heroku config:set SEEDNETWORK_EMAIL_HOST='smtp.example.com'
```


About the Hilltown Seed Saving Network 
--------------------------------------
The Hilltown Seed Saving Network of western Massachusetts is a loosely organized group working to educate ourselves and our neighbors about seed saving and currently creating a virtual local seed bank, sharing information about what seeds we have in our own collections and how best to grow them. We are from Cummington, Chesterfield, Plainfield, Worthington, Windsor, Goshen, Ashfield and surrounding towns in the region and meet monthly in Cummington. All are welcome!
