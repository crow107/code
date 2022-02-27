window.onscroll = function() {scorl()}

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
    window.scrollTo(0,0);
}

function about(){
    window.scrollTo(0,694.2857055664062);
}


function Skills(){
    window.scrollTo(0,1250);
}

function Projects(){
    window.scrollTo(0,0)
}