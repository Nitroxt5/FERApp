$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  let $this = $(this),
    label = $this.prev('label');

  if (e.type === 'keyup') {
    if ($this.val() === '') {
      label.removeClass('active highlight');
    } else {
      label.addClass('active highlight');
    }
  } else if (e.type === 'blur') {
    if($this.val() === '') {
      label.removeClass('active highlight');
    } else {
      label.removeClass('highlight');
    }
  } else if (e.type === 'focus') {
    if($this.val() === '') {
      label.removeClass('highlight');
    } else if($this.val() !== '') {
      label.addClass('highlight');
    }
  }
});

$('.tab a').on('click', function (e, clear_msg = true) {

  e.preventDefault();

  const token = $('input[name="csrfmiddlewaretoken"]').val();

  $('input').val('');
  $('label').removeClass('active highlight');
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  if (clear_msg) {
    if (target === '#signin') {
      $('#reg_err').html('');
    } else if (target === '#signup') {
      $('#log_err').html('');
    }
  }

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

  $('input[name="csrfmiddlewaretoken"]').val(token);

});

$('#id_reg_password, #id_reg_confirm_password').on('keyup', function () {
  if ($('#id_reg_password').val() == '' && $('#id_reg_confirm_password').val() == '') {
    $('#reg_button').prop('disabled', false).css('opacity', '1');
    $('#reg_err').html('');
  } else if ($('#id_reg_password').val() == $('#id_reg_confirm_password').val()) {
    $('#reg_button').prop('disabled', false).css('opacity', '1');
    $('#reg_err').html('Passwords match');
  } else {
    $('#reg_button').prop('disabled', true).css('opacity', '.5');
    $('#reg_err').html('Passwords do not match');
  }
});
