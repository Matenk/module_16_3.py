from fastapi import FastAPI, Path

app = FastAPI()

users = {'1' : 'Имя: Сергей, возраст: 18'}

@app.get('/users')
async def all_users() -> dict:
    return users

@app.post('/users/{username}/{age}')
async def add_users(username: str = Path(min_length=3, max_length=18, description='Enter your username', example='Adam')
                    , age: int = Path(ge=0, le=120, description='Enter your age', example='37')):
    current_user_id = str(int(max(users, key=int)) + 1)
    users[current_user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {current_user_id} is registered.'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str=Path(min_length=3, max_length=18, description='Enter new username'),
                      age: int=Path(ge=0, le=120, description='Enter new age')):

    if user_id in users: # Проверка наличия ID в БД (при обновлении словарей python создает новый данные, если таких не
        # было раннее, данная проверка решает эту проблему).
        users[user_id] = f'Имя {username}, возраст {age}'
        return f"The user {user_id} is updated."
    else:
        return f'The user {user_id} not found, try another ID'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    if user_id in users:
        users.pop(user_id)
        return f'The user {user_id} was deleted.'
    else:
        return f'The user {user_id} not found, try another ID'



