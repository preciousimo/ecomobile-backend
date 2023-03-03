from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def endpoints(request):

    data = ['/auth/                   (for login)',
            '/auth/refresh/           (refresh token)',
            '/users/register/         (register user)',
            '/products                (list of products)',
            '/products/categories     (products categories)',]

    return Response(data)