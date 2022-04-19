

console.log('working');
if(localStorage.getItem('cart') == null){
var cart = {};
}
else
{

cart = JSON.parse(localStorage.getItem('cart'));
document.getElementById('cart').innerHTML = Object.keys(cart).length;
}
$('.cart').click(function(){
console.log('clicked');
var idstr = this.id.toString();
console.log(idstr);
if (cart[idstr] !=undefined){
cart[idstr] = cart[idstr] + 1;
}
else
{
cart[idstr] = 1;
}
console.log(cart);
localStorage.setItem('cart', JSON.stringify(cart));
// document.getElementById('cart').innerHTML = Object.keys(cart).length;


var total = 0;
for (i = 0; i < Object.values(cart).length; i++) {
  total += Object.values(cart)[i];
}
document.getElementById('cart').innerHTML = total;


});