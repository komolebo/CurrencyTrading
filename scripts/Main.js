function refresh_table() {
    var tmp = "";
    $.get("/currencies", function(data)
    {
        // First row - names
        tmp += '<TR><TD>#</TD>'
        for (var name in data) {
            tmp += '<TD>';
            tmp += name;
            tmp += '</TD>';
        }

        for (var name in data) {
            tmp += '<TR><TD>' + name + '</TD>';

            for (var val in data[name])
                tmp += '<TD>' + data[name][val] + '</TD>';

            tmp += '</TR>';
        }
        $('#table').html(tmp);
    });
};

function load_options() {
    $.get('/currencies', function(data) {
        tmp = "";
        for (var name in data) {
            tmp += '<option>' + name + '</option>';
        }
        $('#option_from').html(tmp);
        $('#option_to').html(tmp);
    })
}

function load_profit() {
    $.get('/sequence', function(data){
        $('#profit').html(data);
    })
}

function add_currency() {
    var currency = $('#new_curr_name').val()

    $.post('/currency/' + currency, currency);

    refresh_table();
    load_options();
}

// For easy put request
jQuery.each( [ "put", "delete" ], function( i, method ) {
  jQuery[ method ] = function( url, data, callback, type ) {
    if ( jQuery.isFunction( data ) ) {
      type = type || callback;
      callback = data;
      data = undefined;
    }

    return jQuery.ajax({
      url: url,
      type: method,
      dataType: type,
      data: data,
      success: callback
    });
  };
});

function change_rate() {
    var from = $('#option_from').val()
    var to = $('#option_to').val()
    var rate = $('#new_rate').val()

    $.put('/currency/' + from + '/' + to + '/' + rate);

    refresh_table();
}