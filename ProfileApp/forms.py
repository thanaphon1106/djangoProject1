from django.forms import *

class ProductForm(Form):
    BRANDLIST = [('PEAK','PEAK'),('Nike','Nike'),('Jordan','Jordan')]
    NAMELIST = [('name1','name1'),('name2','name2')]
    id = CharField(label="รหัสสินค้า", widget=TextInput(attrs={"size":"15"}))
    name = ChoiceField(label="ชื่อสินค้า", widget=Select,choices=NAMELIST)
    brand = ChoiceField(label="แบรนด์", widget=RadioSelect(attrs={"size": "15"}),choices=BRANDLIST)
    price = FloatField(label="ราคา", widget=TextInput(attrs={"size": "15"}))
    amount = IntegerField(label="จำนวน", widget=TextInput(attrs={"size": "15"}))
    detail = CharField(label="รายละเอียด", widget=Textarea(attrs={"size": "15"}))
