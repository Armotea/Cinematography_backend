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
    a = cats_li.appendChild(document.createElement('a'))
    a.innerHTML = i.genre_name
    a.href = '#'
    let id = i.id
    a.addEventListener('click', async function(){
      const response = await fetch(`http://127.0.0.1:8000/getCinematographyByGenres/{id}?genre=${id}`, {
        method: "GET",
      });
      result = await response.json();
      for (i of result){
        h = cinematography.appendChild(document.createElement('h'))
        h.innerHTML = i.name
      };
  }, {once:true})}
}, {once:true})