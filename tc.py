import json
import argparse
import os

parser = argparse.ArgumentParser(
    description='Программа для ведения списка дел.'
    )

parser.add_argument('-a', '--add', help='Добавьте новую задачу.', required = False)
parser.add_argument('-u', '--update', help='Обновите задачу.', required = False)
parser.add_argument('-m', '--mark', help = 'Отметьте задачу выполненной(done) или в прогрессе(in progress).', required = False)
parser.add_argument('-d', '--delete', help = 'Удалите задачу.', required = False)
parser.add_argument( '-l', '--list', help = 'Напишите --list и её статус(all, todo, done, in progress)', required = False)
parser.add_argument('-p', '--pick', help='Выберите нужную задачу.', required = False)


args = parser.parse_args()

# print(f'Добавлено: {args.add if args.add else 'Нет задач'}.')
# print(f'Обновлено: {args.update if args.update else 'Нет задач для обновления'}.')
# print(f'Удалено: {args.delete if args.delete else 'Нет задач для удаления'}.')
# print(f'Отмечено выполненным: {args.mark if args.mark else 'Нет задач'}.')
# print(f'Лист задач: {args.list if args.list else 'Список пуст'}')

work_file = 'tasklist.json'



def adding_task(taask):
    tasks = taask
    if not os.path.exists(work_file):
        tasks = [
            {
                'id': 1,
                'description': taask,
                'status': 'todo'               
            }
        ]
        with open(work_file, 'w') as file:
            json.dump(tasks, file, indent=4)

    else:
        with open(work_file, 'r') as file:
            data = json.load(file)
            last_id = max(item['id'] for item in data) if data else 0
            new_task = {
                'id': last_id + 1,
                'description': taask,
                'status': 'todo'
            }
            data.append(new_task)

        with open(work_file, 'w') as file:
            json.dump(data, file, indent=4)



def delete(id):
    with open(work_file, 'r') as file:
        data = json.load(file)

        


def show_list(status):
    with open(work_file, 'r') as file:
        data = json.load(file)
    if status == 'all':
        print(json.dumps(data, indent = 4))
    elif status == 'todo':
        todo_tasks = [task for task in data if task.get('status') == 'todo']
        print(json.dumps(todo_tasks, indent = 4))
    elif status == 'in progress':
        in_progress_tasks = [task for task in data if task.get('status') == 'in progress']
        print(json.dumps(in_progress_tasks, indent = 4))
    elif status == 'done':
        done_tasks = [task for task in data if task.get('status') == 'done']
        print(json.dumps(done_tasks, indent = 4))
    else:
        print('Где-то ошибка ;)')
        exit()


    
if args.add:
    print(f'Добавлено: {args.add if args.add else 'Нет задач'}.')
    adding_task(args.add)
elif args.list:
    show_list(args.list)
elif args.delete:
    print(f'Элемент удалён {args.delete}')
    delete(int(args.delete))
else:
    exit()







     



            

        