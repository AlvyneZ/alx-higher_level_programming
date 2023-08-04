// Updating the text color of the <header> element to red (#FF0000)
//  without JQuery while being imported from document head

document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');

  header.style.color = '#FF0000';
});
