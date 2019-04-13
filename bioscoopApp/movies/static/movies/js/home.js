$(document).ready(function () {

    //gestion of the navigation layout

    $('nav .trending').addClass("navColor");
    console.log("js working")

    var newDistance = $('#new').offset().top-1;
    var bestRatedDistance = $('#bestRated').offset().top-1;
    var upcommingDistance = $('#upcomming').offset().top - 1;

    $(window).scroll(function () {
        if ($(this).scrollTop() < newDistance) {
            changeHighlight('trending')
        }
        if ($(this).scrollTop() >= newDistance && $(this).scrollTop() < bestRatedDistance) {
            changeHighlight('new')
            //$('nav .new').addClass('navColor');
        } if ($(this).scrollTop() >= bestRatedDistance && $(this).scrollTop() < upcommingDistance) {
            changeHighlight('bestRated')
        } if ($(this).scrollTop() >= upcommingDistance) {
            changeHighlight('upcomming')
        }
    });

    //toggle the visibility of favorite and log out icon
    var toggle = true;
    document.getElementById('hamburger').addEventListener('click',function () { 
        if (toggle) {
            $('.menuIcons').fadeIn(500);
            console.log('visible')
        } else {
            $('.menuIcons').fadeOut(300);
            console.log('invisible')
        }
        toggle = !toggle;
    })

    $('.exit').click(function() {
        location.assign('./logout');
    })

    $('.favorite').click(function() {
        location.assign('./favorites');
    })

    $('.ticket').click(function() {
        location.assign('./screenings');
    })


});

function changeHighlight(highlight) {
    switch (highlight) {
        case 'new':
            $('nav .trending').removeClass("navColor");
            $('nav .new').addClass('navColor');
            $('nav .bestRated').removeClass('navColor');
            $('nav .upcomming').removeClass('navColor');
            $('nav').css("background-color","#2A9D8F");
            break;

        case 'trending':
            $('nav .trending').addClass("navColor");
            $('nav .new').removeClass('navColor');
            $('nav .bestRated').removeClass('navColor');
            $('nav .upcomming').removeClass('navColor');
            $('nav').css("background-color","#264653");
            break;

        case 'bestRated':
            $('nav .trending').removeClass("navColor");
            $('nav .new').removeClass('navColor');
            $('nav .bestRated').addClass('navColor');
            $('nav .upcomming').removeClass('navColor');
            $('nav').css("background-color","#E9C46A");
            break;

        case 'upcomming':
            $('nav .trending').removeClass("navColor");
            $('nav .new').removeClass('navColor');
            $('nav .bestRated').removeClass('navColor');
            $('nav .upcomming').addClass('navColor');
            $('nav').css("background-color","#F4A261");
            break;

        default:
            break;
    }
}
