window.onscroll = function() {scorl()}

function scorl()
    {var windowscrol = window.scrollY;
    var name = document.getElementById("name2");
    var nevbar1 = document.getElementById('nevbar');

    if(windowscrol>180){
        
        nevbar1.style.backgroundColor = '#ffca58';
        name.style.color = 'white'
        
    }
    else{
        nevbar1.style.backgroundColor = 'rgb(0,0,0,0)';
        name.style.color = '#ffca58'
    }
}
