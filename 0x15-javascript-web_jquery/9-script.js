// Fetching from https://fourtonfish.com/hellosalut/?lang=fr and displaysing
//  the value of hello from that fetch in the HTML tag DIV#hello

$(document).ready(function () {
  const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';

  $.ajax({
    url: apiUrl,
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      const translation = data.hello;
      $('#hello').text(translation);
    },
    error: function () {
      $('hello').text('Failed to fetch the transaltion.');
    }
  });
});
