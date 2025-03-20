from django.db import models
from django.utils.translation import gettext_lazy as _

# ^ this is used to translate the curencys from one to another ^
from django.contrib.postgres import fields as PostgresFields


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{} - {}".format(self.name, self.description)


class Provider(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):

    class Curency(models.TextChoices):
        USD = ("USD", _("United States Dollar"))
        EUR = ("EUR", _("Euro"))
        JOD = ("JOD", _("Jordanian Dinar"))

    name = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512, blank=True)
    Provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )

    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    curency = models.CharField(
        max_length=3,
        choices=Curency.choices,
        default=Curency.JOD,
    )

    variation_porduct_id = PostgresFields.ArrayField(
        models.IntegerField(null=True, blank=True),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.Provider.name} - {self.Provider}"
