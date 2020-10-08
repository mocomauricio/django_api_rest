from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User


##############################################
# Estas vistas se usan para mostar usuarios 
# con sus lista de snippets creadas
# (campo owner del modelo Snippets) 
# Obs: el ID es del usuario 

#(GET) localhost:8000/api/users/
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# (GET) localhost:8000/api/users/:id
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#############################################


#
# CRUD de Snippet implementedo con Clases Genéricas,
# como comentarios sus correspondientes URL
# Obs: el ID es del snippet
#

# (GET) localhost:8000/api/snippets/
# (POST) localhost:8000/api/snippets/
class SnippetListCreate(generics.ListCreateAPIView):
	queryset = Snippet.objects.filter( borrado=False )
	serializer_class = SnippetSerializer

	# sobrecarga del metodo perform_create para almacenar el usuario logeado
	# en el campo owner del modelo Snippet
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

# (GET) localhost:8000/api/snippets/:id
# (PUT) localhost:8000/api/snippets/:id
# (DELETE) localhost:8000/api/snippets/:id
class SnippetDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.filter( borrado=False )
	serializer_class = SnippetSerializer
