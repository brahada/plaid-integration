from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='frontend/index.html',
            extra_context={'pk': settings.PLAID_PUBLIC_KEY}
        )
    ),
    path(
        'login/',
        TemplateView.as_view(template_name='frontend/login.html'),
    ),
    path(
        'accounts/',
        TemplateView.as_view(
            template_name='frontend/accounts.html',
        ),
        name='accounts'
    )
]
