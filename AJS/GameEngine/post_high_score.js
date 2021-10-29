function getCookie(name) {
  var cookieValue = null;

  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');

    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);

      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


var data_transmit_enable = 1;
function transmitToServer(data){
  if(data_transmit_enable == 1){
    data_transmit_enable = 0;
    $.ajax({
      method: 'POST',
      headers: {'X-CSRFToken': getCookie('csrftoken')},
      url: 'add_score/',
      data: data,
      success: function(){
        data_transmit_enable = 1;
      },
      error: function(xhr, status, err){
        console.log("Error " + xhr.status);
        data_transmit_enable = 1;
      }
    });
  }
}

function getLeaderboardData(){
  if(data_transmit_enable == 1){
    data_transmit_enable = 0;
    document.querySelector("main_menu").classList.add("invisible");
    hideEndScreen();
    $.ajax({
      method: 'GET',
      headers: {'X-CSRFToken': getCookie('csrftoken')},
      url: 'add_score/',
      success: function(data){
        data_transmit_enable = 1;
        leaderboard_data = data;
        leaderboard();
      },
      error: function(xhr, status, err){
        console.log("Error " + xhr.status);
        data_transmit_enable = 1;
      }
    });
  }
}