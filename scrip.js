var d = new Date(); // for now
var hours = d.getHours(); 
// d.getMinutes(); 
// d.getSeconds(); 

if (hours >= 18){
    $("#content").css({"color":"#fff",'background-color':'#333'});
} 