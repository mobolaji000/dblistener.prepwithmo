import os


import traceback
from app.aws import AWSInstance
awsInstance = AWSInstance()
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class Config(object):
    try:
        if os.environ['DEPLOY_REGION'] == 'local':

            logger.debug("Environment is local")

            os.environ["url_to_start_reminder"] = "http://127.0.0.1:5003/"
            flask_secret_key = os.environ.get('flask_secret_key')
            SECRET_KEY = os.environ.get('flask_secret_key')
            dbUserName = os.environ.get('dbUserNameLocal')
            dbPassword = os.environ.get('dbPasswordLocal')
            SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'+str(dbUserName)+':'+str(dbPassword)+'@host/mobolajioo'
            SQLALCHEMY_TRACK_MODIFICATIONS = False
            #SQLALCHEMY_ECHO = True


            os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
            os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


            os.environ["psycopg_url"] = "host"
            os.environ["psycopg_db"] = "mobolajioo"
            os.environ["psycopg_port"] = "5432"



        elif os.environ['DEPLOY_REGION'] == 'dev':

            os.environ["url_to_start_reminder"] = "159.223.174.169/"
            flask_secret_key = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            SECRET_KEY = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            dbUserName = awsInstance.get_secret("do_db_cred", "dev_username")
            dbPassword = awsInstance.get_secret("do_db_cred", "dev_password")
            SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'+str(dbUserName)+':'+str(dbPassword)+'@app-27fee962-3fa3-41cb-aecc-35d29dbd568e-do-user-9096158-0.b.db.ondigitalocean.com:25060/db'
            SQLALCHEMY_TRACK_MODIFICATIONS = False
            #SQLALCHEMY_ECHO = True##


            os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
            os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

            os.environ["psycopg_url"] = "app-27fee962-3fa3-41cb-aecc-35d29dbd568e-do-user-9096158-0.b.db.ondigitalocean.com"
            os.environ["psycopg_db"] = "db"
            os.environ["psycopg_port"] = "25060"


        elif os.environ['DEPLOY_REGION'] == 'prod':

            logger.debug("Environment is prod")

            os.environ["url_to_start_reminder"] = "https://messages.prepwithmo.com/"
            flask_secret_key = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            SECRET_KEY = awsInstance.get_secret("vensti_admin", "flask_secret_key")
            dbUserName = awsInstance.get_secret("do_db_cred", "username")
            dbPassword = awsInstance.get_secret("do_db_cred", "password")
            SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' + str(dbUserName) + ':' + str(dbPassword) + '@yet-another-backup-do-user-9096158-0.b.db.ondigitalocean.com:25060/db'
            SQLALCHEMY_TRACK_MODIFICATIONS = False
            #SQLALCHEMY_ECHO = True


            os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
            os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

            #os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

            os.environ["psycopg_url"] = "yet-another-backup-do-user-9096158-0.b.db.ondigitalocean.com"
            os.environ["psycopg_db"] = "db"
            os.environ["psycopg_port"] = "25060"




    except Exception as e:
        print("error in initialization")
        print(e)
        traceback.print_exc()
        #trigger11

