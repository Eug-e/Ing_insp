from django.urls import path
from beltex.views import index
from beltex.views import str1
from beltex.views import Ver
from beltex.views import ex41
from beltex.views import login_user
from beltex.views import log_out
from beltex.views import First
from beltex.views import Second
from beltex.views import Form
from beltex.views import Ajax_path
from beltex.views import Aja
from beltex.views import back
from beltex.views import Costs
from beltex.views import Spec
from django.conf import settings
from django.conf.urls.static import static
from beltex.views import Obj

urlpatterns = [
    path('line1', index),
    path('line2', str1),
    path('line3', Ver),
    path('line4', ex41),
    path('line6', login_user),
    path('line7', log_out),
    path('line8', First),
    path('line9', Second),
    path('line10', Form),
    path('line11', Ajax_path),
    path('line12', Aja),
    path('line13', back),
    path('line14', Costs),
    path('line15', Spec),
    path('line16', Obj),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)