from django.db import models


class User(models.Model):
    login = models.CharField(max_length=150)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.login,
                                     self.email,
                                     self.age)


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_cnt = models.IntegerField()
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.product_name,
                                     self.product_cnt,
                                     self.is_available)


class Cart(models.Model):
    user_mail = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count_id = models.IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.user_mail,
                                     self.product_id,
                                     self.product_count_id)
