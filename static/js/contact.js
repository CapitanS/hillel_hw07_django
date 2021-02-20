$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-message .modal-content").html("");
        $("#modal-message").modal("show");
      },
      success: function (data) {
        $("#modal-message .modal-content").html(data.html_form);
      }
    });
  };

  var sendForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-message .modal-content").html(data.html_contact_send);
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Open contact form
  $(".js-send-message").click(loadForm);
  // Send message
  $("#modal-message").on("submit", ".js-contact-create-form", sendForm);

});