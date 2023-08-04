// Fetching and printing how to say “Hello” depending on the language

$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const langCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${langCode}/`;

    $.get(apiUrl, function (data) {
      const translation = data.hello;

      $('#hello').text(translation);
    }).fail(function () {
      $('#hello').text('Translation not found for the given language code.');
    });
  });
});
