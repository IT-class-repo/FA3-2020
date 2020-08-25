import sqlite3
from flask import Flask, jsonify, g, request
import datetime

app = Flask(__name__)

DATABASE = 'database.db'


def get_db():
    """
    Function make use of Flask Global object to share db connection
    Function return the db connect
     """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.route('/pokemon')
def pokemon():
    c = get_db().cursor()
    results = c.execute("SELECT * FROM pokemon")
    pokemon_info = []
    for row in results:
        pokemon_info.append(dict(row))
    return jsonify(pokemon_info)


@app.route("/pokemon/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_poke_by_id(id):
    c = get_db().cursor()
    if request.method == 'GET':
        results = c.execute("SELECT * FROM pokemon WHERE pokeId =" + str(id))
        pokemon_info = results.fetchone()
        return jsonify(dict(pokemon_info)) if pokemon_info else jsonify(None)
    elif request.method == 'PUT':
        pass  # Todo
    elif request.method == 'DELETE':
        pass  # Todo


@app.route("/pokemon/add", methods=['POST'])
def add_poke():
    newPoke = request.get_json()
    if not newPoke or 'name' not in newPoke:
        return jsonify({"error": "Required attribute not found"})

    name = newPoke.get("name")
    time = datetime.datetime.now().ctime()
    addedByUserid = newPoke.get("addedByUserid")
    hp = newPoke.get("hp")
    attack = newPoke.get("attack")
    defense = newPoke.get("defense")
    speed = newPoke.get("speed")
    image = newPoke.get("image")

    c = get_db().cursor()
    sql = "INSERT INTO pokemon (name,addedDatetime,addedByUserId,hp,attack,defense,speed,image) VALUES (?,?,?,?,?,?,?,?)"
    c.execute(sql, (name, time, addedByUserid,
                    hp, attack, defense, speed, image))
    get_db().commit()
    return jsonify("done")


@app.route('/caught')
def caught():
    c = get_db().cursor()
    results = c.execute("SELECT * FROM caught")
    caught_info = []
    for row in results:
        caught_info.append(dict(row))
    return jsonify(caught_info)


@app.route("/caught/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_caught_by_id(id):
    c = get_db().cursor()
    if request.method == 'GET':
        results = c.execute("SELECT * FROM caught WHERE pokeId =" + str(id))
        caught_info = results.fetchone()
        return jsonify(dict(caught_info)) if caught_info else jsonify(None)
    elif request.method == 'PUT':
        pass  # Todo
    elif request.method == 'DELETE':
        pass  # Todo


@app.route("/caught/add", methods=['POST'])
def add_caught():
    newPoke = request.get_json()
    if not newPoke or 'name' not in newPoke:
        return jsonify({"error": "Required attribute not found"})

    name = newPoke.get("name")
    time = datetime.datetime.now().ctime()
    addedByUserid = newPoke.get("addedByUserid")
    hp = newPoke.get("hp")
    attack = newPoke.get("attack")
    defense = newPoke.get("defense")
    speed = newPoke.get("speed")
    image = newPoke.get("image")

    c = get_db().cursor()
    sql = "INSERT INTO caught (name,addedDatetime,addedByUserId,hp,attack,defense,speed,image) VALUES (?,?,?,?,?,?,?,?)"
    c.execute(sql, (name, time, addedByUserid,
                    hp, attack, defense, speed, image))
    get_db().commit()
    return jsonify("done")


if __name__ == '__main__':
    app.run(debug=True)
