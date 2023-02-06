from django.db import models


class Product:
    def __init__(self, id, name, brand, price, amount, detail, total, discount, net):
        self.id=id
        self.name=name
        self.brand=brand
        self.price=price
        self.amount=amount
        self.detail=detail
        self.total=total
        self.discount = discount
        self.net=net
