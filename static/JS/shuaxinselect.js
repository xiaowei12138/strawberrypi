function loadPrograme(){
        $.ajax({
            url : '{% url "abnomal" %}',
            type : 'GET',
            async : false,
            datatype : 'json',
            success : function(data) {
                if(data){
                    var programme_sel=[];
                    programme_sel.push('<option value="" selected>请选择</option>')
                    for(var i=0,len=data.length;i<len;i++){
                        var programme = data[i];
                        programme_sel.push('<option value="'+programme._id+'">'+programme.programme_name+'</option>')
                    }
                    $("#btn1").html(programme_sel.join(' '));
                }
            },
            error : function() {
                alert('查询节目异常');
            }
        });
    }

function loadPrograme1(){
        $.ajax({
            url : '{% url "abnomal" %}',
            type : 'GET',
            async : false,
            datatype : 'json',
            success : function(data) {
                if(data){
                    var programme_sel=[];
                    programme_sel.push('<option value="" selected>请选择</option>')
                    for(var i=0,len=data.length;i<len;i++){
                        var programme = data[i];
                        programme_sel.push('<option value="'+programme._id+'">'+programme.programme_name+'</option>')
                    }
                    $("#btn2").html(programme_sel.join(' '));
                }
            },
            error : function() {
                alert('查询节目异常');
            }
        });
    }


function get_option(){
    var s1 = $('#btn1').find("option:selected").text();
    var s2 = $('#btn2').find("option:selected").text();
    var s3 = $('#btn3').find("option:selected").text();
    finas= s1 +s2 + s3;
    return s1,s2,s3;
}


            var d = new Array();
			d[0] = ["植株A+20171127","植株B+20180417","植株C+20180321"];
			d[1] = ["植株D+20180111","植株E+20171211","植株1+20180412"];
			d[2] = ["植株3+20170711","植株2+20180214","植株3+20171027"];
			d[3] = ['植株①+20180511' ,'植株②+20171107'];
			d[4] = ["植株4+20170721","植株2+20180514"];
			d[5] = ['暂无'];
			function setMajor() {
				var index = $("[name = department]").val();
				var major = $("[name = major]");
				if(index!=-1) {
					// 清空专业下拉列表
					major.empty();
					for(i=0;i<d[index].length;i++) {
						// 产生一个option,参数为(内容,位置);
						var o = new Option(d[index][i],i+1);
						// 将option追加到下拉列表末尾
						major.append(o);
					}
				} else {
					// 清空专业下拉列表
					major.empty();
				}
			}





