from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

# Create the database and the database table
with app.app_context():
    db.create_all()
def find_user_by_name(name):
    """
    This function retrieves a user from the database based on their name.

    Parameters:
    name (str): The name of the user to search for.

    Returns:
    User: The user object if found, otherwise None.
    """
    return User.query.filter_by(name=name).first()

def find_user_by_id(user_id):
    """
    This function retrieves a user from the database based on their unique ID.

    Parameters:
    user_id (int): The unique ID of the user to search for.

    Returns:
    User: The user object if found, otherwise None.
    """
    return User.query.get(user_id)


@app.route('/')
def hello():
    return jsonify(message="Hello from Flask on Vercel!")

# If the app is running within Vercel's serverless function, it should be wrapped like this:
def handler(event, context):
    from werkzeug.serving import run_simple
    return run_simple("0.0.0.0", 5000, app)


@app.route('/users', methods=['POST'])
def create_user():
    """
    This function handles the creation of a new user.

    It expects a JSON payload with a 'name' field. If the name is not provided,
    it returns a 400 error. If the user already exists, it returns a 400 error.
    Otherwise, it creates a new user, saves it to the database, and returns the
    user's ID and name in a JSON response.
    """
    data = request.json
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    if find_user_by_name(data['name']):
        return jsonify({'error': 'User already exists'}), 400

    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'name': new_user.name}), 201

@app.route('/users', methods=['GET'])
def get_user_by_name():
    """
    This function handles retrieving a user by their name.

    It expects a 'name' query parameter. If the name is not provided, it returns
    a 400 error. If the user is found, it returns the user's ID and name in a JSON
    response. Otherwise, it returns a 404 error.
    """
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name query parameter is required'}), 400

    user = find_user_by_name(name)
    if user:
        return jsonify({'id': user.id, 'name': user.name})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """
    This function handles retrieving a user by their unique ID.

    It expects a user ID in the URL path. If the user is found, it returns the
    user's ID and name in a JSON response. Otherwise, it returns a 404 error.
    """
    user = find_user_by_id(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['PUT'])
def update_user_by_name():
    """
    This function handles updating a user's name by their old name.

    It expects a 'name' query parameter and a JSON payload with a 'name' field.
    If either the old name or the new name is not provided, it returns a 400 error.
    If the user is found, it updates the user's name, saves it to the database,
    and returns the user's ID and name in a JSON response. Otherwise, it returns
    a 404 error.
    """
    old_name = request.args.get('name')
    new_name = request.json.get('name')

    if not old_name or not new_name:
        return jsonify({'error': 'Both old and new names are required'}), 400

    user = find_user_by_name(old_name)
    if user:
        user.name = new_name
        db.session.commit()
        return jsonify({'id': user.id, 'name': user.name})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    """
    This function handles updating a user's name by their unique ID.

    It expects a user ID in the URL path and a JSON payload with a 'name' field.
    If the new name is not provided, it returns a 400 error. If the user is found,
    it updates the user's name, saves it to the database, and returns the user's
    ID and name in a JSON response. Otherwise, it returns a 404 error.
    """
    data = request.json
    if 'name' not in data:
        return jsonify({'error': 'New name is required in the request body'}), 400

    user = find_user_by_id(user_id)
    if user:
        user.name = data['name']
        db.session.commit()
        return jsonify({'id': user.id, 'name': user.name})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['DELETE'])
def delete_user_by_name():
    """
    This function handles deleting a user by their name.

    It expects a 'name' query parameter. If the name is not provided, it returns
    a 400 error. If the user is found, it deletes the user from the database and
    returns a success message in a JSON response. Otherwise, it returns a 404 error.
    """
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name query parameter is required'}), 400

    user = find_user_by_name(name)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'User {name} deleted successfully'})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    """
    This function handles deleting a user by their unique ID.

    It expects a user ID in the URL path. If the user is found, it deletes the
    user from the database and returns a success message in a JSON response.
    Otherwise, it returns a 404 error.
    """
    user = find_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)