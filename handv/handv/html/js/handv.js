function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        	}
    	}
	}
    return cookieValue;
}

//增加一个名为 IsPicture 的函数作为
// String 构造函数的原型对象的一个方法。
String.prototype.isPicture = function()
{
    //判断是否是图片 - strFilter必须是小写列举
    var strFilter=".jpeg|.gif|.jpg|.png|.bmp|.pic|.JPEG|.GIF|.JPG|.PNG|.BMP|.PIC|"
    if(this.indexOf(".")>-1)
    {
        var p = this.lastIndexOf(".");
        //alert(p);
        //alert(this.length);
        var strPostfix=this.substring(p,this.length) + '|';        
        strPostfix = strPostfix.toLowerCase();
        //alert(strPostfix);
        if(strFilter.indexOf(strPostfix)>-1)
        {
            //alert("True");
            return true;
        }
    }        
    //alert('False');
    return false;            
}
$(document).ready(function(){
	$("#submit").click(function(){
		$(this).attr("disabled","disabled");
	});
});