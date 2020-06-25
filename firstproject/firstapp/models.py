from django.db import models


# Create your models here.
# class ProjectData(models.Model):
#     First_Name = models.CharField(max_length=20)
#     Last_Name = models.CharField(max_length=20)
#     Address = models.CharField(max_length=20)

class Customer(models.Model):
    Customer_id = models.UUIDField(max_length=20, primary_key=True)

    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Phone_Number = models.IntegerField(max_length=20)
    Email_ID = models.EmailField(max_length=20)
    address1 = models.CharField( max_length=20 )
    address1 = models.CharField( max_length=20 )
    zip_code = models.CharField( max_length=20 )
    city = models.CharField( max_length=20 )
    country = models.CharField( max_length=20 )


class FoodItem(models.Model):
    Food_id = models.UUIDField(max_length=20, primary_key=True)
    Food_Name = models.CharField(max_length=20)
    Price = models.IntegerField(max_length=20)
    Quantity = models.IntegerField(max_length=20)


    Item_Category = models.CharField(max_length=20)



class Order(models.Model):
    Order_ID = models.UUIDField(max_length=20, primary_key=True)

    Customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,)
    Food_id = models.ForeignKey(FoodItem,on_delete=models.CASCADE,)


    Total_Quantity = models.IntegerField(max_length=20)
    Total_Price = models.IntegerField(max_length=20)






class Menu(models.Model):
    Menu_id = models.UUIDField(max_length=20, primary_key=True)

    Food_Id = models.ForeignKey(FoodItem, on_delete=models.CASCADE,)

    Price = models.IntegerField(max_length=20)


class Payment(models.Model):
    Payment_id = models.UUIDField(max_length=20, primary_key=True)
    Customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,)
    Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE,)

    Time = models.IntegerField(max_length=20)
    Date = models.IntegerField(max_length=20)
    Payment_type = models.CharField(max_length=20)






