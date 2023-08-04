// Fetching a list of the title for all movies by using this URL:
//  https://swapi-api.alx-tools.com/api/films/?format=json
//  and listing them in UL#list_movies

$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function (data) {
    const movielists = data.results;

    $.each(movielists, function (index, movielist) {
      const title = movielist.title;
      const listitem = $('<li>').text(title);

      $('#list_movies').append(listitem);
    });
  });
});
