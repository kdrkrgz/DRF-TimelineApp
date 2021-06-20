from django.db import models
from django.contrib.auth.models import User
from timeline.basemodel import BaseModel


class UserTeam(BaseModel):
    team_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    team_image = models.ImageField(
        null=True, blank=True, upload_to=f'team_images/%Y/%m')

    def __str__(self):
        return self.team_name

    def save(self, image=None, *args, **kwargs):
        image = self.team_image
        return super().save(image, *args, **kwargs)

    class Meta:
        verbose_name = "Takım"
        verbose_name_plural = "Takımlar"


class UserProfile(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user")
    team = models.ForeignKey(
        UserTeam, on_delete=models.CASCADE, null=True, related_name="team")
    biography = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=63, blank=True)
    photo = models.ImageField(null=True, blank=True,
                              upload_to=f'profile_photos/%Y/%m')

    def __str__(self):
        return self.user.username

    def save(self, image=None, *args, **kwargs):
        image = self.photo
        return super().save(image, *args, **kwargs)

    class Meta:
        verbose_name = "Kullanıcı Profili"
        verbose_name_plural = "Kullanıcı Profilleri"


class TimeLineMessage(BaseModel):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="userprofile")
    message = models.CharField(max_length=200)
    message_image = models.ImageField(
        null=True, blank=True, upload_to=f'message_images/%Y/%m')

    def __str__(self):
        return f'{self.user_profile.user.username} - {self.message}'

    def save(self, image=None, *args, **kwargs):
        image = self.message_image
        return super().save(image, *args, **kwargs),

    class Meta:
        verbose_name = "Durum Mesajı"
        verbose_name_plural = "Durum Mesajları"
