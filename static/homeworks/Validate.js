$( document ).ready(function() {

    $(document).on("click", ".payfor-options-item", function(event){
       var payforclass = document.getElementById("payfor-class-div");
       payforclass.className = "payfor payfor__active";

       ga('send', {
          hitType: 'event',
          eventCategory: 'Validate',
          eventAction: 'Payment',
          eventLabel: $(this)[0].id,
          transport: 'beacon'
        });

    });
});

// payfor-class-div
// validate-notsure-button