# # from django.shortcuts import render, HttpResponse
# #
# # def main (request):
# #     return render (request, 'index.html')
# #
# # def about (request):
# #     return HttpResponse ("<h2> My name is Vlad</h2>")
# # # Create your views here.
# from django.shortcuts import render, HttpResponse
#
#
# # Create your views here.
# def main(request):
#     return render(request, 'index.html')
#
#
# def about(request):
#     author = {
#         "name": "Евгений",
#         "surname": "Юрченко"
#     }
#     context = {
#         "author": author,
#         "age": 36,
#         "hobbies": ["programming", "game", "bike"]
#     }
#     return render(request, 'about.html', context)

from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def main(request):
    return render(request, 'index.html')


def item(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        raise Http404
    context = {
        "item": item
    }
    # for item in items:
    #     if item["id"] == id:
    #         context["item"] = item
    return render(request, 'item.html', context)
    return render(request, 'item.html', context)

    return HttpResponse(f"Товар с id={id} не найден")


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)