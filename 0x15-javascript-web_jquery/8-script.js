$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', data => {
     data.results.forEach(l_m => {
     $("#list_movies").append(`<li>${l_m.title}</li>`);
     });
  })
});
