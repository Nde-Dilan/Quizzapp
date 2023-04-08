from django.db import models
# Differentes categories, tu peux en ajouter idem pour les niveaux tu peux les modifier
categorie_choix = (("Science",'Science'),
                ("Litterature",'Litterature'),
                ("Informatique",'Informatique'),
                ("Mythologie",'Mythologie'))

niveau_choix = (("Expert",'Expert+'),
                ("Difficile",'Difficile'),
                ("Normal",'Normal'),
                ("Facile",'Facile'))

# Create your models here.

class Quizz(models.Model):
    title = models.CharField(max_length=150)
    images = models.ImageField(upload_to="Media", null=True)
    niveau = models.CharField(choices=niveau_choix,max_length=50)
    nbr_px = models.IntegerField()
    def __str__(self):
        return self.title
    
class Question(models.Model):
    quizz=models.ForeignKey(Quizz,null=True,on_delete=models.PROTECT)
    # Plusieurs questions appartiennent à un quizz
    categorie = models.CharField(choices=categorie_choix,max_length=90)
    question = models.TextField(null=False,default="Jattends vos questions...")
    nbr_points = models.IntegerField()
    def __str__(self):
        return self.question


class Proposition(models.Model):
    # Plusieurs propositions appartiennent à une question
    proposition = models.CharField(max_length=5000)
    question = models.ForeignKey(Question,on_delete=models.PROTECT)
    def __str__(self):
        return self.proposition

# print(Question.objects.)