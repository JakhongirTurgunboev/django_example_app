import logging

class SimpleMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    # Preparation ops

    # Retrieving the response
    response = self.get_response(request)
    with open("file.log", "a") as f:
      if request.user.is_authenticated:
        f.write(request.user.username + str(request) + "\n")
    # Updating the response

    # Returning the response
    return response
