$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('div#hello').text(data.hello);
});
