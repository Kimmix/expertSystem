const express = require("express");
const app = express();
const PythonShell = require("python-shell");

/* GET home page. */
app.get("/res/api", (req, res, next) => {
  let options = {
    mode: "text",
    pythonPath: "./bin/python3",
    scriptPath: "./",
    args: [req.query.light]
  };

  PythonShell.run("main.py", options, (err, results) => {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log(results);
    res.json({ res: results });
  });
});

app.get("/", (req, res) =>
  res.send("Try: http://localhost:3000/res/api?light=red")
);

app.listen(3000, () => console.log("Example app listening on port 3000!"));
//Hollo Word
