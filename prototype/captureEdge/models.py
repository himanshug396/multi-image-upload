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
    id = models.AutoField(primary_key=True, unique=True)
    claim_id = models.ForeignKey(Claim, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=10, blank=False, help_text='Must be a 10 digit number')
    def __str__(self):
        return str(self.claim_id) + '_' + self.name + '_' + str(self.phone)
    class Meta:
        unique_together = ('claim_id', 'phone')

def content_file_name(instance, filename):
    return '/'.join(['media', 'claim_id_' + str(instance.claim_id.id), filename])

class Photo(BaseModel):
    id = models.AutoField(primary_key=True)
    claim_id = models.ForeignKey(Claim, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=False, help_text='Must be a 10 digit number')
    photo = models.ImageField(upload_to=content_file_name, verbose_name='Photo', height_field=None, width_field=None)
    def __str__(self):
        return str(self.phone) + '_' + str(self.id)
