import json
import os
from datetime import datetime

# ---- CONSTANTS ---- #
DATA_FILE = "tasks.json"

class TaskManager:
    """Manages tasks stored in a JSON file."""
    
    def __init__(self):
        self.tasks = []
        self.load_tasks()
        
    def load_tasks(self):
        """Load tasks from JSON."""
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    self.tasks = json.load(f)
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
            
    def save_tasks(self):
        """Save tasks to JSON."""
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.tasks, f, indent=4)
        except Exception as e:
            print(f"Error saving tasks: {e}")
            
    def add_task(self, title, priority, due_date=""):
        """Add a new task."""
        new_id = 1
        if len(self.tasks) > 0:
            new_id = max(t["id"] for t in self.tasks) + 1
            
        task = {
            "id": new_id,
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        return new_id
        
    def get_all_tasks(self, filter_priority=None, filter_status=None):
        """Get tasks with optional filtering."""
        res = self.tasks
        if filter_priority:
            res = [t for t in res if t["priority"] == filter_priority]
        if filter_status is not None:
            res = [t for t in res if t["completed"] == filter_status]
        return res
        
    def mark_completed(self, task_id):
        """Mark a task as completed."""
        for t in self.tasks:
            if t["id"] == task_id:
                t["completed"] = True
                self.save_tasks()
                return True
        return False
        
    def delete_task(self, task_id):
        """Delete a task."""
        for t in self.tasks:
            if t["id"] == task_id:
                self.tasks.remove(t)
                self.save_tasks()
                return True
        return False
