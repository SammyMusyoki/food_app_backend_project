from main3 import app
from model2 import db, User

user_data = [
{
 "id": 1,
  "first_name": "Bree",
  "last_name": "Jeynes",
  "email": "bjeynes0@spiegel.de",
  "user_type": "restaurent_owner",
  "password": "pT5(`e?Z"
},{
  "id": 2,
  "first_name": "Paloma",
  "last_name": "Spacey",
  "email": "pspacey1@hexun.com",
  "user_type": "employee",
  "password": "qK8#,Z/\\<"
}, {
  "id": 3,
  "first_name": "Merla",
  "last_name": "Timbridge",
  "email": "mtimbridge2@ameblo.jp",
  "user_type": "customer",
  "password": "bX0$)r*u"
}, {
  "id": 4,
  "first_name": "Betsy",
  "last_name": "Poznanski",
  "email": "bpoznanski3@paypal.com",
  "user_type": "restaurent_owner",
  "password": "oA0{KB66!"
}, {
  "id": 5,
  "first_name": "Sibylla",
  "last_name": "Kiley",
  "email": "skiley4@scientificamerican.com",
  "user_type": "employee",
  "password": "eD7`e'S%"
}, {
  "id": 6,
  "first_name": "Leontyne",
  "last_name": "Fidge",
  "email": "lfidge5@bing.com",
  "user_type": "customer",
  "password": "hL4$d=v&nLt"
}, {
  "id": 7,
  "first_name": "Mario",
  "last_name": "Gianettini",
  "email": "mgianettini6@google.com",
  "user_type": "restaurent_owner",
  "password": "kG6}knkI!t/@nG"
}, {
  "id": 8,
  "first_name": "Brinn",
  "last_name": "Aireton",
  "email": "baireton7@google.co.jp",
  "user_type": "employee",
  "password": "jZ0}J`QfWzR"
}, {
  "id": 9,
  "first_name": "Rachel",
  "last_name": "Rawling",
  "email": "rrawling8@guardian.co.uk",
  "user_type": "customer",
  "password": "tZ3+0W\\6m"
}, {
  "id": 10,
  "first_name": "Hilary",
  "last_name": "Jankovsky",
  "email": "hjankovsky9@163.com",
  "user_type": "restaurent_owner",
  "password": "iA7.vD{ulrl1{"
}]
    # Add other user data here


user_type = ['restaurent_owner', 'employee', 'customer']

with app.app_context():
    for data in user_data:
        users = User(
            id=data["id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            user_type=data["user_type"],
            password=data["password"]
        )
        db.session.add(users)

    db.session.commit()

