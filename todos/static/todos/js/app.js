$(document).ready(function() {
  $('.action-link').on('click', function() {
    var form = $(this).closest('form'),
        url = this.href;

    form.attr('action', url);
    form.submit();
  });
});
