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
			} 
      else if($this.val() !== '') {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {
  
  e.preventDefault();

  $('input').val('');
  $('label').removeClass('active highlight');
  $('#err_msg').html('');
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});

$('#password, #confirm_password').on('keyup', function () {
  $('#err_msg').addClass('highlight').css('left', '0')
  if ($('#password').val() == '' && $('#confirm_password').val() == '') {
    $('#reg_button').prop('disabled', false).css('opacity', '1');
    $('#err_msg').html('');
  } else if ($('#password').val() == $('#confirm_password').val()) {
    $('#reg_button').prop('disabled', false).css('opacity', '1');
    $('#err_msg').html('Passwords match');
  } else {
    $('#reg_button').prop('disabled', true).css('opacity', '.5');
    $('#err_msg').html('Passwords does not match');
  }
});