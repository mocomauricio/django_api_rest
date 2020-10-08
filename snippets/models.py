from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):

	class Meta:
		#ordena por la fecha de creacion que se alamacena en el campo "created"
		ordering = ['created'] 


	title = models.CharField(max_length=100, blank=True, default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

	owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
	highlighted = models.TextField( editable = False)

	# este campo se rellena sólito con la fecha de creacion y luego ya no se modifica
	# esto se consigue con el parametro auto_now_add=True
	created = models.DateTimeField(auto_now_add=True)

	# campo booleano para implementar un borrado lógico
	borrado = models.BooleanField(default=False)


	# sobrecarga del método save del modelo
	def save(self, *args, **kwargs):
		"""
		Use the `pygments` library to create a highlighted HTML
		representation of the code snippet.
		"""
		lexer = get_lexer_by_name(self.language)
		linenos = 'table' if self.linenos else False
		options = {'title': self.title} if self.title else {}
		formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super(Snippet, self).save(*args, **kwargs)

	# sobrecarga del metodo delete del modelo para implementar borrado lógico
	def delete(self, *args, **kwargs):
		self.borrado = True
		self.save()

	def __str__(self):
		return self.title