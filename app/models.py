from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Create your models here.
class Tag(BaseModel):
    name = models.CharField(
        max_length = 150,
        unique = True
    )

    class Meta:
        verbose_name = "Statu"

    def __str__(self) -> str:
        return self.name
    
class NumericData(BaseModel):
    data = models.CharField(
        max_length = 255,
        unique = True,
        verbose_name = "Donnée"
    )
    value = models.IntegerField()
    unit = models.CharField(
        max_length = 100, 
        null = True
    )

    class Meta:
        verbose_name = "Donnée"

    def __str__(self) -> str:
        return f"{self.data} : {self.value}"
    


class Question(BaseModel):
    content = models.TextField(
        blank = True,
        unique = True
    )

    tag_id = models.ForeignKey(Tag, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.content
    

class Answer(BaseModel):
    content = models.TextField(
        blank = True
    )
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Reponse"
    
    def __str__(self) -> str:
        return self.content
    
class AnswerNumericData(models.Model):
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE)
    numeric_data = models.ForeignKey(NumericData, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Reponses avec données numerique"
