$(function () {
  console.log("Fetching translation...");
  $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    $("#hello").text(data.hello);
  });
});
