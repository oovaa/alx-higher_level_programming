$(document).ready(() => {
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        success: (response) => {
            $('DIV#hello').text(response.hello);
        }
    });
});