from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('warmup-1/near-hundred/<n>', near_hundred),
    path('warmup-2/string-splosion/<string>', string_splosion),
    path('string-2/cat-dog/<string>', cat_dog),
    path('logic-2/lone-sum/<a>/<b>/<c>', lone_sum),
    path('admin/', admin.site.urls),
]
