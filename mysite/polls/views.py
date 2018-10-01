from django.http import HttpResponse


def nothing(request):
    return HttpResponse("This is a bad request. Use one of the other routes (language, system, or ide)")


def language(request):
    return HttpResponse("My favorite Language is Javascript")


def system(request):
    return HttpResponse("My favorite system is Linux")


def ide(request):
    return HttpResponse("My favorite IDE is Intellij")

