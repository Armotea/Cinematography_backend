fetch('http://127.0.0.1:8000/getGenres/')
  .then((response) => {
    data = response.json()
    console.log(data.Array)
  })