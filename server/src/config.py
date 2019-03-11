DBname = "newmedia"
DBuser = "newmedia"
DBpass = "maxoyed2013"
DBhost = "mariadb:3306"
# DBhost = "172.31.0.3:3306"
SQLALCHEMY_DATABASE_URI = \
 "mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4" % \
 (DBuser, DBpass, DBhost, DBname)
SECRET_KEY = "the quick brown fox jumps over the lazy dog"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
WX_APPID = "wx40b724f24eaad66d"
WX_SECRET = "ed101e56382793599a53b925b53fbf52"
