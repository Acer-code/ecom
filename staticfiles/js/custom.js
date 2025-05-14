(function ($) {
  
    "use strict";
  
      $('.slick-slideshow').slick({
        autoplay: true,
        infinite: true,
        arrows: true,
        fade: true,
        dots: false,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              infinite: true,
              dots: false
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });
  
      $('.slick-testimonial').slick({
        arrows: true,
        dots: false,
      });
      
    })
    
    (window.jQuery);

    // brand-slider-start
    jQuery(document).ready(function($) {
      $('.testimonial').slick({
        dots: false,
        infinite: true,
        speed: 3000,
        slidesToShow: 4,
        slidesToScroll: 2,
        autoplay: true,
        autoplaySpeed: 0,
        cssEase: 'linear',
        arrows: false,
        responsive: [{
          breakpoint: 600,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        },
        {
           breakpoint: 500,
           settings: {
              arrows: false,
              slidesToShow: 3,
              slidesToScroll: 1,
              centerMode: true,
              centerPadding: '50px'
           }
        }]
    });
});
    // brand-slider-end

    // certify-slider-start
    jQuery(document).ready(function($) {
      $('.testimonial2').slick({
        dots: false,
        infinite: true,
        speed: 3000,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 0,
        cssEase: 'linear',
        arrows: false,
        responsive: [{
          breakpoint: 600,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        },
        {
           breakpoint: 500,
           settings: {
              arrows: false,
              slidesToShow: 2,
              slidesToScroll: 1,
              centerMode: true,
              centerPadding: '20px'
           }
        }]
    });
});
    
    // certify-slider-end

    // exhibition-slider-start
    jQuery(document).ready(function($) {
      $('.testimonial3').slick({
        dots: false,
        infinite: true,
        speed: 3000,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 0,
        cssEase: 'linear',
        arrows: false,
        responsive: [
          {
            breakpoint: 991,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1
            }
          },
          {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
           breakpoint: 500,
           settings: {
              arrows: false,
              slidesToShow: 1,
              slidesToScroll: 1,
              centerMode: true,
              centerPadding: '20px'
           }
        }]
    });
}); 
// exhibition-slider-end

//whatsapp icon fixed
const whatsappWrapper = document.createElement('div');
whatsappWrapper.classList.add('whatsapp-wrapper','pulse');

const whatsappLink = document.createElement('a');
whatsappLink.href = 'tel:9212508582';
whatsappLink.target = '_blank';
whatsappLink.classList.add('whatsapp-icon');

whatsappWrapper.appendChild(whatsappLink);
document.body.appendChild(whatsappWrapper);
//whatsapp icon fixed end

// Contatc form submission using AJAX
    document.getElementById("contact-form").addEventListener("submit", function(event) {
      event.preventDefault();  // Prevent default redirection
  
      let form = event.target;
      let formData = new FormData(form);
      let statusMessage = document.getElementById("form-status");
  
      fetch(form.action, {
          method: form.method,
          body: formData,
          headers: { "Accept": "application/json" }
      })
      .then(response => response.json())
      .then(data => {
          if (data.ok) {
              statusMessage.innerText = "Thank you! We will contact you soon.";
              statusMessage.style.display = "block";  // Show thank-you message
              form.reset();  // Reset the form fields
              setTimeout(() => { statusMessage.style.display = "none"; }, 5000);  // Hide message after 5 sec
          } else {
              statusMessage.innerText = "Oops! Something went wrong.";
              statusMessage.style.color = "red";
              statusMessage.style.display = "block";
          }
      })
      .catch(error => {
          statusMessage.innerText = "There was a problem sending your message.";
          statusMessage.style.color = "red";
          statusMessage.style.display = "block";
      });
  });


