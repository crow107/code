var i =1;
var j = 6;
var arr1 = ["moneyheist.png","net1.jpg","net2.jpg","net3.jpg","net4.jpg","net5.jpg","squidgames.jpg"];
function clicktopleft() {
    if (j<=6){
        
        console.log(arr1[j]);
        document.getElementById("moneyheist").src = arr1[j];
        j = j -1;}
    else{
        j=0
    }
}
    

function clicktopright(){
    if (i<7){
        
        console.log(arr1[i]);
        document.getElementById("moneyheist").src = arr1[i];
        i = i +1;}
    else{
        i=0
    }
}
var img = document.getElementsByClassName('box'); 
var width = img.clientWidth;
var height = img.clientHeight;
console.log(width)

function mover1(obj){
    obj.innerHTML =`<p> <h3>Alive</h3></p>   <p>1h 39m - 2020 </p>`
}
function mout1(obj){
    obj.innerHTML = ""
}
function mover2(obj){
    obj.innerHTML =`<p> <h3>SooryaVanshi</h3></p>   <p>2h 0m - 2021 </p>`
}
function mout2(obj){
    obj.innerHTML = ""
}
function mover3(obj){
    obj.innerHTML =`<p> <h3>Red Notice</h3></p><p>1h 55m - 2021 </p>`
}
function mout3(obj){
    obj.innerHTML = ""
}
function mover4(obj){
    obj.innerHTML =`<p> <h4>Spiderman:Far from Home</h4></p>  <p>2h 10m - 2019 </p>`
}
function mout4(obj){
    obj.innerHTML = ""
}
function mover5(obj){
    obj.innerHTML =`<p> <h3>Joker</h3></p>  <p>2h 2m - 2019 </p>`
}
function mout5(obj){
    obj.innerHTML = ""
}
function mover6(obj){
    obj.innerHTML =`<p> <h3>Venom</h3></p>   <p>1h 39m - 2020 </p>`
}
function mout6(obj){
    obj.innerHTML = ""
}
function mover7(obj){
    obj.innerHTML =`<p> <h4>Chandinigarh Kare Aashiqui</h4></p>   <p>1h 39m - 2020 </p>`
}
function mout7(obj){
    obj.innerHTML = ""
}
function mover8(obj){
    obj.innerHTML =`<p> <h3>Dhamaka</h3></p> <p>1h 39m - 2020 </p>`
}
function mout8(obj){
    obj.innerHTML = ""
}
function mover9(obj){
    obj.innerHTML =`<p> <h4>Don't Breathe 2</h4></p>   <p>1h 39m - 2020 </p>`
}
function mout9(obj){
    obj.innerHTML = ""
}
function mover10(obj){
    obj.innerHTML =`<p> <h3>Bulbul</h3></p>   <p>1h 39m - 2020 </p>`
}
function mout10(obj){
    obj.innerHTML = ""
}
function mover11(obj){
    obj.innerHTML =`<p> <h3>Hulk</h3></p>  <p>1h 39m - 2020 </p>`
}
function mout11(obj){
    obj.innerHTML = ""
}
function mover12(obj){
    obj.innerHTML =`<p> <h3>Kong:Skull Island</h3></p>   <p>1h 39m - 2020 </p>`
}
function mout12(obj){
    obj.innerHTML = ""
}
function mover13(obj){
    obj.innerHTML =`<p> <h3>Spiderman 3</h3></p>   <p>1h 39m - 2020 </p>`
}
function mout13(obj){
    obj.innerHTML = ""
}
function mover14(obj){
    obj.innerHTML =`<p> <h3>Men In Black</h3></p>  <p>1h 39m - 2020 </p>`
}
function mout14(obj){
    obj.innerHTML = ""
}
function mover15(obj){
    obj.innerHTML =`<p> <h3>Godzilla</h3></p>   <p>1h 39m - 2020 </p>`
}
function mout15(obj){
    obj.innerHTML = ""
}
function mover16(obj){
    obj.innerHTML =`<p> <h4>Spiderman:Homecoming</h4></p>   <p>1h 39m - 2020 </p>`
}
function mout16(obj){
    obj.innerHTML = ""
}

function mover17(obj){
    obj.innerHTML =`<p> <h3>Punisher</h3></p>  <p>1h 39m - 2020 </p>`
}
function mout17(obj){
    obj.innerHTML = ""
}
function mover18(obj){
    obj.innerHTML =`<p> <h3>Enola holmes</h3></p>  <p>1h 39m - 2020 </p>`
}
function mout18(obj){
    obj.innerHTML = ""
}
function mover19(obj){
    obj.innerHTML =`<p> <h4>Now You See Me 2</h4></p>  <p>1h 39m - 2020 </p>`
}
function mout19(obj){
    obj.innerHTML = ""
}
function nighmode(){
    var elem = document.getElementsByTagName("body")
    if (elem[0].style.backgroundColor=="white"){
        elem[0].style.background = "black";
        var elem = document.getElementsByTagName("h2");
        elem[0].style.color ="white";
        elem[1].style.color ="white";

    }
    else{
        elem[0].style.background ="white";
        var elem = document.getElementsByTagName("h2")
        elem[0].style.color ="black"
        elem[1].style.color ="black"
    }

    
}
    

function playit(){
    console.log("hello")
}