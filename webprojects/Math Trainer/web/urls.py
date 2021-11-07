from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
       path('', views.main),
       path('quiz/',views.quiz),
       path('answers/<int:Answerss>/',views.answers)
    ]  
###Stats url patterns
StatsUrlPatterns = [
       path('',views.stats),
       path('charts/',views.charts),
       path('charts/AnswersChart/',views.AnswersChart),
       path('charts/ResultChart/',views.ResultsChart)
]


###API URLPATTERNS
ApiUrlPatterns = [       
   path('CheckQuestions/',views.CheckAnswers),
   path('equation/<int:level>/',views.generateequation)
   ]



if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


