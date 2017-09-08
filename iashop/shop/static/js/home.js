/**
 * Created by JUSTICE on 7/22/2017.
 */

$(document).ready(function(){
    var owl = $("#carousel1")
    owl.owlCarousel({
        items:1,
        loop:true,
        margin:10,
        autoplay:true,
        autoplayTimeout:4000,
        autoplaySpeed: 5000,
        autoplayHoverPause:true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',

    })

    var owl2 = $("#carousel2, #carousel3")

    owl2.owlCarousel({
        items:5,
        loop:true,
        margin:10,
        autoplay:true,
        autoplayTimeout:4000,
        autoplaySpeed: 5000,
        autoplayHoverPause:true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',

    })



    //$('.cat-list').hover(function(){
    //    var el = $('#subcats');
    //    var username = $(this).data('action');
    //
    //
    //    //$.post("{% url 'auctions:select-by-category' %}",
    //    //    { username:username},
    //    //    function() {
    //    //        alert('I am working')
    //    //
    //    //    });
    //
    //    //)
    //    $(this).append(el)
    //    el.css('display', 'inline-block')
    //    el.css('position', 'absolute')
    //    el.css('z-index', '3')
    //},
    //    function(){
    //        //$( this ).find( '.sub-cat-on-hover:last' ).remove();
    //        $( this ).find( '#subcats' ).css('display', 'none')
    //    }
    //)





})








//var webrtc = new SimpleWebRTC({
//  // the id/element dom element that will hold "our" video
//  localVideoEl: 'localVideo',
//  // the id/element dom element that will hold remote videos
//  remoteVideosEl: 'remotesVideos',
//  // immediately ask for camera access
//  autoRequestMedia: true
//});
//
//// we have to wait until it's ready
//webrtc.on('readyToCall', function () {
//  // you can name it anything
//  webrtc.joinRoom('your awesome room name');
//});

//$('.carousel.carousel-slider').each(function() {
//var view = $(this);
//var firstImage = view.find('.carousel-item img').first();
//var imageHeight = firstImage[0].naturalHeight;
//if (imageHeight > 0) {
//view.css('height', imageHeight / firstImage[0].naturalWidth * view.width());
//}
//else {
//view.css('height', 400);
//}
//});
//$('.carousel.carousel-slider').carousel({fullWidth: true});

//
//$('button.test').click(function(){
//    $(this).text('Unfollow')
//})



////The User follow script here
//    $('.follow').click(function(e){
//        e.preventDefault()
//
//        $.post('{% url "user_follow" %}'),
//        {
//            id:$(this).data('id'),
//            action: $(this).data('action'),
//        }
//
//        alert($(this).data('action'))
//
//
//    })





//List and grid toggle function

$(document).ready(function() {
    $('#list').click(function(event){event.preventDefault();
    $('#products .item').addClass('list-group-item');});
    $('#grid').click(function(event){event.preventDefault();
    $('#products .item').removeClass('list-group-item');
    $('#products .item').addClass('grid-group-item');});
});


//var countDownDate = new Date("Jan 5, 2018 15:37:25").getTime();

var x = setInterval(function(){
    var now = new Date().getTime()
    $(".myClock").each(function(){
        var dates = $(this).data('action')
        var converted = parseInt(dates)
        var newDate = new Date(converted)
        var distance = newDate - now
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        $(this).find(".days").text(days)
        $(this).find(".hours").text(hours)
        $(this).find(".minutes").text(minutes)
        $(this).find(".seconds").text(seconds)


        if (distance < 0){
            $(this).find(".days").text(0)
            $(this).find(".hours").text(0)
            $(this).find(".minutes").text(0)
            $(this).find(".seconds").text(0)
        }
        //if (distance < 0){
        //    //clearInterval(x);
        //    (this).find("time-info").text("Finished")
        //}


    })





},1000)




//Counter js

