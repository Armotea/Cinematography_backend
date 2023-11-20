// fetch('http://127.0.0.1:8000/getGenres/')
//   .then((response) => {
//     data = response.json()
//     console.log(data.Array)
//   })

category = document.querySelector('.category')
categoryBtn = document.querySelector('.categoryBtn')
categoryBtn.addEventListener('click', async function() {
  const response = await fetch("http://127.0.0.1:8000/getGenres/", {
      method: "GET",
    });
    result = await response.json();
    result = JSON.stringify(result)
    console.log(result)
    result = JSON.parse(result)
    console.log(result)
    for (i of result){
       a = category.appendChild(document.createElement('a'))
       a.classList.add('categories')
       a.innerHTML = i.genre_name
       a.href = 'index.html'
    }
})
// category = document.querySelector('.category')
// async function uploadMultiple(){
//     const response = await fetch("http://127.0.0.1:8000/getGenres/", {
//       method: "GET",
//     });
//     result = await response.json();
//     result = JSON.stringify(result)
//     console.log(result)
//     result = JSON.parse(result)
//     console.log(result)
//     for (i of result){
//        a = category.appendChild(document.createElement('a'))
//        a.classList.add('categories')
//        a.innerHTML = i.genre_name
//        a.href = 'index.html'
//     }
// }
