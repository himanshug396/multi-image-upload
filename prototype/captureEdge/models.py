from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Claim(BaseModel):
    id =  models.AutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id) + '_' + self.description

class Phone(BaseModel):
    id = models.AutoField(primary_key=True)
    claim_id = models.ForeignKey(Claim, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=13, blank=False, help_text='Must be a 10 digit number')
    def __str__(self):
        return str(self.claim_id) + '_' + self.name + '_' + str(self.phone)

class Photo(BaseModel):
    id = models.AutoField(primary_key=True)
    claim_id = models.ForeignKey(Claim, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return str(self.phone) + '_' + str(self.id)
