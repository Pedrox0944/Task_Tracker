import typer
import json
import os

app = typer.Typer() # Criação da interface CLI

list = {}

@app.command()
def add(task:str):
    task_id = len(list) + 1 # i preferred to use a simple way to set the task ID to make the code more optimized, but I could use the UUID library 
    list[task_id] = {'name_task': task, 'status': 'no-to-do'}
    typer.echo(f'{task} has added')


