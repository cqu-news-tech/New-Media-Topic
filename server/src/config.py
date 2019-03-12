DBname = "your_application_database"
DBuser = "your_application_user"
DBpass = "your_application_password"
DBhost = "mariadb:3306"
SQLALCHEMY_DATABASE_URI = \
 "mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4" % \
 (DBuser, DBpass, DBhost, DBname)
SECRET_KEY = "the quick brown fox jumps over the lazy dog"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
WX_APPID = "your_appid"
WX_SECRET = "your_appsecret"
