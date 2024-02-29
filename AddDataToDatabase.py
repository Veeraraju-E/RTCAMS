import firebase_admin
from firebase_admin import credentials, db

# the firebase service account key
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://rtcams-4b4df-default-rtdb.firebaseio.com/'})

# create a database reference

ref = db.reference('Students') # --> store the IDs of students
data = {

}