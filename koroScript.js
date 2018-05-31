console.log("hello world!")
var cards = document.querySelectorAll('.left-player-card');
console.log(cards)
cards.forEach(function(element){
	element.onclick = function(event){
	console.log(event)
	console.log(event.target.alt)

	}
});