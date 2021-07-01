// function for the comment button to hide or show comments
function commentReplyToggle(parent_id) {
    const row = document.getElementById(parent_id);

    if (row.classList.contains('d-none')) {
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

const searchInputDropdown = document.getElementById('search-input-dropdown');
const dropdownOptions = document.querySelectorAll('.input-group-dropdown-item');

searchInputDropdown.addEventListener('input', () => {
  const filter = searchInputDropdown.value.toLowerCase();
  showOptions();
  const valueExist = !!filter.length;

  if (valueExist) {
    dropdownOptions.forEach((el) => {
      const elText = el.textContent.trim().toLowerCase();
      const isIncluded = elText.includes(filter);
      if (!isIncluded) {
        el.style.display = 'none';
      }
    });
  }
});

const showOptions = () => {
  dropdownOptions.forEach((el) => {
    el.style.display = 'flex';
  })
}



// stripe

/* Payment collect javascript */
$(function () {

    /* submit payment button */
    $('#payment-form').submit(function () {
        console.log("TESTAR")
        //pull off card details
        var form = this;
        var card = {
            number: $('#id_credit_card_number').val(),
            expMonth: $('#id_expiry_month').val(),
            expYear: $('#id_expiry_year').val(),
            cvc: $('#id_ccv').val()
        };

        //submit to strip with secure token
        Stripe.createToken(card, function (status, response) {
            if (status == 200) {
                $('#credit-card-errors').hide();
                $('#id_stripe_id').val(response.id);

                //prevent the card details from being submitted to our server
                $('#id_credit_card_number').removeAttr('name');
                $('#id_ccv').removeAttr('name');
                $('#id_expiry_month').removeAttr('name');
                $('#id_expiry_year').removeAttr('name');
                form.submit()
            } else {
                //something went wrong, show error messaging.
                $('#stripe-error-message').text(response.error.message);
                $('#credit-card-errors').show();
                $('#validate_card_btn').attr('disabled', false);
            }
        });
        return false;
    });
});