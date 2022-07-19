#!/usr/bin/node

// writes a string to a file

fs = require('fs')

fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) throw err;
});
