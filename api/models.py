from django.db import models

# Create your models here.
class btn(models.Model):
    is_on =  models.BooleanField()

    def __str__(self):
        return self.is_on

    # def save(self, *args, **kwargs):
    #     if self.is_on:
    #         try:
    #             temp = switch.objects.get(is_on=True)
    #             if self != temp:
    #                 temp.is_on = False
    #                 temp.save()
    #         except switch.DoesNotExist:
    #             pass
    #     super(switch, self).save(*args, **kwargs)