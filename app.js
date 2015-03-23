var main = function() {
  $('.description').hide();

  $('.movie-title').click(function() {
    alert('test');
    $('.description').show();
  });
}

$(document).ready(main);