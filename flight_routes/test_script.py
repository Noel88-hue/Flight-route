from django.test import Client
c = Client()
response = c.post('/search/', {'duration': 1, 'position': 'left', 'n': 2})
print("STATUS:", response.status_code)
print("CONTEXT:", response.context['result'])
