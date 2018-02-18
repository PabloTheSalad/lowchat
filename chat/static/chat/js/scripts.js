$(document).ready(function() {
const scrollDown = document.getElementById("frameScroll");
scrollDown.scrollTop = scrollDown.scrollHeight;
});

$(document).ready(function(){
	     	 $("#goMessage").keypress(function(e){
	     	   if(e.keyCode==13){
          $("#buttonGo").click();
	     	   }
	     	 });
	     });
