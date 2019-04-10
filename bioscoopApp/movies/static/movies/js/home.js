$(document).ready(function () {

    //gestion of the navigation layout

    $('nav .trending').addClass("navColor");
    console.log("js working")

    var newDistance = $('#new').offset().top;
    var bestRatedDistance = $('#bestRated').offset().top;
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
});

function changeHighlight(highlight) {
    switch (highlight) {
        case 'new':
            $('nav .trending').removeClass("navColor");
            $('nav .new').addClass('navColor');
            $('nav .bestRated').removeClass('navColor');
            break;

        case 'trending':
            $('nav .trending').addClass("navColor");
            $('nav .new').removeClass('navColor');
            break;

        case 'bestRated':
            $('nav .new').removeClass('navColor');
            $('nav .bestRated').addClass('navColor');
            $('nav .upcomming').removeClass('navColor');
            break;

        case 'upcomming':
            $('nav .bestRated').removeClass('navColor');
            $('nav .upcomming').addClass('navColor');
            break;

        default:
            break;
    }
}
