$('DIV#toggle_header').click(function () {
    var header = $('header');
    if (header.hasClass('red')) {
        header.removeClass('red').addClass('green');
    } else if (header.hasClass('green')) {
        header.removeClass('green').addClass('red');
    }
});