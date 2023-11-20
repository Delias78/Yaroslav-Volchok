from flask import Flask, Response
import uuid
from flask import request
app = Flask(__name__)

users = {}
name = ""
text = ""


@app.route('')
def main():
    return "commands /auth, /send, /logout, /getall"

@app.route('/auth')
def auth():
    name = request.args.get('name')
    if name not in users:
        token = uuid.uuid4()
        users[f'name'] = token
        print(users)
        return (f'Вы успешно авторизовались Твой токен - {token}')
    else:
        return (f'Вы уже авторизовались')
    

    @app.route('/send')
    def send():
        text = request.args.get('text')
        tok = request.args.get('tok')
        count = 0
        for symbol in tok:
            count += 1
        print(count)
        if ...:
            for stokes in users.values():
                if tokens == tok:
                    print("успешно")
                    break
                else:
                    print("неуспешно")
                    break
                if text == None:
                    return 'Текст не указан'
                elif tok == None:
                    return 'Токен не указан'
                elif count < 36:
                    return 'Токен неверный'
                else:
                    return 'Успешно отправлено'
                

@app.route('/logout')
def logout():
    print(users)
    tok = request.args.get('tok')
    count = 0
    if count == 36:
        keys = [key for key, value in users.items() if value == tok]
        print(keys)
        del users[keys[0]]
        print(users)
        return (f'Вы успешно удалили аккаунт')
    if tok == None:
        return 'Токен не указан'
    elif count != 36:
        return 'Токен неверный'
    else:
        keys = [key for key, value in users.items() if value == tok]
        print(keys)
        del users[keys[0]]
        print(users)
        return (f'Вы успешно удалили аккаунт')



@app.route('/getall')
def getall():
    token = request.args.get('token')
    for value in users.items():
        if value == token:
            return Response(json.dumps(msg), status = 200)
        return Response("Токен не найден",status = 403)


if __name__ == '__main__':
    app.run(debug=True)

