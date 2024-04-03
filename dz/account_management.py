from dz.class_account_management import Admin, User

admin1 = Admin(1, "Nick", 5)
admin1.add_user("Pam")
admin1.add_user("Rob")
admin1.add_user("Bob")
admin1.list_user()
admin1.remove_user("Bob")
admin1.remove_user("Pob")
admin1.list_user()

user1 = User(2, "Pop")


