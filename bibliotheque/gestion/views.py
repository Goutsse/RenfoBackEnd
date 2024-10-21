from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation
from .serializers import (
    AuteurSerializer, LivreSerializer, CategorieSerializer, ExemplaireSerializer,
    EmpruntSerializer, CommentaireSerializer, EditeurSerializer, EvaluationSerializer
)
from .filters import AuteurFilter, LivreFilter, CategorieFilter, ExemplaireFilter, EmpruntFilter, CommentaireFilter, EditeurFilter, EvaluationFilter

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AuteurFilter
    ordering_fields = ['nom', 'date_de_naissance']
    ordering = ['nom']
    permission_classes = [IsAuthenticated] 

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LivreFilter
    ordering_fields = ['date_de_publication', 'titre']
    ordering = ['date_de_publication']
    permission_classes = [IsAuthenticated] 

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CategorieFilter
    ordering_fields = ['nom']
    ordering = ['nom']
    permission_classes = [IsAuthenticated]  

class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ExemplaireFilter
    ordering_fields = ['date_acquisition', 'etat']
    ordering = ['date_acquisition']
    permission_classes = [IsAuthenticated]  

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EmpruntFilter
    ordering_fields = ['date_emprunt', 'date_retour_prevue']
    ordering = ['date_emprunt']
    permission_classes = [IsAuthenticated]  

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CommentaireFilter
    ordering_fields = ['date_publication', 'note']
    ordering = ['date_publication']
    permission_classes = [IsAuthenticated]  

class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EditeurFilter
    ordering_fields = ['nom']
    ordering = ['nom']
    permission_classes = [IsAuthenticated] 

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EvaluationFilter
    ordering_fields = ['date_evaluation', 'note']
    ordering = ['date_evaluation']
    permission_classes = [IsAuthenticated]  
