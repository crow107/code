window.onscroll = function() {scorl()} 
var main = document.getElementById("main1");
window.onload = function(){magic()}

function magic(){
    document.getElementById("downloadCv").style.display="none";
    setTimeout(()=> {main.style.display ="none" ;document.getElementById("downloadCv").style.display="block"},4200 );
}

function scorl()
    {var windowscrol = window.scrollY;
    var name = document.getElementById("name2");
    var nevbar1 = document.getElementById('nevbar');

    if(windowscrol>180){
        nevbar1.style.backgroundColor = 'rgb(153,217,234)';
        name.style.color = 'white'
        
    }
    else{
        nevbar1.style.backgroundColor = 'rgb(0,0,0,0)';
        name.style.color = 'rgb(153,217,234)'
    }
}

function home(){
    window.scroll({
        top: 0, 
        left: 0, 
        behavior: 'smooth'
      });
}


function about(){
    window.scroll({
        top: 750, 
        left:0 , 
        behavior: 'smooth'
      });
}


function Skills(){
    window.scroll({
        top: 1536, 
        left:0 , 
        behavior: 'smooth'
      });
}

function Projects(){
    window.scroll({
        top: 2350, 
        left:0 , 
        behavior: 'smooth'
      });
}

function dCv(x){
    console.log(x);
    window.open("https://drive.google.com/file/d/1A1DIvXhqzPjYDuliVPwNjLRuhBRObbpa/view?usp=sharing","_blank")
    x.style.color = "cyan";
    setTimeout(() => {x.style.color = "white";},500);
}