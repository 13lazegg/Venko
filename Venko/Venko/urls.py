from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Venko.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Admin.views.login', name='login'),
    url(r'^home/', 'Admin.views.home', name='home'),
    url(r'^alumnos/', 'Admin.views.alumnos', name='alumnos'),
    url(r'^borrar/(\d+)$', 'Admin.views.borrar', name='borrar'),
    url(r'^add/$', 'Admin.views.add', name='add'),
    url(r'^addServicio/$', 'Admin.views.addServicio', name='addServicio'),
    url(r'^alumnosDetalle/(\d+)$', 'Admin.views.alumnosDetalle', name='alumnosDetalle'),
    url(r'^modServicio/(\d+)$', 'Admin.views.modServicio', name='modServicio'),
    url(r'^servicios/', 'Admin.views.servicios', name='servicios'),
    url(r'^pagoDetalle/(\d+)$', 'Admin.views.pagoDetalle', name='pagoDetalle'),
    url(r'^pagos/', 'Admin.views.pagos', name='pagos'),
    url(r'^getAlumnos/', 'Admin.views.getAlumnos', name='getAlumnos'),

    
    url(r'^admin/', include(admin.site.urls)),
)
