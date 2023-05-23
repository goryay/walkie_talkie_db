from django.db import models
from state.models import State
from organization.models import Organization
from post.models import Post
from resposible.models import Resposible
from walkie_talkie.models import WalkieTalkie


class Accounting(models.Model):
    id = models.AutoField(primary_key=True)
    id_walkie_talkie = models.ForeignKey(WalkieTalkie, on_delete=models.CASCADE)
    id_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    id_resposible = models.ForeignKey(Resposible, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_state = models.ForeignKey(State, on_delete=models.CASCADE)
    relevance = models.BooleanField('Актуальность', default=False)
    document = models.CharField('Документ подтверждающий приём на себя рацию', max_length=380)
    date = models.DateTimeField('Дата')
    comments = models.TextField('Комментарий')

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return f'/accounting/{self.id}'

    class Meta:
        verbose_name = 'Учёт'
        verbose_name_plural = 'Учёт'
