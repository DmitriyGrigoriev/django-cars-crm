from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "emails"


urlpatterns = [
    re_path(r"^list/", views.emails_list, name="list"),
    re_path(r"^compose/", views.email, name="compose"),
    re_path(r"^email_sent/", views.email_sent, name="email_sent"),
    re_path(
        r"^email_move_to_trash/(?P<pk>\d+)/$",
        views.email_move_to_trash,
        name="email_move_to_trash",
    ),
    re_path(r"^email_delete/(?P<pk>\d+)/$", views.email_delete, name="email_delete"),
    re_path(r"^email_trash/", views.email_trash, name="email_trash"),
    re_path(
        r"^email_trash_delete/(?P<pk>\d+)/$",
        views.email_trash_delete,
        name="email_trash_delete",
    ),
    re_path(r"^email_draft/", views.email_draft, name="email_draft"),
    re_path(
        r"^email_draft_delete/(?P<pk>\d+)/$",
        views.email_draft_delete,
        name="email_draft_delete",
    ),
    re_path(r"^email_imp/(?P<pk>\d+)/$", views.email_imp, name="email_imp"),
    re_path(r"^email_imp_list/", views.email_imp_list, name="email_imp_list"),
    re_path(
        r"^email_sent_edit/(?P<pk>\d+)/$", views.email_sent_edit, name="email_sent_edit"
    ),
    re_path(r"^email_unimp/(?P<pk>\d+)/$", views.email_unimp, name="email_unimp"),
    re_path(r"^email_view/(?P<pk>\d+)/$", views.email_view, name="email_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
