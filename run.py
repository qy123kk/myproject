from app import create_app
from datetime import datetime

app = create_app()

@app.context_processor
def inject_now():
    """在模板中注入当前时间"""
    return {'now': datetime.utcnow()}

if __name__ == '__main__':
    app.run(debug=True) 