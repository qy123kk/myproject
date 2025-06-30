# 任务管理系统

一个基于Flask框架的任务管理Web应用，提供用户注册登录、任务创建、编辑、删除和状态管理等功能。

## 功能特点

- 用户认证系统
  - 注册、登录、登出
  - 密码安全存储（哈希加密）
- 任务管理
  - 创建、编辑、删除任务
  - 设置任务截止日期
  - 标记任务完成状态
  - 过滤查看不同状态的任务
- 响应式设计
  - 适配不同尺寸的设备屏幕
- RESTful API
  - 提供API接口获取任务数据

## 技术栈

- 后端：Flask框架
- 数据库：SQLite，SQLAlchemy ORM
- 前端：原生HTML/CSS/JavaScript
- 用户认证：Flask-Login
- 表单处理：Flask-WTF

## 项目结构

```
resume_project/
  ├── app/                  # 应用主目录
  │    ├── __init__.py      # 应用初始化
  │    ├── models.py        # 数据库模型
  │    ├── routes.py        # 路由和视图函数
  │    ├── forms.py         # 表单类
  │    ├── static/          # 静态文件
  │    └── templates/       # HTML模板
  ├── config.py             # 配置文件
  ├── run.py                # 应用入口
  └── requirements.txt      # 项目依赖
```

## 安装与运行

1. 克隆项目到本地

```bash
git clone <repository-url>
cd resume_project
```

2. 创建并激活虚拟环境（推荐）

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

3. 安装依赖

```bash
pip install -r requirements.txt
```

4. 运行应用

```bash
python run.py
```

5. 在浏览器中访问 http://127.0.0.1:5000

## 项目截图

（项目截图将在实际部署后补充）

## 未来计划

- 添加任务分类/标签功能
- 实现任务提醒系统
- 支持多语言
- 添加任务统计和分析功能

## 贡献指南

1. Fork该项目
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个Pull Request

## 许可证

此项目采用MIT许可证 - 详见LICENSE文件 