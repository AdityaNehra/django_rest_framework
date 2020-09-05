import os
import io
import django
if 'env setting':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_framework.settings')
    django.setup()

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
print(serializer.data)

content = JSONRenderer().render(serializer.data)
print(content)

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

serializer = SnippetSerializer(data=data)
print(serializer.is_valid())

print(serializer.validated_data)
serializer.save()

serializer = SnippetSerializer(Snippet.objects.all(), many=True)
print(serializer.data)