from django.db import models
import datetime


class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        today=datetime.date.today()
        # add keys and values to errors dictionary for each invalid field
        for show in Show.objects.all():
            if postData['title'] == show.title:
                errors["title"] = "Show title already exist!"

        if len(postData['title']) < 1:
            errors["title"] = "Show title should be at least 1 characters"

        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"

        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"

        if postData['release_date'] >= str(today):
            errors["release_date"] = "Show release date should be in the past"
        return errors

    def update_validator(self, postData ,id_id):
        errors = {}
        today=datetime.date.today()
        for show in Show.objects.all():
            if show.id == id_id: 
                if postData['title'] == show.title:
                    pass
            else:
                if postData['title'] == show.title:
                    errors["title"] = "Show title already exist!"
        # show_to_update = Show.objects.filter(title=postData['title'])
        # if len(show_to_update) > 0 and show_to_update['id'] != id_id:
        #     errors["title"] = "Show title already exist!"



        if len(postData['title']) < 1:
            errors["title"] = "Show title should be at least 1 characters"

        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"

        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"

        if postData['release_date'] >= str(today):
            errors["release_date"] = "Show release date should be in the past"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    desc = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=showManager()