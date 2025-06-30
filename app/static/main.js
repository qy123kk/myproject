// 等待DOM加载完成
document.addEventListener('DOMContentLoaded', function() {
    // 处理闪现消息的自动消失
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 500);
        }, 3000);
        message.style.transition = 'opacity 0.5s';
    });

    // 处理任务切换完成状态的交互
    const taskCheckboxes = document.querySelectorAll('.task-checkbox');
    taskCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskId = this.getAttribute('data-task-id');
            window.location.href = `/tasks/toggle/${taskId}`;
        });
    });

    // 处理确认删除对话框
    const deleteButtons = document.querySelectorAll('.delete-task-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('确定要删除这个任务吗？此操作不可撤销。')) {
                e.preventDefault();
            }
        });
    });

    // 初始化日期选择器（如果有）
    const dateTimeInputs = document.querySelectorAll('input[type="datetime-local"]');
    if (dateTimeInputs.length > 0) {
        dateTimeInputs.forEach(input => {
            // 如果使用第三方日期选择器库，这里可以进行初始化
            console.log('日期输入字段已初始化');
        });
    }

    // 任务描述展开/收起功能
    const taskDescriptionToggles = document.querySelectorAll('.task-description-toggle');
    taskDescriptionToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const description = this.nextElementSibling;
            const isExpanded = description.style.display !== 'none';
            
            if (isExpanded) {
                description.style.display = 'none';
                this.textContent = '显示详情';
            } else {
                description.style.display = 'block';
                this.textContent = '隐藏详情';
            }
        });
    });

    // 任务过滤功能
    const filterSelect = document.getElementById('task-filter');
    if (filterSelect) {
        filterSelect.addEventListener('change', function() {
            const taskItems = document.querySelectorAll('.task-item');
            const filterValue = this.value;
            
            taskItems.forEach(item => {
                if (filterValue === 'all') {
                    item.style.display = 'flex';
                } else if (filterValue === 'completed' && item.classList.contains('completed')) {
                    item.style.display = 'flex';
                } else if (filterValue === 'active' && !item.classList.contains('completed')) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }

    // 检查和标记过期任务
    function checkOverdueTasks() {
        const now = new Date();
        const taskDeadlines = document.querySelectorAll('[data-deadline]');
        
        taskDeadlines.forEach(element => {
            const deadlineStr = element.getAttribute('data-deadline');
            if (deadlineStr) {
                const deadline = new Date(deadlineStr);
                const taskItem = element.closest('.task-item');
                
                if (now > deadline && !taskItem.classList.contains('completed')) {
                    taskItem.classList.add('overdue');
                    
                    // 如果有过期标签，确保它存在
                    if (!element.querySelector('.overdue-badge')) {
                        const badge = document.createElement('span');
                        badge.className = 'overdue-badge';
                        badge.textContent = '已过期';
                        badge.style.color = 'var(--danger-color)';
                        badge.style.fontWeight = 'bold';
                        badge.style.marginLeft = '10px';
                        element.appendChild(badge);
                    }
                }
            }
        });
    }
    
    // 执行过期检查
    checkOverdueTasks();
}); 