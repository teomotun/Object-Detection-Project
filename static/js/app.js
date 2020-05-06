var dropzone = document.getElementById("dropzone");
var recorderr = document.getElementById("recorderr");
var icon_options = document.getElementById("icon_options");
var data = ["cups", "spoon", "knife"];

var recorderrclone = $("#recorderr").clone();
var icon_optionsclone = $("#icon_options").clone();

function image_up() {
  $("#icon_options").replaceWith(icon_optionsclone.clone());
  d3.select("#text_for_icon").text("UPLOAD IMAGE");
  $("#recorderr").empty();
}

function video_up() {
  $("#icon_options").replaceWith(icon_optionsclone.clone());
  d3.select("#text_for_icon").text("UPLOAD VIDEO");
  $("#recorderr").empty();
}

function video_stream() {
  //recorderr.disabled = false;
  $("#recorderr").replaceWith(recorderrclone.clone());
  $("#icon_options").empty();
}

function init() {
  image_up();
}

d3.select("#image_up").on("click", image_up);
d3.select("#video_up").on("click", video_up);
d3.select("#video_stream").on("click", video_stream);

init();

data.forEach((data) => {
  var drop = d3.select("#selDataset").append("option");
  drop.text(data.toUpperCase());
  drop.property("value", data);
});


//$("#recorderr").find("*").prop("disabled", true);
