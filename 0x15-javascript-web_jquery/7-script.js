$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', data => {
     $("#character").append(`<p>${data.name}</p>`);
  });
});
