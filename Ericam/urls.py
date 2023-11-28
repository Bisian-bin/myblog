from django.contrib import admin
from django.urls import include, path  # 这里引入include()方法
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('users/', include('users.urls')),  # 这里使用include()引入users.urls文件
                  path('', include('blog.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # 配置静态文件url

# 配置用户上传文件url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)