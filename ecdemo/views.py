from django.shortcuts import render

# <summary> 首頁 </summary>
# <return> 首頁 </return>
def index(request):

    return render(request, 'index.html', locals())

# <summary> 服飾 </summary>
# <return> 服飾頁面 </return>
def dresses(request):

    return render(request, 'dresses.html', locals())

# <summary> 鞋類 </summary>
# <return> 鞋類頁面 </return>
def sandals(request):

    return render(request, 'sandals.html', locals())

# <summary> 關於 </summary>
# <return> 關於頁面 </return>
def about(request):

    return render(request, 'about.html', locals())

# <summary> 訂單 </summary>
# <return> 訂單頁面 </return>
def order(request):

    return render(request, 'mail.html', locals())
