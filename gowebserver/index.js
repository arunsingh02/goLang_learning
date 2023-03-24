/*
Part of exercise file for go lang course
*/

const express = require('express')
const app = express()
const port = 8000

app.use(express.json()); 
app.use(express.urlencoded({extended: true}));

app.get('/', (req, res) => {
  res.status(200).send("Welcome to arunsingh go server")
})

app.get('/get', (req, res) => {
    res.status(200).json({message: "Hello from arunsingh02 github account."})
  })


app.post('/post', (req, res) => {
    let myJson = req.body;      // your JSON
	
	res.status(200).send(myJson);
})

app.post('/postform', (req, res) => {
    res.status(200).send(JSON.stringify(req.body));
})
  

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})