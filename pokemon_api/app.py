from flask import Flask, render_template, jsonify,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, or_
from flask_marshmallow import Marshmallow
from utils import csv_to_list
app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_SORT_KEYS'] = False    

mrsh = Marshmallow(app) 

db = SQLAlchemy(app)


'''This is the Pokemon model that creates the Pokemon table and it is used to insert data'''
class Pokemon(db.Model):
    id         = db.Column(db.Integer,    primary_key = True)
    name       = db.Column(db.String(50), nullable=False, )
    type1      = db.Column(db.String(50), nullable=False, )
    type2      = db.Column(db.String(50), nullable=True,  )
    total      = db.Column(db.Integer,    nullable=False, )
    hp         = db.Column(db.Integer,    nullable=False, )
    attack     = db.Column(db.Integer,    nullable=False, )
    defense    = db.Column(db.Integer,    nullable=False, )
    sp_atk     = db.Column(db.Integer,    nullable=False, )
    sp_def     = db.Column(db.Integer,    nullable=False, )
    speed      = db.Column(db.Integer,    nullable=False, )
    generation = db.Column(db.Integer,    nullable=False, )
    legendary  = db.Column(db.Boolean,    nullable=False, )

    def __init__(self, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary):
        self.name       = name
        self.type1      = type1
        self.type2      = type2
        self.total      = total
        self.hp         = hp
        self.attack     = attack
        self.defense    = defense
        self.sp_atk     = sp_atk
        self.sp_def     = sp_def
        self.speed      = speed
        self.generation = generation
        self.legendary  = legendary

db.create_all()
db.session.commit()

'''This is the Pokemon Schema which is used to convert python object data into serialized data'''
class Pokemon_schema(mrsh.Schema):
    class Meta:
        fields = ('id','name','type1','type2','total','hp','attack','defense','sp_atk','sp_def','speed','generation','legendary')
        ordered = True

pokemon_schema = Pokemon_schema(many=False)
pokemons_schema = Pokemon_schema(many=True)

'''This route(method) is the home route and it shows hints on how to use the api with a simple template'''
@app.route('/')
def home():
    return render_template('home.html')

'''This route(method) is used to expose the data from the database, with filters and sorting 
by ascending and descending order'''
@app.route("/view", methods=['GET'])
def view_all():
    if request.json:
        pokemon_filtered= None
        filter_by = ''
        if 'filter_by_type' in request.json:
            filter_by = request.json['filter_by_type']
            pokemon_filtered = Pokemon.query.filter(or_(Pokemon.type1.like(filter_by),Pokemon.type2.like(filter_by)))
        
        if 'sort_by_column' in request.json:
            sort_by_column = request.json['sort_by_column']
            order = ''
            if 'order' in request.json:
                order = request.json['order']
            if order == 'asc':
                if pokemon_filtered:
                    all_pokemons = pokemon_filtered.order_by(sort_by_column).all()
                else:
                    all_pokemons = Pokemon.query.order_by(sort_by_column).all()
            elif order == 'dsc':
                if pokemon_filtered:
                    all_pokemons = pokemon_filtered.order_by(desc(sort_by_column)).all()
                else:
                    all_pokemons = Pokemon.query.order_by(desc(sort_by_column)).all()
            else:
                if pokemon_filtered:
                    all_pokemons = pokemon_filtered.order_by(sort_by_column).all()
                else:
                    all_pokemons = Pokemon.query.order_by(sort_by_column).all()
        else:
            all_pokemons = pokemon_filtered
        result = pokemons_schema.dump(all_pokemons)
        return jsonify(result)
    else:
        all_pokemons = Pokemon.query.all()
        result = pokemons_schema.dump(all_pokemons)
        return jsonify(result)



'''This route(method) deletes all pokemons ( resets the database)'''
@app.route("/deleteall", methods=['DELETE'])
def delete_all_pokemons():
    Pokemon.query.delete()
    db.session.commit()
    return {"success" : "Deleted all Pokemons"}

'''This route(method) takes the pokemon.csv file and loads its data into the pokemon_db database.'''
@app.route("/insertcsv")
def insert_from_csv():
    init_pokemons = csv_to_list('pokemon.csv', Pokemon)
    db.session.add_all(init_pokemons)
    db.session.commit()
    return jsonify(pokemons_schema.dump(init_pokemons))



if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)