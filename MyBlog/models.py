import uuid

from django.db import models


# Create your models here.
class SysUser(models.Model):
    MAN = 'M'
    WOMAN = 'F'
    SECRECY = 'S'
    SEX_IN_SYS_USER_CHOICES = (
        (MAN, "Man"),
        (WOMAN, "Woman"),
        (SECRECY, "Secrecy"),
    )

    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserID = models.CharField(max_length=32)
    Token = models.CharField(max_length=32)
    PassWord = models.CharField(max_length=50)
    UserName = models.CharField(max_length=40)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=1, choices=SEX_IN_SYS_USER_CHOICES, default=SECRECY)
    Card = models.CharField(max_length=18)
    BirthDay = models.DateField()
    Adress = models.CharField(max_length=120)
    Email = models.EmailField()
    Phone = models.CharField(max_length=11)

    def __str__(self):
        return self.UserID


class ForumQuestions(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    QuestionTitle = models.CharField(max_length=50)
    AuthorID = models.ForeignKey('MyBlog.SysUser', on_delete=models.CASCADE, related_name="User")
    Content = models.TextField()
    Pub_Date = models.DateTimeField(auto_now_add=True)
    Opt_Date = models.DateTimeField(auto_now=True)
    IsSolve = models.IntegerField()
    IsClose = models.IntegerField()
    TagID = models.ManyToManyField("MyBlog.Tags")

    def __str__(self):
        return self.QuestionTitle


class Tags(models.Model):
    Name = models.CharField(max_length=10)
    Pub_Date = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField()

    def __str__(self):
        return self.Name


class ForumReplys(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    QuestionID = models.ForeignKey('MyBlog.ForumQuestions', on_delete=models.CASCADE, related_name='Question')
    Content = models.TextField()
    Pub_Date = models.DateTimeField(auto_now_add=True)
    Opt_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Content
