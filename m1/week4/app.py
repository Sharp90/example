from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]
id = len(menus)

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    global id
    id = id + 1
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    new_menu = {
        "id" : id,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menus | 자료를 업데이트한다.
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    # 전달받은 자료로 menus 자원을 업데이트
    request_data = request.get_json()
    for menu in menus:
        if menu.get('id') == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return jsonify(menu)

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    count = 0
    for menu in menus:
        if menu.get('id') == id:
            return jsonify(menus.pop(count))
        count += 1

if __name__ == '__main__':
    app.run()