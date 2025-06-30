import os
from dotenv import load_dotenv

# 加载.env文件中的环境变量（如果存在）
load_dotenv()

class Config:
    # 密钥配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-resume-project'
    
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 