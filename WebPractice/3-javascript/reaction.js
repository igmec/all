var allTimes = new Array();
var currentShape = 1;
var average = 0.0;
var myShape = document.getElementById('shape');

var start = 0;
myShape.onclick = function (){changeShape(myShape);}	


function changeShape (div) {

	//End timer and display result
	if (start != 0){
		var end = new Date().getTime();
		var time = (end - start)/1000;
		allTimes.push(time);
		average = (allTimes.reduce(function(pv, cv) { return pv + cv; }, 0))/allTimes.length;
		document.getElementById("allTimes").innerHTML += ("<p>Shape "+currentShape+": "+time+"s</p>");
		document.getElementById("avgTime").innerHTML = average.toFixed(3)+"s";
		currentShape++;
	}else{
		time = 0;
	}
	
	document.getElementById("time").innerHTML = time;
	
	//Hide shape
	var shapeDiv = div;
	div.style.display = "none";

	//Choose 0 or 1 randomly and make shape
	var type = randNum(0,2);
	
	if(type==0){
		//Circle
		shapeDiv.style.borderRadius = "50%";
	}else{
		//Square
		shapeDiv.style.borderRadius = "3%";
	}

	//Set width and height to random and equal amounts
	var rand = randNum(50, 251);
	shapeDiv.style.width = rand+"px";
	shapeDiv.style.height = rand+"px";

	//Randomly set top and left margin to move the element around
	rand = randNum(50, 251);
	shapeDiv.style.marginTop = rand+"px";
	rand = randNum(50, 301);
	shapeDiv.style.marginLeft = rand+"px";

	//Set a random colour for element
	shapeDiv.style.backgroundColor = makeColour();


	setTimeout(function(){
		start = new Date().getTime();
		div.style.display = "block";
	}, randNum(250,1800));
	
	return shapeDiv;
}


function makeColour() {
	var value;
	var colour = "";

	for(var i=0; i<3; i++){
		value = randNum(0, 251);
		colour += value.toString(16);
	}

	if (colour.length != 6){
		colour = makeColour();
	} else {
		colour = "#"+colour;
	}

	return (colour);
}

function randNum(start, end) {
	return Math.floor(Math.random()*(end-start)) + start;
}