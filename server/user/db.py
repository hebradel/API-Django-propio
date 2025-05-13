from apps.fun.Model import *
class User(Model):
	id = AutoField(primary_key=True)
	nombre = CharField(max_length=45, null=True, blank=True)
	password = CharField(max_length=250, null=True, blank=True)
	def __str__(self):
		return self.nombre or self.id

def create_tables():
    User.create_table()