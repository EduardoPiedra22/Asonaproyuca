from crum import get_current_request
from Core.User.models import User
    

def global_data(request):
    user = get_current_request()
    users = User.objects.prefetch_related('groups', 'user_permissions').filter(is_active=1).exclude(id=user.user.id)
    data = []
    
    for i in users:
        datos = {
            'id': i.id,
            'full_name': i.get_full_name(),
            'image': i.get_image(),
        }
        data.append(datos)
    
    return {'users_data': data}
