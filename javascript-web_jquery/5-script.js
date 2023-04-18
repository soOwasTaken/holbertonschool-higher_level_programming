$(function () {
  $("#add_item").click(function () {
    const li = $("<li>Item</li>");
    $("UL.my_list").append(li);
  });
});
