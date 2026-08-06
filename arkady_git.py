import subprocess
import os
from pathlib import Path
from rich.table import Table

class GitManager:
    def __init__(self, repo):
        self.repo = Path(repo)
    
    def status(self):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'status'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def diff(self):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'diff'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def commit(self, msg):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'commit', '-m', msg], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def push(self):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'push'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def pull(self):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'pull'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def branch(self):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'branch'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def checkout(self, name):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'checkout', name], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def log(self, n):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'log', '-n', str(n)], capture_output=True, text=True, check=True)
            table = Table("Commit", "Author", "Date", "Message")
            for line in result.stdout.split('\n'):
                if line.startswith('commit'):
                    commit_hash = line.split()[1]
                elif line.startswith('Author:'):
                    author = line.split(': ')[1]
                elif line.startswith('Date:'):
                    date = line.split(': ')[1]
                elif line.startswith('    '):
                    message = line[4:]
                    table.add_row(commit_hash, author, date, message)
            return table
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"
    
    def init(self):
        try:
            result = subprocess.run(['git', '-C', str(self.repo), 'init'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка: {e.stderr}"