window.onload= function () {
    checkphone();
};

function checkphone() {
    setTimeout(checkphone,1000*60*2);
   var  host = window.location.host;
   var  url = "http://" + host + "/godzilla/cachemanager/redisphonecheckstatus";


   var value = document.getElementById("phonelist");
   //表格行数
   var row = value.rows.length;
   // //表格列数
    var cell = value.rows.item(0).cells.length;

    var arrydata = [];
    for (var i=0;i<row;i++)
        // alert(value.rows[i].cells[0].innerText);
        arrydata.push({"phone":value.rows[i].cells[1].innerText})
        arrydata.shift();
    //数组转化json
    var phonedata  = JSON.stringify(arrydata);
    // alert(phonedata);
    $.ajax({
        type: "POST",
        url: url,
        dataType: "json",
        data: phonedata
    })

}