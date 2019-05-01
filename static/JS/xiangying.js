$(document).ready(function(){
    var page = $('page');
    $('#smbtn').click(function(){
        refresh_data("page");
    });
    function refresh_data(param){
       page.children().remove();
       $.ajax({
            type:"POST",
            url:"{% url 'shujudaoru' %}",
            data :'page' + param,
            sucess:function(result){
                page.load(result);
            }
       });
    }
});

