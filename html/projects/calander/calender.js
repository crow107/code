var Months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
for(i = 1; i<=Months.length;i++){
    if(i%2!=0 && i<8){
        var days= 31
    }
    if(i>=8 && i%2==0){
        var days = 31
    }
    if (i==2){
        var days = 28;
    }
    if(i%2==0 && i<8 && i!=2) {
        var days = 30;
    }
    if(i%2!=0  && i>=8){
        var days = 30;
    }

    var callingdiv = document.getElementById("calender");
    var frame = document.createElement('div');
    var monthNum = 'MonthNum'+i;
    frame.innerHTML = '<p>'+Months[i-1]+'</p>'
    frame.setAttribute("id",monthNum);
    frame.setAttribute("class",'Month container');
    callingdiv.appendChild(frame);

}