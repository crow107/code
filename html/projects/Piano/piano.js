let Num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
let elem = document.getElementById("piano");
for(i=1;i<Num.length;i++){
    let element = document.createElement('button');
    element.setAttribute('class','wb');
    let classname = 'wb'+i+'()';
    element.setAttribute('id',classname);
    element.setAttribute('onclick',classname)
    element.style.backgroundColor='white'
    elem.appendChild(element);
    element.style.borderBottom = '1px solid black'
    element.style.borderLeft = '1px solid black'
    element.style.borderRight = '1px solid black'
    element.style.borderTop = '0'
    element.style.height='200px'
    element.style.width ='50px'
    console.log(element)
    
    if (i>1 && i<27 && i!= 4 && i!=8 &&i!=11 &&i!= 15 && i!=18 &&i!=22 &&i!=26){
        let element1 = document.createElement('button')
        element1.setAttribute('class','wb');
        let k = 'bb'+i;
        element1.setAttribute('id',k);
        elem.appendChild(element1);
        element1.style.marginLeft='-100px'
        element1.style.marginRight='-100px'
        element1.style.zIndex = '2'
        element1.style.height='110px'
        element1.style.width = '23px'
        element1.style.backgroundColor = 'black'
        element1.style.borderBottom = '1px solid black'
        element1.style.borderLeft = '1px solid black'
        element1.style.borderRight = '1px solid black'



    }

    if (i==1){
        element.style.backgroundColor = 'black'
    }
    if(i==26){
        element.style.backgroundColor = 'black'
    }
}

function sound(){
for(i=1;i<Num.length;i++){
    let audioname = 'audio'+i
    audioname.play()
        
    }
}