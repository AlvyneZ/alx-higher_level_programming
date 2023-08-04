// Adding, removing and clearing LI elements from a list when
//  the user clicks

$(document).ready(function(){
  $('#add_item').on('click', function () {
    const newItem = $('<li>').text('Item');

    $('ul.my_list').append(newItem);
  });
  $('#remove_item').on('click', function () {
    $('ul.my_list li:last-child').remove();
  });
  $('#clear_list').on('click', function () {
    $('ul.my_list').empty();
  });
});
