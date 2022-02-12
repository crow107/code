function yo(){
    
    var men = document.getElementById("menbar")

    
    if (men.style.display =='none'){
        
        let elem = document.getElementById("span1")
        
        elem.style.transform = "rotate(45deg) translate(8px,10px)"
        var elem2 = document.getElementById("span2")
        elem2.style.opacity ='0'
        elem2.style.transform= "rotate(0deg) scale(0.2, 0.2);"
        
        let elem3 = document.getElementById("span3")
        elem3.style.transform = "rotate(-45deg) translate(8px,-10px)" ; 

        var men = document.getElementById("menbar")
        men.style.display ='block'
        
        
}
    else{
        let elem = document.getElementById("span1")
        elem.style.transform = "rotate(0) translate(0, 0)"

        let elem2 = document.getElementById("span2")
        elem2.style.opacity ='1'
    
        let elem3 = document.getElementById("span3")
        elem3.style.transform = "rotate(0) translate(0,0)"
        var men = document.getElementById("menbar")
        men.style.display ='none'

        
    }
}