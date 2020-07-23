from django.shortcuts import render
from .models import Destination, Background, Intro
from django.utils import timezone
from .models import Post
from django.views.generic.dates import YearArchiveView

from travello.models import Post
import datetime
from django.utils.timezone import utc


# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Thailand'
    dest1.desc = 'The city that never sleep'
    dest1.img = '20.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Japan'
    dest2.desc = 'The city that never sleep'
    dest2.img = '19.jpg'
    dest2.price = 800
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Poland'
    dest3.desc = 'The city that never sleep'
    dest3.img = '26.jpg'
    dest3.price = 500
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Poland'
    dest4.desc = 'The city that never sleep'
    dest4.img = '25.jpg'
    dest4.price = 500
    dest4.offer = True

    dests = [dest1, dest2, dest3, dest4]

    intro_item1 = Intro()
    intro_item1.img = 'beach.svg'
    intro_item1.name = 'Top Thai Desserts'
    intro_item1.desc = 'Sollicitudin mauris lobortis in.'

    intro_item2 = Intro()
    intro_item2.img = 'wallet.svg'
    intro_item2.name = 'The Best Thai Desserts'
    intro_item2.desc = 'Sollicitudin mauris lobortis in.'

    intro_item3 = Intro()
    intro_item3.img = 'suitcase.svg'
    intro_item3.name = 'Amazing Thai Desserts'
    intro_item3.desc = 'Sollicitudin mauris lobortis in.'

    intro_items = [intro_item1, intro_item2, intro_item3]

    return render(request, "index.html",
                  {
                      'dests': dests,
                      'intro_items': intro_items,
                   })


def about_us(request):
    aboutus1 = Post()
    aboutus1.ub_date = datetime.datetime.utcnow().replace(tzinfo=utc)
    aboutus1.name = 'My first post'
    aboutus1.desc = 'Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. ' \
                   'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,' \
                   ' tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.'

    aboutus2 = Post()
    aboutus2.ub_date = datetime.datetime.utcnow().replace(tzinfo=utc)
    aboutus2.name = 'My second post'
    aboutus2.desc = 'Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. ' \
                   'Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,' \
                   ' tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.'

    aboutus = [aboutus1, aboutus2]
    return render(request, 'aboutus.html', {'aboutus': aboutus})


def add(request):
    val1 = int(request.POST['number1'])
    val2 = int(request.POST['number2'])
    res = val1 + val2
    return render(request, "result.html", {'result': res}
                  )


def addIndex(request):
    name = request.GET['name']
    description = request.GET['description']
    return render(request, 'addindex.html',
                  {
                      'name': name,
                      "description": description
                  })


def article(request):
    return render(request, 'article.html',
                  {
                      'name': 'Ning'
                  })









