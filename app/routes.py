from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Task
from app.forms import LoginForm, RegistrationForm, TaskForm
from datetime import datetime

# 创建蓝图
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
tasks_bp = Blueprint('tasks', __name__)

# 主蓝图路由
@main_bp.route('/')
@main_bp.route('/index')
def index():
    """首页"""
    return render_template('index.html', title='首页')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """用户仪表盘"""
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template('dashboard.html', title='仪表盘', tasks=tasks)

# 认证蓝图路由
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """用户登录"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('用户名或密码错误')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('main.dashboard')
        return redirect(next_page)
    
    return render_template('login.html', title='登录', form=form)

@auth_bp.route('/logout')
def logout():
    """用户登出"""
    logout_user()
    return redirect(url_for('main.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """用户注册"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功，请登录！')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', title='注册', form=form)

# 任务蓝图路由
@tasks_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_task():
    """创建任务"""
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            deadline=form.deadline.data,
            author=current_user
        )
        db.session.add(task)
        db.session.commit()
        flash('任务创建成功！')
        return redirect(url_for('main.dashboard'))
    
    return render_template('task_form.html', title='创建任务', form=form, is_edit=False)

@tasks_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    """编辑任务"""
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('您无权编辑此任务')
        return redirect(url_for('main.dashboard'))
    
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.deadline = form.deadline.data
        db.session.commit()
        flash('任务更新成功！')
        return redirect(url_for('main.dashboard'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.deadline.data = task.deadline
    
    return render_template('task_form.html', title='编辑任务', form=form, is_edit=True)

@tasks_bp.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    """删除任务"""
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('您无权删除此任务')
        return redirect(url_for('main.dashboard'))
    
    db.session.delete(task)
    db.session.commit()
    flash('任务已删除！')
    return redirect(url_for('main.dashboard'))

@tasks_bp.route('/toggle/<int:task_id>')
@login_required
def toggle_task(task_id):
    """切换任务完成状态"""
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('您无权修改此任务')
        return redirect(url_for('main.dashboard'))
    
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.dashboard'))

# API路由
@tasks_bp.route('/api/tasks')
@login_required
def api_get_tasks():
    """获取任务API"""
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at.isoformat(),
        'deadline': task.deadline.isoformat() if task.deadline else None
    } for task in tasks]) 