#!/usr/bin/node
/*
 * Gets the content of a webpage and stores it in a file
 * url is passed as a command line argument
 * file path to store content also passed as a command line argument
 */

request = require('request');
fs = require('fs');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
