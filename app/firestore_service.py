import firebase_admin 
from firebase_admin import credentials, firestore, initialize_app, exceptions   


if (not len(firebase_admin._apps)):
    cred = credentials.ApplicationDefault()
    initialize_app(cred)

db = firestore.client()

def get_users():
    try:        
        return db.collection('users').get()
    except exceptions.FirebaseError as e:
        # Manejar la excepción, por ejemplo, imprimir un mensaje de error
        print(f"Error de Firebase: {e}")
        return None

    
def get_user(user_id):
    return db.collection('users').document(user_id).get()
    

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({ 'password': user_data.password })

        
def get_todos(user_id):
    try:
        return db.collection('users')\
            .document(user_id)\
            .collection('todos').get()
    except exceptions.FirebaseError as e:
        # Manejar la excepción, por ejemplo, imprimir un mensaje de error
        print(f"No se reconocen to does: {e}")
        return None


def put_todo(user_id, description):
    todos_collection_ref = db.collection('users').document(user_id).collection('todos')
    todos_collection_ref.add({ 'description': description, 'done': False })
    

def delete_todo(user_id, todo_id):
    todo_ref = db.collection('users').document(user_id).collection('todos').document(todo_id)
    todo_ref.delete()
    
def update_todo(user_id, todo_id, done):
    todo_done = not bool(done)
    todo_ref = db.collection('users').document(user_id).collection('todos').document(todo_id)
    todo_ref.update({ 'done':todo_done })