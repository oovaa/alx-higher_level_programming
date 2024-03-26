// a callback
// console.log('1');
// setTimeout(() => {
//   console.log('hi baroya, nina ,omar and 7amano');
// }, 0);
// console.log('2');

let macb = (str, cb) => {
  cb(str);
};

macb('omar', (name) => {
  console.log(name);
});
