$(document).ready(function(){
    var cell6 = $('#cell6');
   $('#btn').click(function(){
        cell6.children().remove();
        cell6.load('cell6.html #cell6');
   });
   var cell6 = $('#cell6');
   $('#btn').click(function(){
    show_newdata('cell6');

   });
   function show_newdata(param){
    cell6.children().remove();
    $.ajax({
        type: "POST",
        url :"{% url 'real_time'%}",
        data : 'page' + param,
        sucess:function(result){
            cell6.load(result)
        }
    });
   }
   $(function(){
       show_newdata('#cell6');
       setInterval("show_newdata(#cell6)", 10);
   })
});