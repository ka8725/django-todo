$(document).ready(function() {
  $('.action-link').on('click', function() {
    var form = $(this).closest('form'),
        url = this.href,
        method = $(this).data('method');

    form.attr('action', url);
    form.attr('method', method);
    form.submit();
  });
});
