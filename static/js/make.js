import Spreadsheet from "x-data-spreadsheet";

// If you need to override the default options, you can set the override
// const options = {};
// new Spreadsheet('#x-spreadsheet-demo', options);
const s = new Spreadsheet("#xspreadsheet")
.loadData({}) // load data
.change(data => {
    console.log('fuckk')
    console.log(data)
    // save data to db
});

// data validation
s.validate()