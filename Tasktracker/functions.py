import typer
import json

app = typer.Typer() # Criação da interface CLI

task_list = {}
task_list_file = "tasks.json"


def load_tasks(): # Função para carregar as tarefas do o arquivo JSON
    try:
        with open(task_list_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {} # Se ele nao achar nada, vai voltar um dicionario vazio
    
def save_tasks(tasks): # Função para salvar as tarefas no arquivo JSON
    with open (task_list_file, "w") as file:
        json.dump(tasks, file, indent=4) # Aqui ele vai gravar no arquivo as tarefas e fazer uma formatação


@app.command()
def add(task:str):
    task_id = len(task_list) + 1 # i preferred to use a simple way to set the task ID to make the code more optimized, but I could use the UUID library 
    task_list[task_id] = {'name_task': task, 'status': 'no-to-do'}
    save_tasks(task_list)
    typer.echo(f'{task} has added, with the id = {task_id}')

if __name__ == "__main__":
    app()
