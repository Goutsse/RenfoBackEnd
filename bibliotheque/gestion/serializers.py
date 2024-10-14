from rest_framework import serializers
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    auteurs = AuteurSerializer(many=True, read_only=True)
    categorie = serializers.StringRelatedField()
    editeur = serializers.StringRelatedField()

    class Meta:
        model = Livre
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ExemplaireSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(read_only=True)

    class Meta:
        model = Exemplaire
        fields = '__all__'

class EmpruntSerializer(serializers.ModelSerializer):
    exemplaire = ExemplaireSerializer(read_only=True)
    utilisateur = serializers.StringRelatedField()

    class Meta:
        model = Emprunt
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    livre = LivreSerializer(read_only=True)

    class Meta:
        model = Commentaire
        fields = '__all__'

class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    livre = LivreSerializer(read_only=True)

    class Meta:
        model = Evaluation
        fields = '__all__'
