const express = require('express');
const ps = require('python-shell');
const morgan = require('morgan');
const path = require('path');

const app = express();

app.use(morgan('dev'));
app.use(express.static(__dirname + '/src'));

/* GET home page. */
app.get('/res/api', (req, res, next) => {
  let options = {
    // mode: 'text',
    // pythonPath: './bin/python3',
    // pythonOptions: ['-u'],
    // scriptPath: './',
    args: [req.query.light]
  };
  ps.PythonShell.run('main.py', options, (err, results) => {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log(results);
    res.status(200).json({ res: results[0] });
  });
});

app.get(
  '/',
  (req, res) => res.sendFile(path.join(__dirname + '/src/index.html'))
  // res.send("Try: http://localhost:3000/res/api?light=red")
);

app.listen(3000, () => console.log('Example app listening on port 3000!'));
