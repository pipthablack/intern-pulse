import unittest
from app.app import app, db, User

class TestUserAPI(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_create_user(self):
        response = self.app.post('/users', json={'name': 'Alice'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'Alice')

    def test_get_user_by_name(self):
        with app.app_context():
            user = User(name='Bob')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user again to ensure it's loaded correctly
            user = User.query.filter_by(name='Bob').first()

            response = self.app.get('/users?name=Bob')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['name'], 'Bob')

    def test_get_user_by_id(self):
        with app.app_context():
            user = User(name='Charlie')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user again to ensure it's loaded correctly
            user = User.query.filter_by(name='Charlie').first()

            response = self.app.get(f'/users/{user.id}')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['name'], 'Charlie')

    def test_update_user_by_name(self):
        with app.app_context():
            user = User(name='Dave')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user again to ensure it's loaded correctly
            user = User.query.filter_by(name='Dave').first()

            response = self.app.put('/users?name=Dave', json={'name': 'David'})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['name'], 'David')

    def test_update_user_by_id(self):
        with app.app_context():
            user = User(name='Eve')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user again to ensure it's loaded correctly
            user = User.query.filter_by(name='Eve').first()

            response = self.app.put(f'/users/{user.id}', json={'name': 'Evelyn'})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['name'], 'Evelyn')

    def test_delete_user_by_name(self):
        with app.app_context():
            user = User(name='Frank')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user again to ensure it's loaded correctly
            user = User.query.filter_by(name='Frank').first()

            response = self.app.delete('/users?name=Frank')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['message'], 'User Frank deleted successfully')

    def test_delete_user_by_id(self):
        with app.app_context():
            user = User(name='Grace')
            db.session.add(user)
            db.session.commit()

            # Retrieve the user again to ensure it's loaded correctly
            user = User.query.filter_by(name='Grace').first()

            response = self.app.delete(f'/users/{user.id}')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['message'], 'User deleted successfully')

if __name__ == '__main__':
    unittest.main()
