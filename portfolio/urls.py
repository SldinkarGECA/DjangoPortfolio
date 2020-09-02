from django.contrib import admin
from django.urls import path, include
# new
from django.conf import settings
from django.conf.urls.static import static

# from jobs import views
import jobs.views

urlpatterns = [
                  path('admin/', admin.site.urls, name="admin"),
                  path('', jobs.views.home, name="home"),
                  path('blog/', include('blog.urls'), name="blogs"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
