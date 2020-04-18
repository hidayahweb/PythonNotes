class NortelIpSwitch(models.Model):
    ipMgmt = models.CharField(max_length=200)
    buildingName = models.CharField(max_length=200)
    typeSwitch = models.CharField(max_length=200)

    def __str__(self):
        return self.ipMgmt
    
class NortelCustomer(models.Model):
    ipUplink = models.ForeignKey(NortelIpSwitch, on_delete=models.CASCADE)
    port = models.IntegerField()
    tdi = models.IntegerField()

# Method 1:
NortelCustomer.objects.values('id','ipUplink__ipMgmt').all()
NortelCustomer.objects.values('id','ipUplink__ipMgmt').filter(ipUplink__ipMgmt='10.1.255.105')
# how to get primary key
datas_select = NortelCustomer.objects.get(id=id_edit)
print(datas_select.ipUplink.buildingName) #summon coloumn building name in related ip uplink


# Method 2:
NortelCustomer.objects.all().prefetch_related('ipUplink')
a = NortelCustomer.objects.all().prefetch_related('ipUplink')
for x in a:
    x.ipUplink.buildingName
    x.ipUplink.ipMgmt


# Method 3:
NortelCustomer.objects.all().select_related('ipUplink')
