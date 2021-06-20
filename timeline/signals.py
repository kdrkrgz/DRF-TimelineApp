from django.contrib.auth.models import User
from timeline.models import UserProfile, TimeLineMessage
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwars):
    """
    Create user profile after save user.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserProfile)
def create_join_message(sender, instance, created, **kwargs):
    """
    Create user join message.
    """
    if created:
        TimeLineMessage.objects.create(
            user_profile=instance,
            message="Hey! artık bende timeline kullanıyorum."
        )
