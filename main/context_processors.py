def role_flags(request):
    is_editor = False
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name="Editor").exists()
    return {"is_editor": is_editor}