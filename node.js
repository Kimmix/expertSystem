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
    args: [
      req.query.mcharaterist,
      req.query.scharaterist,
      req.query.color,
      req.query.feature
    ]
  };
  //Run animal.py
  ps.PythonShell.run('animal.py', options, (err, results) => {
    // results is an array consisting of messages collected during execution
    if (err) throw err;
    console.log(results);
    res.status(200).json({ res: results });
  });
});

//Serve webpage
app.get('/', (req, res) =>
  res.sendFile(path.join(__dirname + '/src/index.html'))
);

//Listen Server
const PORT = process.env.PORT || 5000;
const localip = ip.address();
app.listen(port, () =>
  console.log(
    '\x1b[35m',
    `Running on http://localhost:${port} \nor http://${localip}:${port}`
  )
);
