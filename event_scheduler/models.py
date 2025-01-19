from django.db import models


class Performer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "出演者"


class Place(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "場所"


class Event(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    performer = models.ForeignKey(Performer, blank=True, null=True, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "イベント"
