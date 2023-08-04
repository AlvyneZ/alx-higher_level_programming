// Adding a <li> element to a list when the user clicks on the
//  tag DIV#add_item

$('#add_item').on('click', function () {
  const nitem = $('<li>item</li>');

  $('ul.my_list').append(nitem);
});
