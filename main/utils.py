def success_response(data):
    return JsonResponse(data)

def error_response(message):
    return JsonResponse({"message" : message})
