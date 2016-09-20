    $(document).ready(function(){
    var q_end    = false;
    var q_number = 1;

    $("#q-"+q_number).show();

    $("#next_btn").click(function(){
        $("#q-"+q_number).hide();
        q_number += 1;
        $("#q-"+q_number).show();

        if (q_number == 10) {
            $("#next_btn").hide();
            $("#end_btn").show();
        }
    });
    $('#clock').countdown('2016/09/24', function(event) {
  $(this).html(event.strftime('%D Dias %H:%M:%S'));
});
});


