from django.db import models
from django.contrib.auth.models import User

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    date_de_naissance = models.DateField()
    date_de_deces = models.DateField(null=True, blank=True)
    nationalite = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos_auteurs/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

class Editeur(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    site_web = models.URLField()
    email_contact = models.EmailField()
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    resume = models.TextField()
    date_de_publication = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    nombre_de_pages = models.IntegerField()
    langue = models.CharField(max_length=50)
    image_de_couverture = models.ImageField(upload_to='couvertures/', null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    editeur = models.ForeignKey(Editeur, on_delete=models.SET_NULL, null=True)
    auteurs = models.ManyToManyField(Auteur)

    def __str__(self):
        return self.titre

class Exemplaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    etat = models.CharField(max_length=50, choices=[('Neuf', 'Neuf'), ('Bon', 'Bon'), ('Acceptable', 'Acceptable')])
    date_acquisition = models.DateField()
    localisation = models.CharField(max_length=100)
    disponibilite = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.livre.titre} - {self.etat}"

class Emprunt(models.Model):
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour_prevue = models.DateTimeField()
    date_retour_effective = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[('En cours', 'En cours'), ('Terminé', 'Terminé'), ('En retard', 'En retard')])
    remarques = models.TextField(null=True, blank=True)

class Commentaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    visible = models.BooleanField(default=True)
    modere = models.BooleanField(default=False)

class Evaluation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    commentaire = models.TextField(null=True, blank=True)
    date_evaluation = models.DateTimeField(auto_now_add=True)
    recommande = models.BooleanField(default=False)
