$(document).ready(function() {
  $('input#input_text, textarea#textarea2').characterCounter();
});

M.textareaAutoResize($('#textarea1'));

$(document).ready(function() {
  M.updateTextFields();
});
