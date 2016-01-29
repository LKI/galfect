function typewriter(id, str, pos) {
  var text = str.slice(0, pos);
  document.getElementById(id).innerHTML = text;
  if (text === str) return;
  return setTimeout(function(){typewriter(id, str, pos + 1);}, 30);
};

function show(id, num) {
  if (num < strs.length) {
    $('#'+id).fadeOut(200);
    setTimeout(function(){
      $('#'+id).fadeIn();
      typewriter(id, strs[num], 0);
    }, 200);
  }
}
