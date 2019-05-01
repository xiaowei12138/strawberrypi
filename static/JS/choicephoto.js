$(document).ready(function(){
    $("#sum").click(function(){
    var a  = $("#a").val();
    var b  = $("#b").val();
    $.get("/add/",{'a':a,'b':b},function(ret){
        $('#result').html(ret.result)
        })
    });
});

$(document).show_photo(function(){
    $("button").click(function(){
        $(this).show();
    })
})

$(document).get_json(function(){
    $.getJSON('viewname',function(ret){
        for(var i = ret.length-1; i>=0;i--){
            $('#list_result').append(' ' + ret[i])
        };
    })
})

$(document).get_data(function(){
    $.getJSON('数据分析',function(ret){
        for(var i = 0; i<ret.length; i++){
        $("element").append(' ' + ret[i]);
        };
    })
})

$(document).get_newdata(function(){
    var  name = $('#test1').val();
    return name;
})



