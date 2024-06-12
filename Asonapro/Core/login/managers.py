from django.contrib.auth.models import Group

# a falta de un metodo en django que me revise si un usuario existe dentro de un grupo
# me creo esta funcion


def is_in_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()
