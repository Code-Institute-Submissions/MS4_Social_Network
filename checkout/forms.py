from django import forms
from datetime import datetime

year = int(datetime.now().strftime("%Y"))


class MakePaymentForm(forms.Form):
    """
    Input for Strip Payment Collection
    Default Expiration Year Range to current Year
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(year, year + 20)]

    credit_card_number = forms.CharField(label='Credit Card Number', required=True)
    ccv = forms.CharField(label="Security Code", required=True)
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES, required=True)
