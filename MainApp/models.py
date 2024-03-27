from django.db import models

class ClientServiceProvider(models.Model):
    # Client details
    client_comp_name = models.CharField(max_length=120)
    client_gst = models.CharField(max_length=50)
    client_igst = models.SmallIntegerField()
    client_sgst = models.SmallIntegerField()
    client_phone = models.CharField(max_length=20)
    client_email = models.EmailField()
    client_country = models.CharField(max_length=50)
    client_state = models.CharField(max_length=50)
    client_other_info = models.TextField()

    # Service provider details
    provider_comp_name = models.CharField(max_length=120)
    provider_name = models.CharField(max_length=100)
    provider_acc_no = models.CharField(max_length=100)
    provider_bank_name = models.CharField(max_length=100)
    provider_ifsc = models.CharField(max_length=50)
    provider_gst = models.CharField(max_length=50)
    provider_phone = models.CharField(max_length=20)
    provider_mail = models.EmailField()
    provider_other_info = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Client: {self.client_comp_name}, Id: {self.id}"
    

class Services(models.Model):

    assigne_to = models.ForeignKey(ClientServiceProvider, on_delete=models.CASCADE)
    service_description = models.TextField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.service_description} - {self.quantity}"
