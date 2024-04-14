from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )
    followers_count = models.IntegerField(
        default=0,
    )

    def increment_followers(self):
        self.followers_count += 1
        self.save()

#
# # Create
# a = Author(first_name='Kostadin', last_name='Tashev')
#
# # Update
# a.first_name = 'Kostadin'
#
# # Delete
# a.delete()
#
# # Read
# a
#
# # Action
# a.increment_followers()
