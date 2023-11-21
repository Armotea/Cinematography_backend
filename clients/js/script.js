cinematography = document.querySelector('.cinematography')
category = document.querySelector('.category')
cats = document.querySelector('.cats')
categoryBtn = document.querySelector('.categoryBtn')


categoryBtn.addEventListener('click', async function() {
  category.style.display = 'flex'
  const response = await fetch("http://127.0.0.1:8000/getGenres/", {
      method: "GET",
  });
  result = await response.json();
  for (i of result){
    cats_li = cats.appendChild(document.createElement('li'))
    p = cats_li.appendChild(document.createElement('p'))
    h = cats_li.appendChild(document.createElement('h'))
    p.innerHTML = i.genre_name
    p.href = '#'
    h.innerHTML = i.description
    let id = i.id
    let genre_name = i.genre_name
    p.addEventListener('click', async function(){
      const response = await fetch(`http://127.0.0.1:8000/getCinematographyByGenres/{id}?genre=${id}`, {
        method: "GET",
      });
      result = await response.json();
      for (i of result){
        div = cinematography.appendChild(document.createElement('div'))
        div.classList.add('cinematographyElement')
        cinemaName = div.appendChild(document.createElement('h'))
        cinemaGenre = div.appendChild(document.createElement('p'))
        cinemaDirector = div.appendChild(document.createElement('p'))
        cinemaDescription = div.appendChild(document.createElement('p'))
        cinemaName.innerHTML = i.name
        cinemaGenre.innerHTML = 'Жанр: ' + genre_name
        cinemaDirector.innerHTML = 'Режиссёр: ' + i.director
        cinemaDescription.innerHTML = i.description
      };
  }, {once:true})}
}, {once:true})