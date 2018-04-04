
$(document).ready(function(){

  // ANIMATEDLY DISPLAY THE NOTIFICATION COUNTER.
  //$('#noti_Counter')
  //    .css({ opacity: 0 })
  //    .text('7')              // ADD DYNAMIC VALUE (YOU CAN EXTRACT DATA FROM DATABASE OR XML).
  //    .css({ top: '-10px' })
  //    .animate({ top: '-2px', opacity: 1 }, 500);

  $('#noti_Button').click(function () {

      // TOGGLE (SHOW OR HIDE) NOTIFICATION WINDOW.
      $('#notifications').fadeToggle('fast', 'linear', function () {
          if ($('#notifications').is(':hidden')) {
            //do something
          }
          //else $('#noti_Button').css('background-color', '#FFF'); // CHANGE BACKGROUND COLOR OF THE BUTTON.
      });

      //$('#noti_Counter').fadeOut('slow'); // HIDE THE COUNTER.

      return false;
  });
// HIDE NOTIFICATIONS WHEN CLICKED ANYWHERE ON THE PAGE.
  $(document).click(function () {
      $('#notifications').hide();
  });

  $('#notifications').click(function () {
      return false;       // DO NOTHING WHEN CONTAINER IS CLICKED.
  });

  (function($) {
  "use strict"
  // NAVIGATION
  var responsiveNav = $('#responsive-nav'),
    catToggle = $('#responsive-nav .category-nav .category-header'),
    catList = $('#responsive-nav .category-nav .category-list'),
    menuToggle = $('#responsive-nav .menu-nav .menu-header'),
    menuList = $('#responsive-nav .menu-nav .menu-list');

  catToggle.on('click', function() {
    menuList.removeClass('open');
    catList.toggleClass('open');
  });

  menuToggle.on('click', function() {
    catList.removeClass('open');
    menuList.toggleClass('open');
  });

  $(document).click(function(event) {
    if (!$(event.target).closest(responsiveNav).length) {
      if (responsiveNav.hasClass('open')) {
        responsiveNav.removeClass('open');
        $('#navigation').removeClass('shadow');
      } else {
        if ($(event.target).closest('.nav-toggle > button').length) {
          if (!menuList.hasClass('open') && !catList.hasClass('open')) {
            menuList.addClass('open');
          }
          $('#navigation').addClass('shadow');
          responsiveNav.addClass('open');
        }
      }
    }
  });

  //BEST BRAND SLICK

  $(".best-brand-slick").slick({
    infinite: true,
    speed: 500,
    fade: true,
    cssEase: 'linear'
  })

   $(".slideshow-block").slick({
        infinite: true,
        mobileFirst:true,

        responsive: [{
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 1024,
        settings: {
          arrows: true,
          slidesToShow: 3,
          slidesToScroll: 3,
        }
      },
    ]

  })

  // HOME SLICK
  $('#home-slick').slick({
    autoplay: true,
    infinite: true,
    speed: 300,
    arrows: true,
  });

   $(".latest-auctions-slick").slick({
     infinite: true,
        mobileFirst:true,

        responsive: [{
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 1024,
        settings: {
          arrows: true,
          slidesToShow: 3,
          slidesToScroll: 3,
        }
      },
    ]

   })


  // PRODUCTS SLICK
  $('#product-slick-1').slick({
    slidesToShow: 3,
    slidesToScroll: 3,
    autoplay: true,
    infinite: true,
    speed: 300,
    dots: true,
    arrows: false,
    appendDots: '.product-slick-dots-1',
    responsive: [{
        breakpoint: 991,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 480,
        settings: {
          dots: false,
          arrows: true,
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      },
    ]
  });

  $('#product-slick-2').slick({
    slidesToShow: 3,
    slidesToScroll: 2,
    autoplay: true,
    infinite: true,
    speed: 300,
    dots: true,
    arrows: false,
    appendDots: '.product-slick-dots-2',
    responsive: [{
        breakpoint: 991,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 480,
        settings: {
          dots: false,
          arrows: true,
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      },
    ]
  });

  // PRODUCT DETAILS SLICK
  $('#product-main-view').slick({
    infinite: true,
    speed: 300,
    dots: false,
    arrows: true,
    fade: true,
    asNavFor: '#product-view',
  });

  $('#product-view').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    centerMode: true,
    focusOnSelect: true,
    asNavFor: '#product-main-view',
  });

  // PRODUCT ZOOM
  //$('#product-main-view .product-view').zoom();

  // PRICE SLIDER
  //var slider = document.getElementById('price-slider');
  //if (slider) {
  //  noUiSlider.create(slider, {
  //    start: [1, 999],
  //    connect: true,
  //    tooltips: [true, true],
  //    format: {
  //      to: function(value) {
  //        return value.toFixed(2) + '$';
  //      },
  //      from: function(value) {
  //        return value
  //      }
  //    },
  //    range: {
  //      'min': 1,
  //      'max': 999
  //    }
  //  });
  //}
})(jQuery);
})

