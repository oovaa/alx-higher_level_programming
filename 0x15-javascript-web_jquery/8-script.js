$(document).ready(() => {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: (response) => {

            response.results.forEach((film) => {
                $('ul#list_movies').append(`<li>${film.title}</li>`);
            });
        },
        error: (xhr, status, error) => {
            console.error(xhr.responseText);
        }
    });
});