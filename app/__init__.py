from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# 初始化扩展
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # 设置登录视图的端点

def create_app(config_class=Config):
    # 创建应用实例
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    
    # 注册蓝图
    from app.routes import main_bp, auth_bp, tasks_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app 