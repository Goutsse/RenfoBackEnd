from rest_framework.routers import DefaultRouter
from .views import (
    AuteurViewSet, LivreViewSet, CategorieViewSet, ExemplaireViewSet, EmpruntViewSet, 
    CommentaireViewSet, EditeurViewSet, EvaluationViewSet
)

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet)
router.register(r'livres', LivreViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'exemplaires', ExemplaireViewSet)
router.register(r'emprunts', EmpruntViewSet)
router.register(r'commentaires', CommentaireViewSet)
router.register(r'editeurs', EditeurViewSet)
router.register(r'evaluations', EvaluationViewSet)

urlpatterns = router.urls
