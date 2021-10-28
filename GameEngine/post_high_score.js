var data_transmit_enable = 1;
var begin_fetch_time;
function transmitToServer(data){
  if(data_transmit_enable == 1){
    data_transmit_enable = 0;
    begin_fetch_time = Date.now();
    $.ajax({
      method: "POST",
      url: "",
      data: data,
      success: function(){
        const end_fetch_time = Date.now();
        console.log('Data sent in ', ((end_fetch_time - begin_fetch_time) / 1000) + "s");
        data_transmit_enable = 1;
      },
      error: function(xhr, status, err){
        console.log("Error " + xhr.status);
        data_transmit_enable = 1;
      }
    });
  }
}