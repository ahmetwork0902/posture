from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    date_from = models.DateTimeField(auto_now = True)
    date_to = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.username

class Sessions(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
    date_from = models.DateTimeField(auto_now = True)
    date_to = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_id

class Wrong_pose(models.Model):
    session_id = models.ForeignKey('Sessions', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.session_id

class Users_achievements(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
    achievement_id = models.IntegerField('Achievements')
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_id

class Achievements(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name