from django.db import models

# -*- coding: utf-8 -*-


class Payment(models.Model):
    is_paid = models.BooleanField(default=False)
    payment_agent = models.CharField(max_length=30)

    # WHAT?!
    def get_payment_agent(self):
        """
        A monkey patch to get payment agent. Now is it store in the special field in the database. This method is deprecated and is used for backwards compatibility.

        .. deprecated:: r574
        """
        if not self.is_paid:
            return "-"

        if self.payment_agent:
            return self.payment_agent

        if self.provider1.filter(type=1).count():
            self.payment_agent = "Provider1"
        elif self.qprovider2.filter(type=1).count():
            self.payment_agent = "AO Provider2"
        elif self.provider3.filter(type=1).count():
            self.payment_agent = "Provider3"
        elif self.provider4.count():
            self.payment_agent = "Complex Provider 4 Name With Surname"
        else:
            self.payment_agent = "Provider5 Full Company-Name"

        self.save()
        return self.payment_agent
