class Task:
    def __init__(self, description, priority="normal"):
        self.description = description
        self.priority = priority
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description} ({self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, priority="normal"):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Задача добавлена: {description}")
    
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
            return
    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.mark_completed()
            print(f"Задача выполнена: {task.description}")
        else:
            print("Неверный номер задачи")
        
        print("\n--- Список задач ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    
    def show_pending_tasks(self):
        pending = [task for task in self.tasks if not task.completed]
        if not pending:
            print("Нет невыполненных задач")
            return
        
        print("\n--- Невыполненные задачи ---")
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task}")

def main():
    print("Добро пожаловать в менеджер задач!")
    
if __name__ == "__main__":
    main()