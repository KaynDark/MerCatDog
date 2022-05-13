$("#btn-buscar").click(function (event) {
  event.preventDefault();

  $.ajax({
    url: "ttps://api.thecatapi.com/v1/images/search",
    data: {
      format: 'json',
    },
    error: function () {
      $("#info").html("<p>Ha ocurrido un error!!!! Vuelva a intentarlo</p>");
    },
    dataType: 'json',
    success: function (data) {
      $("#info").empty();
      console.log(data);
      var $nombre_gato = $("<h1>").text(data[0].categories.name);
      var $img_gato = $("<p><img src='" + data[0].breeds.url + "'>");
      
      $("#info")
        .append($nombre_gato)
        .append($img_gato);
    },
  });
});
