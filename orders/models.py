from django.db import models
from customers.models import Customer
from prodect.models import Products

# Part 2.4 order model
class Cart(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE=0
    ORDER_PROCESSED=1
    DELIVERED=2
    REJECTED=3
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (DELIVERED,"DELIVERED"),
                   (REJECTED,"REJECTED")
                   )
    orederstatus=models.IntegerField(choices=STATUS_CHOICE,default=0)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='order')
    name=models.CharField(max_length=50,null=False)
    place=models.CharField(null=False)
    address=models.CharField(null=False)
    email=models.EmailField(null=False)
    phonenumber=models.IntegerField(default=0)
    city=models.CharField(null=False)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self) -> str:
        return "orders-{}-{}".format(self.id,self.owner)


# Part 2.3 cart model
class CartItems(models.Model):
    product=models.ForeignKey(Products,related_name='addcart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='added')