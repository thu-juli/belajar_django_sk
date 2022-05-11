from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def permissionAuthor(user):
    test_group = Group.objects.get(name='author')
    user_group = user.groups.all()

    status = test_group in user_group
    print(status)
    return status

# using function
# @user_passes_test(permissionAuthor)
# def AddArticleView(request):
#     context = {
#         'page_title': 'Add Article'
#     }
#     return render(request, 'article/article_add.html', context)

# using lambda


@user_passes_test(lambda user: Group.objects.get(name='author') in user.groups.all())
def AddArticleView(request):
    context = {
        'page_title': 'Add Article'
    }
    return render(request, 'article/article_add.html', context)


def indexArticleView(request):
    context = {
        'page_title': 'Article View'
    }
    test_group = Group.objects.get(name='author')
    user_group = request.user.groups.all()
    template_name = None
    if test_group in user_group:
        template_name = 'article/author_index.html'
    else:
        template_name = 'article/index.html'

    return render(request, template_name, context)
