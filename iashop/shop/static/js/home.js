/**
 * Created by JUSTICE on 7/22/2017.
 */

//$(document).ready(function(){
//    var owl = $(".owl-carousel")
//    owl.owlCarousel({
//        items:1,
//        loop:true,
//        margin:10,
//        autoplay:true,
//        autoplayTimeout:4000,
//        autoplaySpeed: 5000,
//        autoplayHoverPause:true,
//        animateOut: 'fadeOut',
//        animateIn: 'fadeIn',
//
//    })
//});

//var form_options = {target: "#modal", success: function(response){}};
//$('#modal').ajaxForm(form_options)

//var form_options = { target: '#modal2', success: function(response) {} };
//    $('#modal2').ajaxForm(form_options);




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



//$(".follow").click(function(e){
//    //alert("Hello")
//    e.preventDefault()
//     //alert($.post('{% url "user_follow" %}),
//    $.post('{% url "follow" %}',
//        {
//            id: $(this).data('id'),
//            action: $(this).data('action')
//        },
//        function(data){
//            alert(data['status']=='ok')
//        }
//
            //if (data['status']=='ok'){
            //    var prev_action = $('.follow').data('action');
            //
            //    //toggle data action
            //    $('.follow').data('action',
            //    prev_action == 'follow' ? 'unfollow': 'follow');
            //
            //    //toggle text
            //
            //    $('.follow').text(
            //        prev_action == 'follow' ? 'unfollow' : 'follow');
            //
            //    //update total followers
            //
            //    var previous_followers = parseInt(
            //        $('span.count .total').text()
            //    );
            //    $('span.count .total').text(prev_action == 'follow' ?
            //    previous_followers + 1 : previous_followers - 1);
//            //}
//        //}
//    )
//})


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
        distance = newDate - now
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        $(this).find(".days").text(days)
        $(this).find(".hours").text(hours)
        $(this).find(".minutes").text(minutes)
        $(this).find(".seconds").text(seconds)
    })



},1000)




//Counter js

