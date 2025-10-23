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
    
    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.mark_completed()
            print(f"Задача выполнена: {task.description}")
        else:
            print("Неверный номер задачи")
    
    def show_statistics(self):  # ← ДОБАВЛЕННЫЙ МЕТОД
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed
        
        print(f"\n--- Статистика ---")
        print(f"Всего задач: {total}")
        print(f"Выполнено: {completed}")
        print(f"Осталось: {pending}")

def main():
    manager = TaskManager()
    while True:
        print("\n=== Менеджер задач ===")
        print("1. Показать все задачи")
        print("2. Показать невыполненные задачи")
        print("3. Добавить задачу")
        print("4. Выполнить задачу")
        print("5. Показать статистику")  # ← ДОБАВЛЕН ПУНКТ
        print("6. Выход")  # ← ИЗМЕНЕН НОМЕР
        
        choice = input("Выберите действие: ")
        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            manager.show_pending_tasks()
        elif choice == "3":
            description = input("Введите описание задачи: ")
            manager.add_task(description)
        elif choice == "4":
            manager.show_pending_tasks()
            if manager.tasks:
                try:
                    task_num = int(input("Введите номер задачи для выполнения: "))
                    manager.complete_task(task_num)
                except ValueError:
                    print("Введите корректный номер")
        elif choice == "5":  # ← ДОБАВЛЕН ВАРИАНТ
            manager.show_statistics()
        elif choice == "6":  # ← ИЗМЕНЕН НОМЕР
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()