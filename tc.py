import json
import argparse
import os

parser = argparse.ArgumentParser(
    description = 'Программа для ведения списка дел.',
    epilog = 'Спасибо за использование этого скрипта!'
    )

parser.add_argument('-a', '--add', help='Добавьте новую задачу.', required = False)
parser.add_argument('-u', '--update', help='Обновите задачу.', required = False)
parser.add_argument('-m', '--mark', help = 'Отметьте задачу выполненной(done) или в прогрессе(in-progress).', required = False)
parser.add_argument('-d', '--delete', help = 'Удалите задачу.', required = False)
parser.add_argument( '-l', '--list', help = 'Напишите --list и её статус(all, todo, done, in progress)', required = False)

args = parser.parse_args()

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
            json.dump(tasks, file, indent = 4)

    else:

        with open(work_file, 'r') as file:
            data = json.load(file)
            last_id = max(item['id'] for item in data)
            new_task = {
                'id': last_id + 1,
                'description': taask,
                'status': 'todo'
            }
            data.append(new_task)

        with open(work_file, 'w') as file:
            json.dump(data, file, indent=4)



def delete_id(choosed_id):

    with open(work_file, 'r') as file:
        data = json.load(file)

    data = [item for item in data if item["id"] != choosed_id]

    with open(work_file, 'w') as file:
        json.dump(data, file, indent = 4)



def update_id(choosed_id, text):

    with open(work_file, 'r') as file:
        data = json.load(file)

    for item in data:
        if int(item['id']) == int(choosed_id):
            item["description"] = text

    with open(work_file, 'w') as file:
        json.dump(data, file, indent = 4)
        
def mark_on_id(choosed_id, status):
    
    with open(work_file, 'r') as file:
        data = json.load(file)
    
    for item in data:
        if int(item["id"]) == int(choosed_id):

            if status == 'todo':
                item["status"] = status
                with open(work_file, 'w') as file:
                    json.dump(data, file, indent = 4)

            elif status == 'in-progress':
                item["status"] = status
                with open(work_file, 'w') as file:
                    json.dump(data, file, indent = 4)

            elif status == 'done':
                item["status"] = status
                with open(work_file, 'w') as file:
                    json.dump(data, file, indent = 4)

            else:
                print(f'Статус {status} не распознан')

            break



def show_list(status):

    with open(work_file, 'r') as file:
        data = json.load(file)

    if status == 'all':
        print(json.dumps(data, indent = 4))

    elif status == 'todo':
        todo_tasks = [task for task in data if task['status'] == 'todo']
        print(json.dumps(todo_tasks, indent = 4))

    elif status == 'in-progress':
        in_progress_tasks = [task for task in data if task['status'] == 'in-progress']
        print(json.dumps(in_progress_tasks, indent = 4))

    elif status == 'done':
        done_tasks = [task for task in data if task['status'] == 'done']
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
    print(f'Элемент удалён: {args.delete}')
    delete_id(int(args.delete))

elif args.update:
    id_from_cli, text_from_cli = args.update[0], ' '.join(args.update.split()[1:])
    print(f'Элемент {id_from_cli} обновлён на: {text_from_cli}')
    update_id(int(id_from_cli), str(text_from_cli))

elif args.mark:
    id_from_cli, status_from_cli = args.mark.split()
    print(f'Статус элемента {id_from_cli} изменён на: {status_from_cli}')
    mark_on_id(int(id_from_cli), str(status_from_cli))

else:
    exit()







     



            

        