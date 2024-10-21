import django_filters
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation

class AuteurFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(field_name='nom', lookup_expr='icontains')
    nationalite = django_filters.CharFilter(field_name='nationalite', lookup_expr='icontains')

    class Meta:
        model = Auteur
        fields = ['nom', 'nationalite']

class LivreFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(field_name='titre', lookup_expr='icontains')
    langue = django_filters.CharFilter(field_name='langue', lookup_expr='icontains')

    class Meta:
        model = Livre
        fields = ['titre', 'langue', 'categorie', 'editeur', 'auteurs']

class CategorieFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(field_name='nom', lookup_expr='icontains')
    slug = django_filters.CharFilter(field_name='slug', lookup_expr='icontains')

    class Meta:
        model = Categorie
        fields = ['nom', 'slug']

class ExemplaireFilter(django_filters.FilterSet):
    etat = django_filters.CharFilter(field_name='etat', lookup_expr='icontains')
    localisation = django_filters.CharFilter(field_name='localisation', lookup_expr='icontains')

    class Meta:
        model = Exemplaire
        fields = ['etat', 'disponibilite', 'localisation', 'livre']

class EmpruntFilter(django_filters.FilterSet):
    statut = django_filters.CharFilter(field_name='statut', lookup_expr='icontains')

    class Meta:
        model = Emprunt
        fields = ['utilisateur', 'statut', 'date_emprunt']

class CommentaireFilter(django_filters.FilterSet):
    contenu = django_filters.CharFilter(field_name='contenu', lookup_expr='icontains')

    class Meta:
        model = Commentaire
        fields = ['livre', 'utilisateur', 'visible', 'modere']

class EditeurFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(field_name='nom', lookup_expr='icontains')
    adresse = django_filters.CharFilter(field_name='adresse', lookup_expr='icontains')

    class Meta:
        model = Editeur
        fields = ['nom', 'site_web', 'adresse']

class EvaluationFilter(django_filters.FilterSet):
    commentaire = django_filters.CharFilter(field_name='commentaire', lookup_expr='icontains')

    class Meta:
        model = Evaluation
        fields = ['livre', 'utilisateur', 'note', 'recommande']
