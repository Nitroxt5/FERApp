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
  $('#id_image').trigger('change');
  $('label').removeClass('active highlight');
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  if (clear_msg) {
    if (target === '#profile') {
      $('#upload_err').html('');
    } else if (target === '#recognize') {
      $('#change_err').html('');
    }
  }

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

  $('input[name="csrfmiddlewaretoken"]').val(token);

});

$('#id_image').on('change', function (e) {

  if (!('files' in $(this)[0])) {
    $('#loaded-file').html('File not selected');
    return;
  }

  if ($(this)[0].files.length == 0) {
    $('#loaded-file').html('File not selected');
  } else {
    let filename = $(this)[0].files[0].name;
    if (filename.length > 15) {
      filename = filename.slice(0, 15) + '...';
    }
    $('#loaded-file').html(filename);
  }

});
