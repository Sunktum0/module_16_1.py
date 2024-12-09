from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Создаем экземпляр FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/")
async def read_root():
    return "Главная страница"

# Маршрут к странице администратора
@app.get("/user/admin")
async def read_admin():
    return "Вы вошли как администратор"

# Маршрут к страницам пользователей по ID
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут к страницам пользователей с параметрами в запросе
@app.get("/user")
async def read_user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"