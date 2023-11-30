from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}

    try:
        data = json.loads(body)
    except:
        pass
    
    print(data)
    data['headers'] = request.headers
    return JsonResponse(data)

# Create your views here.
