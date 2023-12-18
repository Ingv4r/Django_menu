from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("menu/", include("menu_app.urls")),
    path(
        "mptt/",
        TemplateView.as_view(template_name="mptt_tree_menu/index.html")
    )
]
