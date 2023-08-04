// Fetching the character name from this URL:
//  https://swapi-api.alx-tools.com/api/people/5/?format=json
//  and displaying it in DIV#character

$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.get(url, function (data) {
    const name = data.name;

    $('#character').text(name);
  });
});
