from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



# Este serializador se utiliza para mostrar los usuarios con sus snippets relacionados. Ej:
# (GET) localhost:8000/api/users/
#
# {
#     "count": 1,
#     "next": null,
#     "previous": null,
#     "results": [
#         {
#             "id": 1,
#             "username": "admin",
#             "snippets": [
#                 1
#             ]
#         }
#     ]
# }
#
# (GET) localhost:8000/api/users/1
#
# {
#     "id": 1,
#     "username": "admin",
#     "snippets": [
#         1
#     ]
# }
#
class UserSerializer(serializers.ModelSerializer):
	# para ello se le agrega un campo "snippets" al JSON que contendra el arreglo
	# de los snippets con el campo owner en del
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

	class Meta:
		model = User
		fields = ['id', 'username', 'snippets']



class SnippetSerializer(serializers.ModelSerializer):
	# se le agrega el campo owner de sólo lectura para evitar que se carge el dato
	# desde la api, porque el campo owner se almacena automáticamente con el usuario
	# logeado que creó un snippet
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Snippet
		fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

