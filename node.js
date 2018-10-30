const express = require('express');
const ps = require('python-shell');
const morgan = require('morgan');
const path = require('path');
const ip = require('ip');
const app = express();

app.use(morgan('dev'));
app.use(express.static(__dirname + '/src'));

//GET args then send result
app.get('/res/api', (req, res, next) => {
  let options = {
    args: [req.query.light]
  };
  ps.PythonShell.run('main.py', options, (err, results) => {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    // console.log(results);
    res.status(200).json({ res: results });
  });
});

//Serve webpage
app.get(
  '/',
  (req, res) => res.sendFile(path.join(__dirname + '/src/index.html'))
  // res.send("Try: http://localhost:3000/res/api?light=red")
);

// app.listen(3000, () => console.log('Example app listening on port 3000!'));
const port = 3000;
const localip = ip.address();
app.listen(port, () =>
  console.log(
    '\x1b[35m',
    `Running on http://localhost:${port} \nor http://${localip}:${port}`
  )
);
