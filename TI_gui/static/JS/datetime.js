function selecttime()
  {
   var xx1 = document.getElementsByName("min_day");
   var xx2 = document.getElementsByName("max_day");
   var s="";
   var t="";
   for (var i=0;i<xx2.length ;i++ )
   {
    if(xx1[i].tagName == 'TD')
     t= t + xx2[i].innerText;
     //alert(xx[i].innerText);
    else
    {
     if(xx2[i].tagName == 'INPUT')
     {
      t += xx2[i].value;
      //由于没有选择日期，默认值是空串
      //if(xx[i].value == null || xx[i].value == 'Undefined' || xx[i].value == "")
      // alert(xx[i].value);
     }
    }
    if( i % 2 == 1)
     t+=";";
   }
   for (var i=0;i<xx1.length ;i++ )
   {
    if(xx1[i].tagName == 'TD')
     s= s + xx1[i].innerText;
     //alert(xx[i].innerText);
    else
    {
     if(xx1[i].tagName == 'INPUT')
     {
      s += xx1[i].value;
      //由于没有选择日期，默认值是空串
      //if(xx[i].value == null || xx[i].value == 'Undefined' || xx[i].value == "")
      // alert(xx[i].value);
     }
    }
    if( i % 2 == 1)
     s+=";";
   }
   var yy = document.getElementById("sp");
   yy.innerHTML = s + ";"+ t;
   alert(s)
   alert(t)
   //document.write("abcdefg<hr>");
   //alert(xx.length);
   return s,t;
  }
var window = $('#photo')
function myrefresh() {
    window.location.reload();
}
//setTimeout('myrefresh()', 3000);