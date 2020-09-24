$(document).ready(() => {
  function update () {
    const lang = $('input#language_code').val();
    $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${lang}`, (data) => {
      $('div#hello').html(data.hello);
    });
  }
  $('input#btn_translate').click(update);
  $('input#language_code').keyup((e) => {
    if (e.keyCode === 13) update();
  });
});
