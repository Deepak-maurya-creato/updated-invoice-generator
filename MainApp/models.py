from django.db import models

class ClientServiceProvider(models.Model):
    # Client details
    client_comp_name = models.CharField(max_length=120)
    client_gst = models.CharField(max_length=50)
    client_phone = models.CharField(max_length=20)
    client_email = models.EmailField()
    client_country = models.CharField(max_length=50)
    client_state = models.CharField(max_length=50)
    client_pin = models.CharField(max_length=20)
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
        return f"Client Name/Company: {self.client_comp_name} - Provider: {self.provider_comp_name} - created_at: {self.created_at}"
